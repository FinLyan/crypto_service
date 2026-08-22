import pytest
from rest_framework.test import APIClient

pytestmark = pytest.mark.django_db


@pytest.fixture
def api_client():
    return APIClient()


def test_ciphers_list(api_client):
    response = api_client.get("/api/v1/ciphers/")
    assert response.status_code == 200
    ids = {c["id"] for c in response.json()}
    assert ids == {"caesar", "vigenere", "xor", "fernet"}


def test_encrypt_ok(api_client):
    response = api_client.post(
        "/api/v1/encrypt/", {"cipher": "caesar", "key": "3", "text": "abc"}, format="json"
    )
    assert response.status_code == 200
    assert response.json() == {"result": "def"}


def test_round_trip(api_client):
    enc = api_client.post(
        "/api/v1/encrypt/", {"cipher": "xor", "key": "k", "text": "Привет 🎉"}, format="json"
    )
    dec = api_client.post(
        "/api/v1/decrypt/", {"cipher": "xor", "key": "k", "text": enc.json()["result"]}, format="json"
    )
    assert dec.json() == {"result": "Привет 🎉"}


def test_encrypt_invalid_key_400(api_client):
    response = api_client.post(
        "/api/v1/encrypt/", {"cipher": "caesar", "key": "xyz", "text": "abc"}, format="json"
    )
    assert response.status_code == 400
    assert "error" in response.json()


def test_encrypt_unknown_cipher_400(api_client):
    response = api_client.post(
        "/api/v1/encrypt/", {"cipher": "nope", "key": "3", "text": "abc"}, format="json"
    )
    assert response.status_code == 400


def test_encrypt_missing_fields_400(api_client):
    response = api_client.post("/api/v1/encrypt/", {"cipher": "caesar"}, format="json")
    assert response.status_code == 400


def test_history_records_operations(api_client):
    api_client.post("/api/v1/encrypt/", {"cipher": "caesar", "key": "3", "text": "abc"}, format="json")
    api_client.post("/api/v1/encrypt/", {"cipher": "xor", "key": "k", "text": "hi"}, format="json")
    response = api_client.get("/api/v1/history/")
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 2
    assert {r["cipher_id"] for r in data} == {"caesar", "xor"}
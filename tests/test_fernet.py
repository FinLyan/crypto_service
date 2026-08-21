import pytest
from cryptography.fernet import Fernet
from crypto_core.fernet import FernetCipher
from crypto_core.exceptions import InvalidKeyError, InvalidTextError, DecryptionError

cipher = FernetCipher()

KEY1 = Fernet.generate_key().decode()
KEY2 = Fernet.generate_key().decode()

def test_round_trip_any_symbols():
    texts = ["Hello, мир! 123", "Привет 🎉", "abc XYZ !!!"]
    for key in (KEY1, KEY2):
        for text in texts:
            assert cipher.decrypt(cipher.encrypt(text, key), key) == text

def test_encrypt_unique_tokens():
    assert cipher.encrypt("abc", KEY1) != cipher.encrypt("abc", KEY1)

def test_wrong_key_raises():
    token = cipher.encrypt("Привет", KEY1)
    with pytest.raises(DecryptionError):
        cipher.decrypt(token, KEY2)

def test_garbage_token_raises():
    with pytest.raises(DecryptionError):
        cipher.decrypt("!!!not a token!!!", KEY1)

def test_invalid_key_raises():
    with pytest.raises(InvalidKeyError):
        cipher.encrypt("abc", "abc")

def test_empty_text_raises():
    with pytest.raises(InvalidTextError):
        cipher.encrypt("", KEY1)
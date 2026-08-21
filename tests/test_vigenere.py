import pytest
from crypto_core.vigenere import VigenereCipher
from crypto_core.exceptions import InvalidKeyError, InvalidTextError

cipher = VigenereCipher()

def test_encrypt_known_vector():
    assert cipher.encrypt("ATTACKATDAWN", "LEMON") == "LXFOPVEFRNHR"

def test_encrypt_different_alphabets_ru():
    assert cipher.encrypt("Hello, мир!", "ключ") == "Sqqjz, шжз!"

def test_encypt_different_alphabets_en():
    assert cipher.encrypt("Hello, мир!", "key") == "Rijvs, дтф!"

def test_cross_language_round_trip():
    text = "Hello, мир!"
    for key in ("ключ", "key", "КлючKey"):
        assert cipher.decrypt(cipher.encrypt(text, key), key) == text

def test_invalid_key_raises():
    with pytest.raises(InvalidKeyError):
        cipher.encrypt("abc", "3")

def test_empty_text_raises():
    with pytest.raises(InvalidTextError):
        cipher.encrypt("", "abc")
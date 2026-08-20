import pytest
from crypto_core.caesar import CaesarCipher
from crypto_core.exceptions import InvalidKeyError, InvalidTextError

cipher = CaesarCipher()

def test_encrypt_known_vector():
    assert cipher.encrypt("abc", "3") == "def"

def test_encrypt_uper_and_KeyNon_str():
    assert cipher.encrypt("XYZ", 3) == "ABC"

def test_encrypt_cyrillic():
    assert cipher.encrypt("абв", 3) == "где"

def test_different_alphabets():
    assert cipher.encrypt("Hello, мир!", "3") == "Khoor, плу!"

def test_decrypt_known_vector():
    assert cipher.decrypt("def", 3) == "abc"

def test_decrypeter_encrypted():
    texts = ["Hello, мир!", "Привет", "abc XYZ", "123 !!!"]
    for key in ("3", "-7", 5):
        for text in texts:
            assert cipher.decrypt(cipher.encrypt(text, key), key) == text

def test_invalid_key_raises():
    with pytest.raises(InvalidKeyError):
        cipher.encrypt("abc", "xyz")


def test_empty_text_raises():
    with pytest.raises(InvalidTextError):
        cipher.encrypt("", "3")
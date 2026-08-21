import pytest
from crypto_core.XOR_cipher import XorCipher
from crypto_core.exceptions import InvalidKeyError, InvalidTextError, DecryptionError

cipher = XorCipher()

def test_encrypt_known_vector():
    assert cipher.encrypt("abc", "abc") == "AAAA"

def test_decrypt_known_vector():
    assert cipher.decrypt("AAAA", "abc") == "abc"

def test_round_trip_any_symbols():
    texts = ["Привет, мир! 123", "hello 🎉", "!!! @@@ ..."]
    for key in ("k", "ключ", "my key!"):
        for text in texts:
            assert cipher.decrypt(cipher.encrypt(text, key), key) == text

def test_invalid_base64_raises():
    with pytest.raises(DecryptionError):
        cipher.decrypt("!!!not base64!!!", "k")

def test_not_utf8_after_xor_raises():
    with pytest.raises(DecryptionError):
        cipher.decrypt("/w==", "k")

def test_invalid_key_raises():
    with pytest.raises(InvalidKeyError):
        cipher.encrypt("abc", "")

def test_empty_text_raises():
    with pytest.raises(InvalidTextError):
        cipher.encrypt("", "k")
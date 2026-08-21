import pytest
from crypto_core.caesar import CaesarCipher
from crypto_core.exceptions import UnsupportedCipherError
from crypto_core.registry import get_cipher, list_ciphers

def test_caesar_in_list():
    ids = [item["id"] for item in list_ciphers()]
    assert "caesar" in ids

def test_get_cipher_return_instance():
    assert isinstance(get_cipher("caesar"), CaesarCipher)

def test_list_ciphers_metadata_shape():
    entry = next(item for item in list_ciphers() if item["id"] == "caesar")
    assert set(entry) == {"id", "name", "description", "key_hint"}
    assert entry["name"] == "Caesar cipher"

def test_get_unknown_cipher():
    with pytest.raises(UnsupportedCipherError):
        get_cipher("enigma")
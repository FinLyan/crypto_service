from .exceptions import UnsupportedCipherError

from .caesar import CaesarCipher
from .vigenere import VigenereCipher
from .XOR_cipher import XorCipher
from .fernet import FernetCipher

_CIPHERS = {cls.cipher_id: cls for cls in (CaesarCipher, VigenereCipher, XorCipher, FernetCipher)}

def get_cipher(cipher_id):
    try:
        return _CIPHERS[cipher_id]()
    except KeyError:
        raise UnsupportedCipherError(f"неподдерживаемый шифр {cipher_id}")

def list_ciphers():
    return[
        {
            "id": cls.cipher_id,
            "name": cls.cipher_name,
            "description": cls.description,
            "key_hint": cls.key_hint
        }
        for cls in _CIPHERS.values()
    ]
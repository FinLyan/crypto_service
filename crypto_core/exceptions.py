class CryptoCoreError(Exception):
    """Base exception for all crypto_core errors."""


class InvalidKeyError(CryptoCoreError):
    """Raised when a key is missing or does not fit the cipher's requirements."""


class InvalidTextError(CryptoCoreError):
    """Raised when the input text is invalid (not a string or empty)."""


class UnsupportedCipherError(CryptoCoreError):
    """Raised when an unknown cipher identifier is requested."""


class DecryptionError(CryptoCoreError):
    """Raised when input looks formally valid but cannot be decrypted."""
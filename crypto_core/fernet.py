from cryptography.fernet import Fernet, InvalidToken
from .base import BaseCipher
from .exceptions import InvalidKeyError, DecryptionError

class FernetCipher(BaseCipher):
    cipher_id = "fernet"
    cipher_name = "Fernet cipher"
    description = (
    "Современное симметричное шифрование на базе проверенной библиотеки cryptography: "
    "AES-128 в режиме CBC плюс HMAC для контроля целостности. Гарантированно обнаруживает "
    "неверный ключ и повреждённые данные; каждый токен уникален благодаря случайному IV "
    "и метке времени."        
)
    key_hint = "Валидный ключ Fernet: строка url-safe base64 длиной 44 символа, генерируется через Fernet"

    def _key_validator(self, key):
        if not isinstance(key, str) or key == "":
            raise InvalidKeyError("ключ должен быть непустой строкой")
        try:
            Fernet(key.encode("ascii"))
        except (ValueError, UnicodeEncodeError):
            raise InvalidKeyError("ключ не является валидным ключом fernet")

    def _encrypt(self, text, key):
        f = Fernet(key.encode("ascii"))
        return f.encrypt(text.encode("utf-8")).decode("ascii")

    def _decrypt(self, text, key):
        f = Fernet(key.encode("ascii"))
        try:
            return f.decrypt(text.encode("ascii")).decode("utf-8")
        except(InvalidToken, UnicodeEncodeError):
            raise DecryptionError("данные повреждены или ключ неверен")

    
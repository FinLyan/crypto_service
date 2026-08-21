from .base import BaseCipher
from .exceptions import DecryptionError
import base64
import binascii

class XorCipher(BaseCipher):
    cipher_id = "xor"
    cipher_name = "XOR cipher"
    description = (
    "Побайтовый XOR текста с повторяющимся ключом. Поддерживает любые символы, "
    "включая пробелы, пунктуацию и эмодзи; результат шифрования кодируется в base64. "
    "При расшифровке повреждённых данных или неверного ключа возвращается ошибка."
)
    key_hint = "Любая непустая строка: буквы, цифры, символы. Чем длиннее и случайнее ключ - тем более стойкое шифрование."

    def _encrypt(self, text, key):
        text_bytes = text.encode("utf-8")
        key_bytes = key.encode("utf-8")
        xored = bytes(b ^ key_bytes[i % len(key_bytes)] for i, b in enumerate(text_bytes))
        return base64.b64encode(xored).decode("ascii")

    def _decrypt(self, text, key):
        key_bytes = key.encode("utf-8")
        try:
            text_bytes = base64.b64decode(text, validate=True)
        except (binascii.Error, UnicodeEncodeError):
            raise DecryptionError("Повреждненные данные - невалидный base64")
        xored = bytes(b ^ key_bytes[i % len(key_bytes)] for i, b in enumerate(text_bytes))
        try:
            return xored.decode("utf-8")
        except UnicodeDecodeError:
            raise DecryptionError("результат не является валидным utf-8, возможно неверный ключ")
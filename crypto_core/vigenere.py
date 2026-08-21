from .base import BaseCipher
from .exceptions import InvalidKeyError

class VigenereCipher(BaseCipher):
    cipher_id = "vigenere"
    cipher_name = "Vigenere cipher"
    description = (
    "Полиалфавитный шифр: каждая буква сдвигается на величину, задаваемую "
    "соответствующей буквой ключа-слова. Поддерживаются русский и английский "
    "алфавиты, регистр сохраняется; не-буквы не изменяются."
)
    key_hint = "Слово из русских или латинских букв, например 'LEMON' или 'КЛЮЧ'."

    russian = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    english = "abcdefghijklmnopqrstuvwxyz"
    ALPHABETS = (russian, russian.upper(), english, english.upper())

    def _key_validator(self, key):
        if not isinstance(key, str) or key == "":
            raise InvalidKeyError("Ключ должен быть не пустой строкой, сплошным словом например 'key'")
        for char in key:
            if not any(char in alphabet for alphabet in self.ALPHABETS):
                raise InvalidKeyError("Ключ должен быть не пустой строкой, сплошным словом например 'key'")
            
    def _encrypt(self, text, key):
        encrypted_text = []
        key_pos = 0
        for char in text:
            for alphabet in self.ALPHABETS:
                if char in alphabet:
                    shift = self._key_shift(key[key_pos % len(key)])
                    encrypted_text.append(alphabet[(alphabet.index(char) + shift) % len(alphabet)])
                    key_pos += 1
                    break
            else:
                encrypted_text.append(char)
        result = ''.join(encrypted_text)
        return result

    def _decrypt(self, text, key):
        encrypted_text = []
        key_pos = 0
        for char in text:
            for alphabet in self.ALPHABETS:
                if char in alphabet:
                    shift = self._key_shift(key[key_pos % len(key)])
                    encrypted_text.append(alphabet[(alphabet.index(char) - shift) % len(alphabet)])
                    key_pos += 1
                    break
            else:
                encrypted_text.append(char)
        result = ''.join(encrypted_text)
        return result

    def _key_shift(self, key_char):
        for alphabet in self.ALPHABETS:
            if key_char in alphabet:
                return alphabet.index(key_char)
        raise InvalidKeyError("Ключ для шифра виженера должен содержать символы поддерживаемого алфавита")
from .base import BaseCipher
from .exceptions import InvalidKeyError

class CaesarCipher(BaseCipher):
    cipher_id = "caesar"
    cipher_name = "Caesar cipher"
    description = (
    "Классический шифр подстановки: буквы сдвигаются по алфавиту "
    "на заданное число позиций. Поддерживаются русский и английский "
    "алфавиты, регистр сохраняется, остальные символы не изменяются."
)
    key_hint = "Целое число — сдвиг по алфавиту, например '3' или '-3'. Можно передать числом или строкой с числом."

    russian = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    english = "abcdefghijklmnopqrstuvwxyz"
    ALPHABETS = (russian, russian.upper(), english, english.upper())

    def _key_validator(self, key):
        if isinstance(key, int):
            return
        if not isinstance(key, str):
            raise InvalidKeyError("Ключ должен быть не пустой строкой или числом")
        try:
            int(key)
        except:
            raise InvalidKeyError("Ключ должен быть не пустой строкой или числом")
        
    def _encrypt(self, text, key):
        shift = int(key)
        pre_result = []
        for char in text:
            for alphabet in self.ALPHABETS:
                if char in alphabet:
                    position = alphabet.index(char)
                    pre_result.append(alphabet[(position + shift) % len(alphabet)])
                    break
            else:
                pre_result.append(char)
        result = ''.join(pre_result)
        return result

    def _decrypt(self, text, key):
        shift = int(key)
        pre_result = []
        for char in text:
            for alphabet in self.ALPHABETS:
                if char in alphabet:
                    position = alphabet.index(char)
                    pre_result.append(alphabet[(position - shift) % len(alphabet)])
                    break
            else:
                pre_result.append(char)
        result = ''.join(pre_result)
        return result
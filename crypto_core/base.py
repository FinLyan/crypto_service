from .exceptions import InvalidKeyError, InvalidTextError

class BaseCipher:
    cipher_id = ""
    cipher_name = ""
    description = ""
    key_hint = ""
    def _text_validator(self, text):
        if not isinstance(text, str) or text == "":
            raise InvalidTextError ("Текст должен быть не пустой строкой")

    def _key_validator(self, key):
        if not isinstance(key, str) or key == "":
            raise InvalidKeyError ("Ключ должен быть не пустой строкой")
        
    def encrypt(self, text, key):
        self._key_validator(key)
        self._text_validator(text)
        return self._encrypt(text, key)

    def decrypt(self, text, key):
        self._key_validator(key)
        self._text_validator(text)
        return self._decrypt(text, key)

    def _encrypt(self, text, key):
        raise NotImplementedError
    
    def _decrypt(self, text, key):
        raise NotImplementedError
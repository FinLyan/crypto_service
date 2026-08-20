from exceptions import InvalidKeyError, InvalidTextError
class BaseCipher:



    def _keyValidate(self, key):
        if not isinstance(key, str) or key == "":
            raise InvalidKeyError
    def _textValidate(self, text):
        if not isinstance
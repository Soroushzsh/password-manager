import string
import random


class PasswordManager:
    SYMBOLS = ['@', '#', '%', '$', '?']
    UPPERCASE = list(string.ascii_uppercase)
    LOWERCASE = list(string.ascii_lowercase)
    DIGITS = list(string.digits)

    @staticmethod
    def generate_password(length: int = 8) -> str:
        counter = length
        result = ''
        
        counter -= 1
        result += random.choice(PasswordManager.SYMBOLS)

        numbers = round(counter * 0.4)
        counter -= numbers
        for i in range(numbers):
            result += random.choice(PasswordManager.DIGITS)
        
        CHARACTERS_LIST = PasswordManager.UPPERCASE + PasswordManager.LOWERCASE
        for i in range(counter):
            result += random.choice(CHARACTERS_LIST)
        
        result = list(result)
        random.shuffle(result)
        return ''.join(result)
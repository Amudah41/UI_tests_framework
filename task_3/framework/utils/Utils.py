import random
import string


class StringUtils:
    @staticmethod
    def convert_string_to_int(text):
        return int(text.replace(",", ""))

    @staticmethod
    def random_string():
        letters_and_digits = string.ascii_letters + string.digits
        return "".join(
            random.sample(letters_and_digits, random.randint(1, 50))
        )

import random
import string


def generate_email():
    login = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
    return f'{login}@yandex.ru'


def generate_password(length=10):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))


def generate_name(length=6):
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for i in range(length))
    return random_string


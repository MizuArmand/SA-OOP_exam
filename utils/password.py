"""
Модуль для работы с паролями

CHARS - константа, из которой будет формироваться новый пароль
"""

import random

CHARS = '+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'


def get_new_password(length: int = 8) -> str:
    """
    Функция генерации паролей из N-символов

    :param length: Длина пароля
    :return: Новый пароль
    """

    # Чтобы программа не генерила один пароль или строго заданное количество,
    # разрешим пользователю самому решать сколько паролей он хочет сгенерировать и определять лину пароля

    # length = int(input('длина пароля?' + "\n"))

    x = ''

    for i in range(length):
        x += random.choice(CHARS)

    return x


def check_strong_password(pswd: str) -> bool:
    """
    Функция проверяет стойкость пароля

    :param pswd: Пароль для проверки
    :return: Стойкость пароля
    """

    if len(pswd) < 6:
        print('Недопустимый пароль')
        return False
    elif pswd.isdigit() or (pswd.isalpha() and pswd.islower()):
        print('Ненадежный пароль')
    elif (pswd.isdigit() and pswd.lower()) or (pswd.isalpha() and pswd.lower()):
        print('Слабый пароль')
    else:
        print('Надежный пароль')
    return True

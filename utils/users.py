"""
Модуль генерации новых пользователей
"""

import random
import string


def get_new_user_name(name_length: int = 0) -> str:
    """
    Функция генерирует новое имя пользователя

    :param name_length: Длина нового имени
    :return: Новое имя пользователя
    """

    x = ''
    if name_length == 0:
        name_length = random.randint(10, 15)

    for i in range(name_length):
        x += random.choice(string.ascii_letters)

    return x

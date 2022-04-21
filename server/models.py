"""
Модуль для работы с БД
"""

import time


def add_user(login: str, password: str) -> bool:
    """
    Функция добавляет пользователя в БД

    :param login: Логин
    :param password: Пароль
    :return: True если добавлен успешно, иначе False
    """

    print(f"{time.ctime()} - Пользователь {login} добавлен")

    list(password)  # Заглушка, чтобы был использован параметр password

    return True


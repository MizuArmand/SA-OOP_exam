"""
Модуль в котором хранится конфигурация приложения
"""

HOST = '127.0.0.1'
PORT = '5432'


def test_config():
    return {"user": "test", "password": "012345"}


def real_config():
    return {"user": "admin", "password": "543210"}


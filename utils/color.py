"""
Модуль для работы с цветом
"""


def hex_to_rgb(color_hex: str) -> tuple:
    """
    Преобразовываем шестнадцатеричные значения в целые числа с основанием 10
    с помощью функции int() для каждого переменного индекса.

    :param color_hex: Цвет в hex формате
    :return: Кортеж RGB
    """

    color_hex = color_hex.lstrip('#')

    return tuple(int(color_hex[i:i+2], 16) for i in (0, 2, 4))


def rgb_to_hex(color_rgb: tuple) -> str:
    """
    Функия преобразует кортеж RGB в HEX

    :param color_rgb: цвет RGB в виде кортежа
    :return: Цвет в HEX
    """

    return '%02x%02x%02x' % color_rgb


if __name__ == '__main__':
    hex_ = input('Введите номер HEX: ')
    print(hex_to_rgb(hex_))

    print(rgb_to_hex((18, 84, 86)))

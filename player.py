"""
Модуль player.py

Содержит класс Player, который представляет игрока.
"""

class Player:
    """
    Класс игрока.

    Атрибуты:
        color (str): Цвет игрока ('white' или 'black').
    """

    def __init__(self, color):
        """
        Инициализация игрока.

        :param color: Цвет игрока ('white' или 'black').
        """
        self.color = color
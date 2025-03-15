"""
Модуль game.py

Содержит класс Game, который управляет игровым процессом.
"""

from chess_board import ChessBoard
from player import Player


class Game:
    """
    Класс игры. Управляет процессом игры, включая ходы игроков и отображение доски.
    """

    def __init__(self):
        """
        Инициализация игры. Создает доску и игроков.
        """
        self.board = ChessBoard()
        self.players = [Player('white'), Player('black')]
        self.current_player = self.players[0]
        self.move_count = 0

    def start(self):
        """
        Запускает игру. Игроки поочередно делают ходы.
        """
        print('Игра началась!')
        while True:
            self.print_board()
            print(f'Ход игрока {self.current_player.color}')
            from_pos = input('Введите позицию фигуры (например: а2): ')
            to_pos = input('Введите, куда вы хотите сходить (например: а4): ')

            if self.board.move_piece(from_pos, to_pos):
                print('Ход выполнен!')
                self.move_count += 1
                self.current_player = self.players[self.move_count % 2]
            else:
                print('Недопустимый ход. Попробуйте снова')

    def print_board(self):
        """
        Выводит текущее состояние доски в консоль.
        """
        print("  a b c d e f g h")
        for row in range(8):
            print(f"{8 - row} ", end="")
            for col in range(8):
                piece = self.board.board[row][col]
                print(f"{piece.symbol if piece else '.'}", end=" ")
            print(f" {8 - row}")
        print("  a b c d e f g h")
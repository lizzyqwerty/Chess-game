"""
Модуль chess_board.py

Содержит класс ChessBoard, который управляет состоянием шахматной доски и перемещением фигур.
"""

from chess_pieces import Pawn, Rook, Knight, Bishop, Queen, King


class ChessBoard:
    """
    Класс шахматной доски.

    Атрибуты:
        board (list): Двумерный список, представляющий шахматную доску 8x8.
    """

    def __init__(self):
        """
        Инициализация доски. Создает пустую доску и расставляет фигуры.
        """
        self.board = self.create_empty_board()
        self.setup_pieces()

    def create_empty_board(self):
        """
        Создает пустую шахматную доску 8x8.

        :return: Двумерный список, заполненный None.
        """
        return [[None for _ in range(8)] for _ in range(8)]

    def setup_pieces(self):
        """
        Расставляет фигуры на доске в начальной позиции.
        """
        # Белые фигуры
        for i in range(8):
            self.board[6][i] = Pawn('white', self.position_to_notation(6, i))
        self.board[7][0] = Rook('white', self.position_to_notation(7, 0))
        self.board[7][1] = Knight('white', self.position_to_notation(7, 1))
        self.board[7][2] = Bishop('white', self.position_to_notation(7, 2))
        self.board[7][3] = Queen('white', self.position_to_notation(7, 3))
        self.board[7][4] = King('white', self.position_to_notation(7, 4))
        self.board[7][5] = Bishop('white', self.position_to_notation(7, 5))
        self.board[7][6] = Knight('white', self.position_to_notation(7, 6))
        self.board[7][7] = Rook('white', self.position_to_notation(7, 7))

        # Черные фигуры
        for i in range(8):
            self.board[1][i] = Pawn('black', self.position_to_notation(1, i))
        self.board[0][0] = Rook('black', self.position_to_notation(0, 0))
        self.board[0][1] = Knight('black', self.position_to_notation(0, 1))
        self.board[0][2] = Bishop('black', self.position_to_notation(0, 2))
        self.board[0][3] = Queen('black', self.position_to_notation(0, 3))
        self.board[0][4] = King('black', self.position_to_notation(0, 4))
        self.board[0][5] = Bishop('black', self.position_to_notation(0, 5))
        self.board[0][6] = Knight('black', self.position_to_notation(0, 6))
        self.board[0][7] = Rook('black', self.position_to_notation(0, 7))

    def position_to_notation(self, row, col):
        """
        Преобразует координаты (строка, столбец) в шахматную нотацию.

        :param row: Номер строки (0-7).
        :param col: Номер столбца (0-7).
        :return: Позиция в шахматной нотации (например, 'a2').
        """
        return f'{chr(ord("a") + col)}{8 - row}'

    def notation_to_position(self, notation):
        """
        Преобразует шахматную нотацию в координаты (строка, столбец).

        :param notation: Позиция в шахматной нотации (например, 'a2').
        :return: Кортеж (строка, столбец).
        """
        col = ord(notation[0]) - ord('a')
        row = 8 - int(notation[1])
        return row, col

    def get_piece(self, position):
        """
        Возвращает фигуру по указанной позиции.

        :param position: Позиция в шахматной нотации (например, 'a2').
        :return: Объект фигуры или None, если клетка пуста.
        """
        row, col = self.notation_to_position(position)
        return self.board[row][col]

    def move_piece(self, from_pos, to_pos):
        """
        Перемещает фигуру с одной позиции на другую, если ход допустим.

        :param from_pos: Начальная позиция фигуры (например, 'a2').
        :param to_pos: Целевая позиция фигуры (например, 'a4').
        :return: True, если ход выполнен, иначе False.
        """
        piece = self.get_piece(from_pos)
        if piece and piece.can_move(to_pos, self):
            from_row, from_col = self.notation_to_position(from_pos)
            to_row, to_col = self.notation_to_position(to_pos)
            self.board[to_row][to_col] = piece
            self.board[from_row][from_col] = None
            piece.move(to_pos)
            return True
        return False
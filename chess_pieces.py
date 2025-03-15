"""
Модуль chess_pieces.py

Содержит классы всех шахматных фигур. Каждая фигура наследуется от базового класса ChessPiece
и реализует метод can_move, который проверяет, может ли фигура переместиться на указанную позицию.
"""

class ChessPiece:
    """
    Базовый класс для всех шахматных фигур.

    Атрибуты:
        color (str): Цвет фигуры ('white' или 'black').
        position (str): Позиция фигуры на доске в шахматной нотации (например, 'a2').
        symbol (str): Символ фигуры для отображения на доске.
    """

    def __init__(self, color, position):
        self.color = color
        self.position = position
        self.symbol = ' '

    def move(self, new_position):
        self.position = new_position

    def can_move(self, new_position, board):
        raise NotImplementedError('Метод должен быть переопределен')


class Pawn(ChessPiece):
    """
    Класс пешки. Наследуется от ChessPiece.

    Атрибуты:
        symbol (str): Символ пешки ('P' для белых, 'p' для черных).
    """

    def __init__(self, color, position):
        super().__init__(color, position)
        self.symbol = 'P' if color == 'white' else 'p'

    def can_move(self, new_position, board):
        current_row, current_col = board.notation_to_position(self.position)
        new_row, new_col = board.notation_to_position(new_position)

        direction = 1 if self.color == 'white' else -1

        # Ход вперед на одну клетку
        if current_col == new_col and new_row == current_row + direction:
            if board.get_piece(new_position) is None:
                return True

        # Первый ход на две клетки
        if (current_col == new_col and new_row == current_row + 2 * direction) and (
                (self.color == 'white' and current_row == 6) or
                (self.color == 'black' and current_row == 1)
        ):
            intermediate_row = current_row + direction
            intermediate_position = board.position_to_notation(intermediate_row, current_col)
            if (board.get_piece(intermediate_position) is None and
                    board.get_piece(new_position) is None):
                return True

        # Взятие фигуры по диагонали
        if abs(new_col - current_col) == 1 and new_row == current_row + direction:
            target_piece = board.get_piece(new_position)
            if target_piece is not None and target_piece.color != self.color:
                return True

        return False


class Rook(ChessPiece):
    """
    Класс ладьи. Наследуется от ChessPiece.

    Атрибуты:
        symbol (str): Символ ладьи ('R' для белых, 'r' для черных).
    """

    def __init__(self, color, position):
        super().__init__(color, position)
        self.symbol = 'R' if color == 'white' else 'r'

    def can_move(self, new_position, board):
        current_row, current_col = board.notation_to_position(self.position)
        new_row, new_col = board.notation_to_position(new_position)

        if current_row == new_row:  # Ход по горизонтали
            step = 1 if new_col > current_col else -1
            for col in range(current_col + step, new_col, step):
                if board.board[current_row][col] is not None:
                    return False
            return True
        elif current_col == new_col:  # Ход по вертикали
            step = 1 if new_row > current_row else -1
            for row in range(current_row + step, new_row, step):
                if board.board[row][current_col] is not None:
                    return False
            return True
        return False


class Knight(ChessPiece):
    """
    Класс коня. Наследуется от ChessPiece.

    Атрибуты:
        symbol (str): Символ коня ('N' для белых, 'n' для черных).
    """

    def __init__(self, color, position):
        super().__init__(color, position)
        self.symbol = 'N' if color == 'white' else 'n'

    def can_move(self, new_position, board):
        current_row, current_col = board.notation_to_position(self.position)
        new_row, new_col = board.notation_to_position(new_position)

        row_diff = abs(new_row - current_row)
        col_diff = abs(new_col - current_col)
        return (row_diff == 2 and col_diff == 1) or (row_diff == 1 and col_diff == 2)


class Bishop(ChessPiece):
    """
    Класс слона. Наследуется от ChessPiece.

    Атрибуты:
        symbol (str): Символ слона ('B' для белых, 'b' для черных).
    """

    def __init__(self, color, position):
        super().__init__(color, position)
        self.symbol = 'B' if color == 'white' else 'b'

    def can_move(self, new_position, board):
        current_row, current_col = board.notation_to_position(self.position)
        new_row, new_col = board.notation_to_position(new_position)

        if abs(new_row - current_row) == abs(new_col - current_col):
            row_step = 1 if new_row > current_row else -1
            col_step = 1 if new_col > current_col else -1
            row, col = current_row + row_step, current_col + col_step
            while row != new_row and col != new_col:
                if board.board[row][col] is not None:
                    return False
                row += row_step
                col += col_step
            return True
        return False


class Queen(ChessPiece):
    """
    Класс ферзя. Наследуется от ChessPiece.

    Атрибуты:
        symbol (str): Символ ферзя ('Q' для белых, 'q' для черных).
    """

    def __init__(self, color, position):
        super().__init__(color, position)
        self.symbol = 'Q' if color == 'white' else 'q'

    def can_move(self, new_position, board):
        current_row, current_col = board.notation_to_position(self.position)
        new_row, new_col = board.notation_to_position(new_position)

        # Ход как ладья
        if current_row == new_row:  # Ход по горизонтали
            step = 1 if new_col > current_col else -1
            for col in range(current_col + step, new_col, step):
                if board.board[current_row][col] is not None:
                    return False
            return True
        elif current_col == new_col:  # Ход по вертикали
            step = 1 if new_row > current_row else -1
            for row in range(current_row + step, new_row, step):
                if board.board[row][current_col] is not None:
                    return False
            return True

        # Ход как слон
        if abs(new_row - current_row) == abs(new_col - current_col):
            row_step = 1 if new_row > current_row else -1
            col_step = 1 if new_col > current_col else -1
            row, col = current_row + row_step, current_col + col_step
            while row != new_row and col != new_col:
                if board.board[row][col] is not None:
                    return False
                row += row_step
                col += col_step
            return True

        return False


class King(ChessPiece):
    """
    Класс короля. Наследуется от ChessPiece.

    Атрибуты:
        symbol (str): Символ короля ('K' для белых, 'k' для черных).
    """

    def __init__(self, color, position):
        super().__init__(color, position)
        self.symbol = 'K' if color == 'white' else 'k'

    def can_move(self, new_position, board):
        current_row, current_col = board.notation_to_position(self.position)
        new_row, new_col = board.notation_to_position(new_position)

        return abs(new_row - current_row) <= 1 and abs(new_col - current_col) <= 1
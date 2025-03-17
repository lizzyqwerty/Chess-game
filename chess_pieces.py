"""
Модуль chess_pieces.py

Содержит классы всех шахматных фигур. Каждая фигура наследуется от базового класса ChessPiece
и реализует метод get_possible_moves который возвращает список допустимых ходов.
"""
class ChessPiece:
    """Базовый класс для всех шахматных фигур."""
    def __init__(self, color, position):
        self.color = color
        self.position = position # Кортеж (row, col)

    def symbol(self):
        raise NotImplementedError('Метод должен быть переопределен')

    def get_possible_moves(self, board):
        """Возвращает список допустимых ходов."""
        raise NotImplementedError('Метод должен быть переопределен')

class Pawn(ChessPiece):
    """Класс пешки."""
    def symbol(self):
        return 'P' if self.color == 'white' else 'p'

    def get_possible_moves(self, board):
        moves = []
        direction = 1 if self.color == 'white' else -1
        start_row = 1 if self.color == 'white' else 6
        row, col = self.position

        # Ход вперед на одну клетку
        if 0 <= row + direction < 8 and board.is_empty(row + direction, col):
            moves.append((row + direction, col))
            # Ход на две клетки из начальной позиции
            if row == start_row and board.is_empty(row + 2 * direction, col):
                moves.append((row + 2 * direction, col))

        # Взятие по диагонали
        for delta in [-1, 1]:
            new_col = col + delta
            if (0 <= new_col < 8 and 0 <= row + direction < 8 and
            board.has_enemy_piece(row + direction, new_col, self.color)):
                moves.append((row + direction, new_col))

        return moves

class Rook(ChessPiece):
    """Класс ладьи."""
    def symbol(self):
        return 'R' if self.color == 'white' else 'r'

    def get_possible_moves(self, board):
        moves = []
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        row, col = self.position

        for d_row, d_col in directions:
            for i in range(1, 8):
                new_row, new_col = row + i * d_row, col + i * d_col
                if not (0 <= new_row < 8 and 0 <= new_col < 8):
                    break
                if board.is_empty(new_row, new_col):
                    moves.append((new_row, new_col))
                    break
                elif board.has_enemy_piece(new_row, new_col, self.color):
                    moves.append((new_row, new_col))
                else:
                    break
            return moves

class Knight(ChessPiece):
    """Класс коня."""
    def symbol(self):
        return 'N' if self.color == 'white' else 'n'

    def get_possible_moves(self, board):
        moves = []
        row, col = self.position
        possible_jumps = [
            (row + 2, col + 1), (row + 2, col - 1),
            (row - 2, col + 1), (row - 2, col - 1),
            (row + 1, col + 2), (row + 1, col - 2),
            (row - 1, col + 2), (row - 1, col - 2),
        ]
        for new_row, new_col in possible_jumps:
            # Ход в пределах доски
            if 0 <= new_row < 8 and 0 <= new_col < 8:
                if board.is_empty(new_row, new_col) or board.has_enemy_piece(new_row, new_col, self.color):
                    moves.append((new_row, new_col))
        return moves

class Bishop(ChessPiece):
    """Класс слона."""
    def symbol(self):
        return 'B' if self.color == 'white' else 'b'

    def get_possible_moves(self, board):
        moves = []
        directions = [(1, 1), (1, -1), (-1, 1), (-1, -1)]  # диагонали
        row, col = self.position
        for d_row, d_col in directions:
            for i in range(1, 8):
                new_row, new_col = row + i * d_row, col + i * d_col
                if not (0 <= new_row < 8 and 0 <= new_col < 8):
                    break
                if board.is_empty(new_row, new_col):
                    moves.append((new_row, new_col))
                elif board.has_enemy_piece(new_row, new_col, self.color):
                    moves.append((new_row, new_col))
                    break
                else:
                    break
        return moves

class Queen(ChessPiece):
    """Класс ферзя."""
    def symbol(self):
        return 'Q' if self.color == 'white' else 'q'

    def get_possible_moves(self, board):
        moves = []
        # Направления ладьи
        directions_rook = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        # Направления слона
        directions_bishop = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
        all_directions = directions_rook + directions_bishop
        row, col = self.position
        for d_row, d_col in all_directions:
            for i in range(1, 8):
                new_row, new_col = row + i * d_row, col + i * d_col
                if not (0 <= new_row < 8 and 0 <= new_col < 8):
                    break
                if board.is_empty(new_row, new_col):
                    moves.append((new_row, new_col))
                elif board.has_enemy_piece(new_row, new_col, self.color):
                    moves.append((new_row, new_col))
                    break
                else:
                    break
        return moves

class King(ChessPiece):
    """Класс короля."""
    def symbol(self):
        return 'K' if self.color == 'white' else 'k'

    def get_possible_moves(self, board):
        moves = []
        row, col = self.position
        # Все соседние клетки
        possible_moves = [
            (row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1),
            (row + 1, col + 1), (row + 1, col - 1), (row - 1, col + 1), (row - 1, col - 1)
        ]
        for new_row, new_col in possible_moves:
            if 0 <= new_row < 8 and 0 <= new_col < 8:
                if board.is_empty(new_row, new_col) or board.has_enemy_piece(new_row, new_col, self.color):
                    moves.append((new_row, new_col))
        return moves

# Дополнительное задание - 3 новых фигуры
class Deer(ChessPiece):
    """Класс оленя."""
    def symbol(self):
        return 'D' if self.color == 'white' else 'd'

    def get_possible_moves(self, board):
        moves = []
        row, col = self.position
        # Направление слона
        directions_bishop = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
        # Направление коня
        directions_knight =  [
                (row + 2, col + 1), (row + 2, col - 1),
                (row - 2, col + 1), (row - 2, col - 1),
                (row + 1, col + 2), (row + 1, col - 2),
                (row - 1, col + 2), (row - 1, col - 2),
            ]
        all_directions = directions_knight + directions_bishop
        for d_row, d_col in all_directions:
            for i in range(1, 8):
                new_row, new_col = row + i * d_row, col + i * d_col
                if not (0 <= new_row < 8 and 0 <= new_col < 8):
                    break
                if board.is_empty(new_row, new_col):
                    moves.append((new_row, new_col))
                elif board.has_enemy_piece(new_row, new_col, self.color):
                    moves.append((new_row, new_col))
                    break
                else:
                    break
        return moves

class Bear(ChessPiece):
    """Класс медведя."""
    def symbol(self):
        return 'E' if self.color == 'white' else 'e'

    def get_possible_moves(self, board):
        moves = []
        row, col = self.position
        # Ходы ладьи
        directions_rook = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        # Ходы коня
        directions_knight =  [
                (row + 2, col + 1), (row + 2, col - 1),
                (row - 2, col + 1), (row - 2, col - 1),
                (row + 1, col + 2), (row + 1, col - 2),
                (row - 1, col + 2), (row - 1, col - 2),
            ]
        all_directions = directions_rook + directions_knight
        for d_row, d_col in all_directions:
            for i in range(1, 8):
                new_row, new_col = row + i * d_row, col + i * d_col
                if not (0 <= new_row < 8 and 0 <= new_col < 8):
                    break
                if board.is_empty(new_row, new_col):
                    moves.append((new_row, new_col))
                elif board.has_enemy_piece(new_row, new_col, self.color):
                    moves.append((new_row, new_col))
                    break
                else:
                    break
        return moves

class Hunter(ChessPiece):
    """Класс охотника."""
    def symbol(self):
        return 'H' if self.color == 'white' else 'h'

    def get_possible_moves(self, board):
        moves = []
        # Ходит как король
        row, col = self.position
        possible_moves = [
            (row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1),
            (row + 1, col + 1), (row + 1, col - 1), (row - 1, col + 1), (row - 1, col - 1)
        ]
        for new_row, new_col in possible_moves:
            if 0 <= new_row < 8 and 0 <= new_col < 8:
                if board.is_empty(new_row, new_col) or board.has_enemy_piece(new_row, new_col, self.color):
                    moves.append((new_row, new_col))
        return moves





"""
Модуль chess_board.py
Содержит класс ChessBoard, который управляет состоянием шахматной доски и перемещением фигур.
"""

from chess_pieces import Pawn, Rook, Knight, Bishop, Queen, King, Deer, Hunter, Bear

class ChessBoard:
    """Класс шахматной доски."""
    def __init__(self):
        self.board = [[None for _ in range(8)] for _ in range(8)]
        self.setup_pieces()
        self.move_history = []

    def setup_pieces(self):
        # Белые фигуры
        for col in range(8):
            self.board[1][col] = Pawn('white', (1, col))
        self.board[0][0] = Rook('white', (0, 0))
        self.board[0][1] = Knight('white', (0, 1))
        self.board[0][2] = Bishop('white', (0, 2))
        self.board[0][3] = Queen('white', (0, 3))
        self.board[0][4] = King('white', (0, 4))
        self.board[0][5] = Bishop('white', (0, 5))
        self.board[0][6] = Knight('white', (0, 6))
        self.board[0][7] = Rook('white', (0, 7))
        self.board[2][0] = Deer('white', (2,0))
        self.board[2][1] = Bear('white', (2, 1))
        self.board[2][7] = Hunter('white', (2, 7))

        # Черные фигуры
        for col in range(8):
            self.board[6][col] = Pawn('black', (6, col))
        self.board[7][0] = Rook('black', (7, 0))
        self.board[7][1] = Knight('black', (7, 1))
        self.board[7][2] = Bishop('black', (7, 2))
        self.board[7][3] = Queen('black', (7, 3))
        self.board[7][4] = King('black', (7, 4))
        self.board[7][5] = Bishop('black', (7, 5))
        self.board[7][6] = Knight('black', (7, 6))
        self.board[7][7] = Rook('black', (7, 7))
        self.board[5][0] = Deer('black', (5, 0))
        self.board[5][1] = Bear('black', (5, 1))
        self.board[5][7] = Hunter('black', (5, 7))

    def display(self):
        print('  a b c d r f g h')
        for row in range(7, -1, -1):
            print(f'{row + 1} ', end='')
            for col in range(8):
                piece = self.board[row][col]
                print(piece.symbol() if piece else '.', end = ' ')
            print(f'{row + 1}')
        print('  a b c d e f g h')

    def is_empty(self, row, col):
        return self.board[row][col] is None

    def has_enemy_piece(self, row, col, color):
        piece = self.board[row][col]
        return piece is not None and piece.color != color

    def find_king(self, color):
        """Находит позицию короля заданного цвета"""
        for row in range(8):
            for col in range(8):
                piece = self.board[row][col]
                if isinstance(piece, King) and piece.color == color:
                    return (row, col)
            return None

    def is_in_check(self, color):
        """Проверяет, находится ли король под шахом."""
        king_pos = self.find_king(color)
        if not king_pos:
            return False

        enemy_color = 'black' if color == 'white' else 'white'
        for row in range(8):
            for col in range(8):
                piece = self.board[row][col]
                if piece and piece.color == enemy_color:
                    moves = piece.get_possible_moves(self)
                    if king_pos in moves:
                        return True
        return False

    def move_piece(self, from_pos, to_pos):
        """Перемещает фигуру с проверкой шаха."""
        piece = self.board[from_pos[0]][from_pos[1]]
        if not piece or to_pos not in piece.get_possible_moves(self):
            return False

        captured_piece = self.board[to_pos[0]][to_pos[1]]
        self.board[to_pos[0]][to_pos[1]] = piece
        self.board[from_pos[0]][from_pos[1]] = None
        old_position = piece.position
        piece.position = to_pos

        # Проверка не ставит ли шах при ходе короля
        if self.is_in_check(piece.color):
            self.board[from_pos[0]][from_pos[1]] = piece
            self.board[to_pos[0]][to_pos[1]] = captured_piece
            piece.position = old_position

        self.move_history.append((from_pos, to_pos, captured_piece))
        return True

    def undo_move(self):
        if not self.move_history:
            print('Нет ходов для отката')
            return False

        from_pos, to_pos, captured_piece = self.move_history.pop()
        piece = self.board[to_pos[0]][to_pos[1]]

        self.board[from_pos[0]][from_pos[1]] = piece
        self.board[to_pos[0]][to_pos[1]] = captured_piece
        piece.position = from_pos
        return True

def parse_position(pos_str):
    """Преобразует строковую позицию (например, 'e2') в кортеж (row, col)."""
    if len(pos_str) != 2:
        return None
    col = ord(pos_str[0].lower()) - ord('a')
    try:
        row = int(pos_str[1]) - 1
    except ValueError:
        return None
    if 0 <= row < 8 and 0 <= col < 8:
        return (row, col)
    return None






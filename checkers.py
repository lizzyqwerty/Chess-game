class CheckersPiece:
    """Базовый класс для фигур в шашках."""
    def __init__(self, color, position):
        self.color = color  # 'white' или 'black'
        self.position = position  # Кортеж (row, col)

    def symbol(self):
        raise NotImplementedError

    def get_possible_moves(self, board):
        raise NotImplementedError

class Checker(CheckersPiece):
    """Обычная шашка."""
    def symbol(self):
        return 'C' if self.color == 'white' else 'c'

    def get_possible_moves(self, board):
        moves = []
        captures = []
        direction = 1 if self.color == 'white' else -1
        row, col = self.position

        # Проверка ходов вперед
        for delta_col in [-1, 1]:
            new_row = row + direction
            new_col = col + delta_col
            if 0 <= new_row < 8 and 0 <= new_col < 8:
                if board.is_empty(new_row, new_col):
                    moves.append((new_row, new_col))
                elif board.has_enemy_piece(new_row, new_col, self.color):
                    jump_row = new_row + direction
                    jump_col = new_col + delta_col
                    if 0 <= jump_row < 8 and 0 <= jump_col < 8 and board.is_empty(jump_row, jump_col):
                        captures.append((jump_row, jump_col))

        # Взятия обязательны
        return captures if captures else moves

class King(CheckersPiece):
    """Дамка."""
    def symbol(self):
        return 'K' if self.color == 'white' else 'k'

    def get_possible_moves(self, board):
        moves = []
        captures = []
        directions = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
        row, col = self.position

        for d_row, d_col in directions:
            for i in range(1, 8):
                new_row = row + i * d_row
                new_col = col + i * d_col
                if not (0 <= new_row < 8 and 0 <= new_col < 8):
                    break
                if board.is_empty(new_row, new_col):
                    moves.append((new_row, new_col))
                elif board.has_enemy_piece(new_row, new_col, self.color):
                    jump_row = new_row + d_row
                    jump_col = new_col + d_col
                    if 0 <= jump_row < 8 and 0 <= jump_col < 8 and board.is_empty(jump_row, jump_col):
                        captures.append((jump_row, jump_col))
                    break
                else:
                    break

        # Взятия обязательны
        return captures if captures else moves

from checkers_pieces import Checker, King

class CheckersBoard:
    """Доска для шашек."""
    def __init__(self):
        self.board = [[None for _ in range(8)] for _ in range(8)]
        self.setup_pieces()
        self.move_history = []  # Для отката ходов

    def setup_pieces(self):
        """Расстановка шашек."""
        # Черные шашки (вверху)
        for row in range(3):
            for col in range(8):
                if (row + col) % 2 == 1:  # Черные клетки
                    self.board[row][col] = Checker('black', (row, col))
        # Белые шашки (внизу)
        for row in range(5, 8):
            for col in range(8):
                if (row + col) % 2 == 1:
                    self.board[row][col] = Checker('white', (row, col))

    def display(self):
        """Отображение доски."""
        print(' a b c d e f g h')
        for row in range(7, -1, -1):
            print(f'{row + 1} ', end='')
            for col in range(8):
                piece = self.board[row][col]
                print(piece.symbol() if piece else '.', end=' ')
            print(f'{row + 1}')
        print(' a b c d e f g h')

    def is_empty(self, row, col):
        return self.board[row][col] is None

    def has_enemy_piece(self, row, col, color):
        piece = self.board[row][col]
        return piece is not None and piece.color != color

    def move_piece(self, from_pos, to_pos):
        """Перемещение фигуры."""
        piece = self.board[from_pos[0]][from_pos[1]]
        if not piece or to_pos not in piece.get_possible_moves(self):
            return False

        # Проверка на взятие
        is_capture = abs(from_pos[0] - to_pos[0]) == 2
        captured_piece = None
        if is_capture:
            mid_row = (from_pos[0] + to_pos[0]) // 2
            mid_col = (from_pos[1] + to_pos[1]) // 2
            captured_piece = self.board[mid_row][mid_col]
            self.board[mid_row][mid_col] = None

        # Перемещение
        self.board[to_pos[0]][to_pos[1]] = piece
        self.board[from_pos[0]][from_pos[1]] = None
        piece.position = to_pos

        # Превращение в дамку
        if isinstance(piece, Checker):
            if (piece.color == 'white' and to_pos[0] == 0) or (piece.color == 'black' and to_pos[0] == 7):
                self.board[to_pos[0]][to_pos[1]] = King(piece.color, to_pos)

        self.move_history.append((from_pos, to_pos, captured_piece, is_capture))
        return True

    def undo_move(self):
        """Откат последнего хода."""
        if not self.move_history:
            print("Нет ходов для отката.")
            return False

        from_pos, to_pos, captured_piece, is_capture = self.move_history.pop()
        piece = self.board[to_pos[0]][to_pos[1]]
        self.board[from_pos[0]][from_pos[1]] = piece
        self.board[to_pos[0]][to_pos[1]] = None
        piece.position = from_pos

        if is_capture:
            mid_row = (from_pos[0] + to_pos[0]) // 2
            mid_col = (from_pos[1] + to_pos[1]) // 2
            self.board[mid_row][mid_col] = captured_piece

        return True

    def has_moves(self, color):
        """Проверка наличия ходов у игрока."""
        for row in range(8):
            for col in range(8):
                piece = self.board[row][col]
                if piece and piece.color == color and piece.get_possible_moves(self):
                    return True
        return False

def parse_position(pos_str):
    """Преобразование строки в координаты."""
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

from checkers_board import CheckersBoard, parse_position

def main():
    board = CheckersBoard()
    turn = 'white'
    move_count = 0

    while True:
        board.display()
        print(f"Ход {move_count + 1}. Ходят {turn}.")

        if not board.has_moves(turn):
            print(f"{'Белые' if turn == 'white' else 'Черные'} не могут сделать ход. Игра окончена.")
            break

        command = input("Введите команду (например, 'move e2 e4' или 'undo'): ").strip().lower()

        if command == 'undo':
            if board.undo_move():
                turn = 'black' if turn == 'white' else 'white'
                move_count -= 1 if move_count > 0 else 0
                print("Ход успешно отменен.")
            continue

        if command.startswith('move'):
            try:
                _, from_input, to_input = command.split()
                from_pos = parse_position(from_input)
                to_pos = parse_position(to_input)
            except ValueError:
                print("Некорректный формат. Используйте 'move e2 e4'.")
                continue

            if from_pos is None or to_pos is None:
                print("Некорректная позиция.")
                continue

            piece = board.board[from_pos[0]][from_pos[1]]
            if piece is None or piece.color != turn:
                print("Неверная фигура.")
                continue

            if board.move_piece(from_pos, to_pos):
                move_count += 1
                turn = 'black' if turn == 'white' else 'white'
                print("Ход выполнен.")
            else:
                print("Недопустимый ход.")
        else:
            print("Команда неизвестна. Используйте 'move' или 'undo'.")

if __name__ == "__main__":
    main()
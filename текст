class ChessPiece:
    def __init__(self, color, position):
        self.color = color
        self.position = position
        self.symbol = ' '

    def move(self, new_position):
        # Метод для перемещения фигур
        self.position = new_position

    def can_move(self, new_position, board):
        # Проверяет, может ли фигура так ходить
        # Будет переопределен в дочерних классах
        raise NotImplementedError('Метод должен быть переопределен')

class Pawn(ChessPiece):
    def __init__(self, color, position):
        super().__init__(color, position)
        self.symbol = 'P' if color == 'white' else 'p'

    def can_move(self, new_position, board):
        """
        Проверяет, может ли пешка так ходить.
        """
        current_row, current_col = board.notation_to_position(self.position)
        new_row, new_col = board.notation_to_position(new_position)

        direction = 1 if self.color == 'white' else -1  # Направление движения пешки

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
    def __init__(self, color, position):
        super().__init__(color, position)
        self.symbol = 'R' if color == 'white' else 'r'

    def can_move(self, new_position, board):
        """
        Проверяет, может ли ладья так ходить.
        """
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
    def __init__(self, color, position):
        super().__init__(color, position)
        self.symbol = 'N' if color == 'white' else 'n'

    def can_move(self, new_position, board):
        """
        Проверяет, может ли конь так ходить.
        """
        current_row, current_col = board.notation_to_position(self.position)
        new_row, new_col = board.notation_to_position(new_position)

        row_diff = abs(new_row - current_row)
        col_diff = abs(new_col - current_col)
        return (row_diff == 2 and col_diff == 1) or (row_diff == 1 and col_diff == 2)


class Bishop(ChessPiece):
    def __init__(self, color, position):
        super().__init__(color, position)
        self.symbol = 'B' if color == 'white' else 'b'

    def can_move(self, new_position, board):
        """
        Проверяет, может ли слон так ходить.
        """
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
    def __init__(self, color, position):
        super().__init__(color, position)
        self.symbol = 'Q' if color == 'white' else 'q'

    def can_move(self, new_position, board):
        """
        Проверяет, может ли ферзь так ходить.
        """
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
    def __init__(self, color, position):
        super().__init__(color, position)
        self.symbol = 'K' if color == 'white' else 'k'

    def can_move(self, new_position, board):
        """
        Проверяет, может ли король так ходить.
        """
        current_row, current_col = board.notation_to_position(self.position)
        new_row, new_col = board.notation_to_position(new_position)

        return abs(new_row - current_row) <= 1 and abs(new_col - current_col) <= 1


class ChessBoard:
    def __init__(self):
        self.board = self.create_empty_board()
        self.setup_pieces()

    def create_empty_board(self):
        """
        Создает пустую доску 8x8.
        """
        return [[None for _ in range(8)] for _ in range(8)]

    def setup_pieces(self):
        """
        Расставляет фигуры в начальные позиции.
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
        Преобразует координаты (строка, столбец) в шахматную нотацию (например, 'a2').
        """
        return f'{chr(ord("a") + col)}{8 - row}'

    def notation_to_position(self, notation):
        """
        Преобразует шахматную нотацию (например, 'a2') в координаты (строка, столбец).
        """
        col = ord(notation[0]) - ord('a')
        row = 8 - int(notation[1])
        return row, col

    def get_piece(self, position):
        """
        Возвращает фигуру по позиции.
        """
        row, col = self.notation_to_position(position)
        return self.board[row][col]

    def move_piece(self, from_pos, to_pos):
        """
        Перемещает фигуру с одной позиции на другую.
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

class Game:
    def __init__(self):
        self.board = ChessBoard()
        self.players = [Player('white'), Player('black')]
        self.current_player = self.players[0]
        self.move_count = 0

    def start(self):
        print('Игра началась!')
        while True:
            self.print_board() # Выводим доску перед каждым ходом
            print(f'Ход игрока {self.current_player.color}')
            from_pos = input('Введите позицию фигуры (например: а2): ')
            to_pos = input('Введите, куда вы хотите сходить (например: а4): ' )

            if self.board.move_piece(from_pos, to_pos):
                print('Ход выполнен!')
                self.move_count += 1
                self.current_player = self.players[self.move_count % 2]
            else:
                print('Недопустимый ход. Попробуйте снова')

    def print_board(self):
        """
        Выводит доску в консоль.
        """
        print("  a b c d e f g h")  # Подписи столбцов
        for row in range(8):
            print(f"{8 - row} ", end="")  # Подписи строк
            for col in range(8):
                piece = self.board.board[row][col]
                print(f"{piece.symbol if piece else '.'}", end=" ")  # Символ фигуры или точка
            print(f" {8 - row}")  # Подписи строк справа
        print("  a b c d e f g h")  # Подписи столбцов снизу

class Player:
    def __init__(self, color):
        self.color = color  # 'white' или 'black'

if __name__ == "__main__":
    game = Game()
    game.start()




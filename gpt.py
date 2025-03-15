class ChessBoard:
    def __init__(self):
        self.board = self.create_empty_board()
        self.put_pieces()

    def create_empty_board(self):
        return [["--"] * 8 for _ in range(8)]

    def print_board(self):
        print(
            " " * 3 + "a" + " " * 2 + "b" + " " * 2 + "c" + " " * 2 + "d" + " " * 2 + "e" + " " * 2 + "f" + " " * 2 + "g" + " " * 2 + "h")
        for i, row in enumerate(self.board):
            print(8 - i, end="  ")
            for col in row:
                print(col, end=" ")
            print("")
        print(
            " " * 3 + "a" + " " * 2 + "b" + " " * 2 + "c" + " " * 2 + "d" + " " * 2 + "e" + " " * 2 + "f" + " " * 2 + "g" + " " * 2 + "h")

    def put_pieces(self):
        white_pieces_map = {
            "wP": [(6, 0), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5), (6, 6), (6, 7)],
            "wN": [(7, 1), (7, 6)],
            "wB": [(7, 2), (7, 5)],
            "wR": [(7, 0), (7, 7)],
            "wQ": [(7, 3)],
            "wK": [(7, 4)]
        }
        black_pieces_map = {
            "bP": [(1, 0), (1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7)],
            "bN": [(0, 1), (0, 6)],
            "bB": [(0, 2), (0, 5)],
            "bR": [(0, 0), (0, 7)],
            "bQ": [(0, 3)],
            "bK": [(0, 4)]
        }

        for piece, squares in white_pieces_map.items():
            for square in squares:
                x, y = square
                self.board[x][y] = piece

        for piece, squares in black_pieces_map.items():
            for square in squares:
                x, y = square
                self.board[x][y] = piece


class ChessGame:
    def __init__(self):
        self.board = ChessBoard()
        self.curr_turn = 1
        self.col_map = {
            "a": 0, "b": 1, "c": 2, "d": 3, "e": 4, "f": 5, "g": 6, "h": 7
        }

    def start_game(self):
        while True:
            self.board.print_board()
            print("")
            curr_player = "Белые" if self.curr_turn % 2 == 1 else "Черные"
            self.curr_turn += 1
            print(f"{curr_player} ходят!")
            print("")

            starting_square = input("Напишите, какой фигурой вы собираетесь ходить (например, a2): ")
            start_x, start_y = starting_square[0], starting_square[1]
            start_x = self.col_map[start_x]
            start_y = 8 - int(start_y)
            start_x, start_y = start_y, start_x  # Переворачиваем координаты

            ending_square = input("Введите поле, на которое вы хотите передвинуть фигуру (например, a4): ")
            end_x, end_y = ending_square[0], ending_square[1]
            end_x = self.col_map[end_x]
            end_y = 8 - int(end_y)
            end_x, end_y = end_y, end_x  # Переворачиваем координаты

            self.move_piece(start_x, start_y, end_x, end_y)

    def move_piece(self, start_x, start_y, end_x, end_y):
        piece = self.board.board[start_x][start_y]
        if piece == "--":
            print("Нет фигуры на выбранной клетке.")
            return

        # Выполняем ход, просто перемещаем фигуру
        self.board.board[start_x][start_y] = "--"
        self.board.board[end_x][end_y] = piece
        print(f"Фигура {piece} перемещена на {chr(end_y + 97)}{8 - end_x}")


# Запуск игры
if __name__ == "__main__":
    game = ChessGame()
    game.start_game()

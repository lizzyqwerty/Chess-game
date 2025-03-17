"""
Модуль main.py

Точка входа в программу. Запускает игру.
"""
from chess_board import ChessBoard, parse_position

def main():
    main_board = ChessBoard()
    turn = 'white'
    move_count = 0

    while True:
        main_board.display()
        print(f"Ход {move_count + 1}. Ходят {turn}.")
        if main_board.is_in_check(turn):
            print(f"{'Белые' if turn == 'white' else 'Черные'} под шахом!")

        command = input("Введите команду (например, 'move e2 e4' или 'undo'): ").strip().lower()

        if command == 'undo':
            if main_board.undo_move():
                turn = 'black' if turn == 'white' else 'white'  # Смена хода
                move_count -= 1 if move_count > 0 else 0
                print("Ход успешно отменен.")
            continue

        if command.startswith('move'):
            try:
                _, from_input, to_input = command.split()
                from_pos = parse_position(from_input)
                to_pos = parse_position(to_input)
            except ValueError:
                print("Некорректный формат команды. Используйте 'move e2 e4'.")
                continue

            if from_pos is None or to_pos is None:
                print("Некорректный ввод позиции. Попробуйте еще раз.")
                continue

            piece = main_board.board[from_pos[0]][from_pos[1]]
            if piece is None or piece.color != turn:
                print("Выбрана неверная или отсутствующая фигура. Попробуйте еще раз.")
                continue

            # Выполнение хода
            if main_board.move_piece(from_pos, to_pos):
                move_count += 1
                turn = 'black' if turn == 'white' else 'white'
                print("Ход успешно выполнен.")
            else:
                print("Недопустимый ход (возможно, король под шахом). Попробуйте еще раз.")
        else:
            print("Неизвестная команда. Используйте 'move' или 'undo'.")


if __name__ == "__main__":
    main()
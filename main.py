"""
Модуль main.py

Точка входа в программу. Запускает игру.
"""
from chess_board import ChessBoard, CheckersBoard, parse_position


def main():
    print("Выберите игру: 1 - Шахматы, 2 - Шашки")
    choice = input("Введите 1 или 2: ").strip()

    if choice == '1':
        board = ChessBoard()
        game_type = 'chess'
    elif choice == '2':
        board = CheckersBoard()
        game_type = 'checkers'
    else:
        print("Некорректный выбор. Завершение программы.")
        return

    turn = 'white'
    move_count = 0

    while True:
        board.display()
        print(f"Ход {move_count + 1}. Ходят {turn}.")

        if game_type == 'chess' and board.is_in_check(turn):
            print(f"{'Белые' if turn == 'white' else 'Черные'} под шахом!")

        if game_type == 'checkers' and board.is_game_over():
            winner = 'Черные' if turn == 'white' else 'Белые'
            print(f"Игра окончена. {winner} победили!")
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
                print("Некорректный формат команды. Используйте 'move e2 e4'.")
                continue

            if from_pos is None or to_pos is None:
                print("Некорректный ввод позиции. Попробуйте еще раз.")
                continue

            piece = board.board[from_pos[0]][from_pos[1]]
            if piece is None or piece.color != turn:
                print("Выбрана неверная или отсутствующая фигура. Попробуйте еще раз.")
                continue

            # Проверка обязательных прыжков
            if game_type == 'checkers':
                if board.has_mandatory_jump(turn):
                    if abs(from_pos[0] - to_pos[0]) != 2:
                        print("Обязательный прыжок доступен. Вы должны сделать прыжок.")
                        continue

            if board.move_piece(from_pos, to_pos):
                move_count += 1
                turn = 'black' if turn == 'white' else 'white'
                print("Ход успешно выполнен.")
            else:
                print("Недопустимый ход. Попробуйте еще раз.")
        else:
            print("Неизвестная команда. Используйте 'move' или 'undo'.")


if __name__ == "__main__":
    main()
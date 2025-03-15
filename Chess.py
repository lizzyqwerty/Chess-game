class Game:
    def __init__(self, n, a, b, c, d):
        self.n = n
        self.a = a  # Буква 1
        self.b = b  # Номер 1
        self.c = c  # Буква 2
        self.d = d  # Номер 3
        self.board()

    def board(self):
        if self.n == 0:
            game_board = [[' '], ['A'], ['B'], ['C'], ['D'], ['E'], ['F'], ['G'], ['H'], [' '],
                          [8], ['r'], ['n'], ['b'], ['q'], ['k'], ['b'], ['n'], ['r'], [8],
                          [7], ['p'], ['p'], ['p'], ['p'], ['p'], ['p'], ['p'], ['p'], [7],
                          [6], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], [6],
                          [5], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], [5],
                          [4], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], [4],
                          [3], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], ['.'], [3],
                          [2], ['P'], ['P'], ['P'], ['P'], ['P'], ['P'], ['P'], ['P'], [2],
                          [1], ['R'], ['N'], ['B'], ['Q'], ['K'], ['B'], ['N'], ['R'], [1],
                          [' '], ['A'], ['B'], ['C'], ['D'], ['E'], ['F'], ['G'], ['H'], [' ']

                          ]
            f = 10
            s = 0
            for j in range(10):
                line = ' '.join(str(item[0]) for item in game_board[s:f])
                print(line)
                f += 10
                s += 10
            return game_board

    info_figures = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8}



class Pawn(Game):
    def step_by_pawn(self):
        if self.b == self.c and self.a - self.c == 1:
            print('sss')


class King(Game):
    def step_by_king(self):
        if self.a == self.c and self.b - self.d == +-1:
            print('da')
        if self.a - self.c == +-1 and (self.b == self.d or self.b - self.d == +-1):
            print('make a step')


class Bishop(Game):
    def step_by_bishop(self):

        if ((self.a + self.b) % 2 == 0 and (self.c + self.d) % 2 == 0) and (self.a + self.b) == (self.c + self.d):
            print("YES")
            # черные по правой диагонали
        elif ((self.a + self.b) % 2 == 0 and (self.c + self.d) % 2 == 0) and (self.a - self.c) == (self.b - self.d):
            print("YES")
            # white
        elif ((self.a + self.b) % 2 == 1 and (self.c + self.d) % 2 == 1) and (self.a + self.b) == (self.c + self.d):
            print("YES")
        elif ((self.a + self.b) % 2 == 1 and (self.c + self.d) % 2 == 1) and (self.a - self.c) == (self.b - self.d):
            print("YES")
        else:
            print("NO")


class Rook(Game):
    def step_by_rook(self):
        ...
class Knight(Game):
    def step_by_knight(self):
        if (self.a == self.c + 1 or self.a == self.c - 1) and (self.b == self.d + 2 or self.b == self.d - 2):
            print("YES")
        elif (self.a == self.c + 2 or self.a == self.c - 2) and (self.b == self.d + 1 or self.b == self.d - 1):
            print("YES")

        else:
            print("NO")

a = Game(0, 8, 5, 7, 5)

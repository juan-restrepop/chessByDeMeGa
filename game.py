class Pawn(object):
    kind = 'p'
    coordinate = list()

    def __init__(self, color, coordinates):
        self.initialize_pawn(color, coordinates)

    def initialize_pawn(self, color, coordinates):
        self.color = color
        self.coordinates = coordinates

class Game(object):
    grid = list()
    pawns = list()

    def __init__(self):
        self.initialize_board()
        self.initialize_pieces()
        self.initialize_board_with_pieces()

    def initialize_board_with_pieces(self):
        for k in range(len(self.pawns)):
            rowCoord = self.pawns[k].coordinates[0]
            colCoord = self.pawns[k].coordinates[1]
            self.grid[rowCoord][colCoord] = self.pawns[k].kind

    def initialize_pieces(self):
        for k in range(8):
            self.pawns.append(Pawn('w', [1, k]))


    def initialize_board(self):
        for i in range(0,8):
            self.grid.append(list())

            for j in range(0, 8):
                self.grid[i].append(str((j + i) % 2))

    def print_board(self):

        board_string = ''
        for i in range(0, 8):
            for j in range(0, 8):
                board_string = board_string + ' ' + self.grid[i][j]

            board_string = board_string + '\n'

        print board_string

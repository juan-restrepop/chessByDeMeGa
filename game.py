import pieces

class Pawn(pieces.Piece):
    def __init__(self, color, coordinates):
        pieces.Piece.__init__(self, 'p', color, coordinates)

class Game(object):
    grid = list()
    pawns_w = list()
    pawns_b = list()

    def __init__(self):
        self.initialize_board()
        self.initialize_pieces()
        self.initialize_board_with_pieces()

    def initialize_board_with_pieces(self):
        for p in (self.pawns_w + self.pawns_b):
            rowCoord = p.coordinates[0]
            colCoord = p.coordinates[1]
            self.grid[rowCoord][colCoord] = p.kind

    def initialize_pieces(self):
        for k in range(8):
            self.pawns_w.append(Pawn('w', [1, k]))
            self.pawns_b.append(Pawn('b', [6, k]))


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

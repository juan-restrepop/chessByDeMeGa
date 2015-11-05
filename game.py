import pieces

class Pawn(pieces.Piece):
    def __init__(self, color, coordinates):
        pieces.Piece.__init__(self, 'p', color, coordinates)

class Queen(pieces.Piece):
    def __init__(self, color, coordinates):
        pieces.Piece.__init__(self, 'q', color, coordinates)

class King(pieces.Piece):
    def __init__(self, color, coordinates):
        pieces.Piece.__init__(self, 'k', color, coordinates)

class Game(object):
    grid = list()
    pawns_w = list()
    pawns_b = list()

    king_w = list()
    king_b = list()

    queen_w = list()
    queen_b = list()

    def __init__(self):
        self.initialize_board()
        self.initialize_pieces()
        self.initialize_board_with_pieces()

    def initialize_board_with_pieces(self):
        all_pieces = self.pawns_w + self.pawns_b + self.king_w + self.king_b + self.queen_w + self.queen_b
        for p in all_pieces:
            rowCoord = p.coordinates[0]
            colCoord = p.coordinates[1]
            self.grid[rowCoord][colCoord] = p.kind

    def initialize_pieces(self):
        for k in range(8):
            self.pawns_w.append(Pawn('w', [1, k]))
            self.pawns_b.append(Pawn('b', [6, k]))

        self.king_b.append(King('b', [7, 4]))
        self.king_w.append(King('w', [0, 4]))

        self.queen_b.append(Queen('b', [7, 3]))
        self.queen_w.append(Queen('w', [0, 3]))


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

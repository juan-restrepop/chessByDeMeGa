import pieces

class Pawn(pieces.Piece):
    def __init__(self, color, coordinates):
        pieces.Piece.__init__(self, 'p', color, coordinates)

class Rook(pieces.Piece):
    def __init__(self, color, coordinates):
        pieces.Piece.__init__(self, 'r', color, coordinates)

class Bishop(pieces.Piece):
    def __init__(self, color, coordinates):
        pieces.Piece.__init__(self, 'b', color, coordinates)

class Knight(pieces.Piece):
    def __init__(self, color, coordinates):
        pieces.Piece.__init__(self, 'n', color, coordinates)


class Game(object):
    grid = list()
    pawns_w = list()
    pawns_b = list()
    rooks_w = list()
    rooks_b = list()
    bishops_w = list()
    bishops_b = list()
    knights_w = list()
    knights_b = list()

    def __init__(self):
        self.initialize_board()
        self.initialize_pieces()
        self.initialize_board_with_pieces()

    def initialize_board_with_pieces(self):
        for p in (self.pawns_w + self.pawns_b
                + self.rooks_w + self.rooks_b
                + self.bishops_w + self.bishops_b
                + self.knights_w + self.knights_b):
            rowCoord = p.coordinates[0]
            colCoord = p.coordinates[1]
            self.grid[rowCoord][colCoord] = p.kind

    def initialize_pieces(self):
        for k in range(8):
            self.pawns_w.append(Pawn('w', [1, k]))
            self.pawns_b.append(Pawn('b', [6, k]))
           
        self.rooks_w.append(Rook('w',[0,0]))
        self.rooks_w.append(Rook('w',[0,7]))
        
        self.bishops_w.append(Bishop('w',[0,2]))
        self.bishops_w.append(Bishop('w',[0,5]))

        self.knights_w.append(Knight('w',[0,1]))
        self.knights_w.append(Knight('w',[0,6]))
        
        self.rooks_b.append(Rook('b',[7,0]))
        self.rooks_b.append(Rook('b',[7,7]))
        
        self.bishops_b.append(Bishop('b',[7,2]))
        self.bishops_b.append(Bishop('b',[7,5]))

        self.knights_b.append(Knight('b',[7,1]))
        self.knights_b.append(Knight('b',[7,6]))



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

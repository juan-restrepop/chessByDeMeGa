import pieces

class ChessBoard(object):
    grid = list()
    pawns_w = list()
    pawns_b = list()
    rooks_w = list()
    rooks_b = list()
    bishops_w = list()
    bishops_b = list()
    knights_w = list()
    knights_b = list()
    king_w = list()
    king_b = list()
    queen_w = list()
    queen_b = list()

    def __init__(self):
        self.initialize_board()
        self.initialize_pieces()
        self.initialize_board_with_pieces()

    def get_all_pieces(self):
        return(self.pawns_w + self.pawns_b + \
                     self.king_w + self.king_b + \
                     self.queen_w + self.queen_b + \
                     self.rooks_w + self.rooks_b + \
                     self.bishops_w + self.bishops_b + \
                     self.knights_w + self.knights_b)

    def initialize_board_with_pieces(self):

        for p in self.get_all_pieces():
            rowCoord = p.coordinates[0]
            colCoord = p.coordinates[1]
            self.grid[rowCoord][colCoord] = p.kind

    def initialize_pieces(self):
        for k in range(8):
            self.pawns_w.append(pieces.Pawn('w', [1, k]))
            self.pawns_b.append(pieces.Pawn('b', [6, k]))
           
        self.rooks_w.append(pieces.Rook('w',[0,0]))
        self.rooks_w.append(pieces.Rook('w',[0,7]))
        
        self.bishops_w.append(pieces.Bishop('w',[0,2]))
        self.bishops_w.append(pieces.Bishop('w',[0,5]))

        self.knights_w.append(pieces.Knight('w',[0,1]))
        self.knights_w.append(pieces.Knight('w',[0,6]))
        
        self.rooks_b.append(pieces.Rook('b',[7,0]))
        self.rooks_b.append(pieces.Rook('b',[7,7]))
        
        self.bishops_b.append(pieces.Bishop('b',[7,2]))
        self.bishops_b.append(pieces.Bishop('b',[7,5]))

        self.knights_b.append(pieces.Knight('b',[7,1]))
        self.knights_b.append(pieces.Knight('b',[7,6]))


        self.king_b.append(pieces.King('b', [7, 4]))
        self.king_w.append(pieces.King('w', [0, 4]))

        self.queen_b.append(pieces.Queen('b', [7, 3]))
        self.queen_w.append(pieces.Queen('w', [0, 3]))


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
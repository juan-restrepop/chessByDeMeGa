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

    def get_bishop_walk_color(self,some_bishop):
        return self.get_square_color(some_bishop.coordinates[0],
                                     some_bishop.coordinates[1])

    def get_square_color(self,i,j):
        return ((j + i) % 2)

    def initialize_board(self):
        self.grid = list()
        for i in range(0,8):
            self.grid.append(list())
            for j in range(0, 8):
                self.grid[i].append(str((j + i) % 2))

    def update_board(self):
        self.initialize_board()
        self.initialize_board_with_pieces()

    def print_board(self):
        board_string = ''
        board_string = board_string + '    a b c d e f g h \n'
        board_string = board_string + '    _______________ \n'
        for i in range(0, 8):
            board_string = board_string + ' ' + str(i+1) + '|'
            for j in range(0, 8):
                board_string = board_string + ' ' + self.grid[i][j] 
            board_string = board_string + ' | ' + str(i+1) + ' '
            if i == 1:
                board_string = board_string + '  <- White pawns line'
            if i == 6:
                board_string = board_string + '  <- Black pawns line'
            board_string = board_string + '\n'
        board_string = board_string + '    _______________ \n'
        board_string = board_string + '    a b c d e f g h \n'
        print board_string

    def can_pawn_reach(self, i, j, pawn):

        i_origin, j_origin = pawn.coordinates
        if j == j_origin:
            return True

    def move_pawn_to(self, col, line):
        # we work only with white
        # TODO: Handle updates and initialization of board and grid.
        # TODO: Handle difference between empty_board and grid?

        i, j = self.coord_board_to_coord_grid(col, line)

        for k in range(len(self.pawns_w)):
            if self.can_pawn_reach(i, j, self.pawns_w[k]):
                self.pawns_w[k].coordinates[0] = i
                break
        self.update_board()
        return


    def move_bishop_to(self, col, line):
        # we work only with white
        i,j  = self.coord_board_to_coord_grid(col,line)
        square_color = str(self.get_square_color(i,j))
        
        for k in range(len(self.bishops_w)):
            # if square_color == str(self.get_bishop_walk_color(self.bishops_w[k])):
            #     self.bishops_w[k].coordinates = [i,j]
            if abs(i - self.bishops_w[k].coordinates[0]) == abs(j - self.bishops_w[k].coordinates[1]):
                self.bishops_w[k].coordinates = [i,j]
                break
        self.update_board()
        return

    def move_knight_to(self, col, line):
        # we work only with white
        i,j = self.coord_board_to_coord_grid(col, line)

        for k in range(len(self.knights_w)):
            i_origin, j_origin = self.knights_w[k].coordinates
            if (abs(i - i_origin) == 1) and (abs(j - j_origin) == 2) \
                or \
                (abs(i - i_origin) == 2) and (abs(j - j_origin) == 1):
                self.knights_w[k].coordinates = [i,j]
                break
        self.update_board()
        return

    def move_rook_to(self, col, line):
        # we work only with white
        i,j  = self.coord_board_to_coord_grid(col,line)

        for k in range(len(self.rooks_w)):

            if (i == self.rooks_w[k].coordinates[0]) or (j == self.rooks_w[k].coordinates[1]):
                self.rooks_w[k].coordinates = [i,j]
                break
        self.update_board()
        return

    def move_king_to(self, col, line):
        # we work only with white
        i,j = self.coord_board_to_coord_grid(col,line)

        i_origin, j_origin = self.king_w[0].coordinates

        if ((abs(i - i_origin) == 1) and (abs(j - j_origin) <= 1) 
            or (abs(j - j_origin) == 1) and (abs(i - i_origin) <= 1)):
            self.king_w[0].coordinates = [i,j]

        self.update_board()
        return

    def move_queen_to(self, col, line):
        #we work only with white
        i,j = self.coord_board_to_coord_grid(col, line)

        for k in range(len(self.queen_w)):
            i_origin, j_origin = self.queen_w[k].coordinates
            if ((i == i_origin) or (j == j_origin)) or (abs(i - i_origin) == abs(j - j_origin)):
                self.queen_w[k].coordinates = [i,j]
                break

        self.update_board()
        return

    def coord_board_to_coord_grid(self,col,line):
        columns_to_grid = {'a': 0,
                           'b': 1,
                           'c': 2,
                           'd': 3,
                           'e': 4,
                           'f': 5,
                           'g': 6,
                           'h': 7}
        return (int(line)-1 ,columns_to_grid[col])



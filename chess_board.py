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


    def initialize_board(self):
        self.grid = list()
        for i in range(0,8):
            self.grid.append(list())
            for j in range(0, 8):
                self.grid[i].append(str((j + i) % 2))

    def clean_pieces(self):
        self.pawns_w = list()
        self.pawns_b = list()
        self.rooks_w = list()
        self.rooks_b = list()
        self.bishops_w = list()
        self.bishops_b = list()
        self.knights_w = list()
        self.knights_b = list()
        self.king_w = list()
        self.king_b = list()
        self.queen_w = list()
        self.queen_b = list()

        self.update_board()

    def initialize_single_piece(self, kind, color, coordinates):
        dic_piece_to_piece_lists = {'wp': self.pawns_w,
                                    'bp': self.pawns_b,
                                    'wr': self.rooks_w,
                                    'br': self.rooks_b,
                                    'wb': self.bishops_w,
                                    'bb': self.bishops_b,
                                    'wn': self.knights_w,
                                    'bn': self.knights_b,
                                    'wq': self.queen_w,
                                    'bq': self.queen_b,
                                    'wk': self.king_w,
                                    'bk': self.king_b}
        if not(\
                        kind in ['p', 'k', 'q', 'b', 'r', 'n'] and \
                        color in ['w', 'b'] and \
                        coordinates[0] in range(8) and \
                        coordinates[1] in range(8)\

                  ):
            print 'That piece or that board coordinate is not valid'

        else:
            if kind == 'p':
                dic_piece_to_piece_lists[color + kind].append(pieces.Pawn(color, coordinates))
            elif kind == 'r':
                dic_piece_to_piece_lists[color + kind].append(pieces.Rook(color, coordinates))
            elif kind == 'n':
                dic_piece_to_piece_lists[color + kind].append(pieces.Knight(color, coordinates))
            elif kind == 'b':
                dic_piece_to_piece_lists[color + kind].append(pieces.Bishop(color, coordinates))
            elif kind == 'q':
                dic_piece_to_piece_lists[color + kind].append(pieces.Queen(color, coordinates))
            elif kind == 'k':
                dic_piece_to_piece_lists[color + kind].append(pieces.King(color, coordinates))

        self.update_board()

    def initialize_pieces(self):
        self.clean_pieces()

        for k in range(8):
            self.pawns_w.append(pieces.Pawn('w', [6, k]))
            self.pawns_b.append(pieces.Pawn('b', [1, k]))
           
        self.rooks_w.append(pieces.Rook('w',[7,0]))
        self.rooks_w.append(pieces.Rook('w',[7,7]))
        
        self.bishops_w.append(pieces.Bishop('w',[7,2]))
        self.bishops_w.append(pieces.Bishop('w',[7,5]))

        self.knights_w.append(pieces.Knight('w',[7,1]))
        self.knights_w.append(pieces.Knight('w',[7,6]))
        
        self.rooks_b.append(pieces.Rook('b',[0,0]))
        self.rooks_b.append(pieces.Rook('b',[0,7]))
        
        self.bishops_b.append(pieces.Bishop('b',[0,2]))
        self.bishops_b.append(pieces.Bishop('b',[0,5]))

        self.knights_b.append(pieces.Knight('b',[0,1]))
        self.knights_b.append(pieces.Knight('b',[0,6]))

        self.king_b.append(pieces.King('b', [0, 4]))
        self.king_w.append(pieces.King('w', [7, 4]))

        self.queen_b.append(pieces.Queen('b', [0, 3]))
        self.queen_w.append(pieces.Queen('w', [7, 3]))

    def initialize_board_with_pieces(self):
        for p in self.get_all_pieces():
            rowCoord = p.coordinates[0]
            colCoord = p.coordinates[1]
            self.grid[rowCoord][colCoord] = p.kind


    def get_bishop_walk_color(self,some_bishop):
        return self.get_square_color(some_bishop.coordinates[0],
                                     some_bishop.coordinates[1])

    def get_square_color(self,i,j):
        return ((j + i) % 2)


    def update_board(self):
        self.initialize_board()
        self.initialize_board_with_pieces()

    def print_board(self):
        board_string = ''
        board_string = board_string + '    a b c d e f g h \n'
        board_string = board_string + '    _______________ \n'
        for i in range(0, 8):
            board_string = board_string + ' ' + str(8- i) + '|'
            for j in range(0, 8):
                board_string = board_string + ' ' + self.grid[i][j] 
            board_string = board_string + ' | ' + str(8 - i) + ' '
            if i == 1:
                board_string = board_string + '  <- Black pawns line'
            if i == 6:
                board_string = board_string + '  <- White pawns line'
            board_string = board_string + '\n'
        board_string = board_string + '    _______________ \n'
        board_string = board_string + '    a b c d e f g h \n'
        print board_string


    def is_square_free(self, i, j):
        return self.grid[i][j] in ['0', '1']


    def can_pawn_reach(self, i, j, pawn):
        # TODO: should work for black pawns as well

        i_origin, j_origin = pawn.coordinates

        if j == j_origin:
            if i >= i_origin:
                return False
            elif i_origin - i == 1:
                return self.is_square_free(i,j)
            elif i_origin - i == 2:
                return self.is_square_free(i+1,j) and self.is_square_free(i,j) and i_origin == 6
            else:
                return False
        else:
            return False

    def can_king_reach(self, i, j, king):
        i_origin, j_origin = king.coordinates

        if ((abs(i - i_origin) == 1) and (abs(j - j_origin) <= 1) 
            or (abs(j - j_origin) == 1) and (abs(i - i_origin) <= 1)):
            return self.is_square_free(i,j)
        return False

    def can_queen_reach(self, i, j, queen):
        return self.can_bishop_reach(i, j, queen) or self.can_rook_reach(i, j, queen)

    def can_rook_reach(self, i, j, rook):
        # TODO: The rook should eat if final square is occupied
        # TODO: Requesting to leave the piece in place should not be considered a valid move
        i_origin, j_origin = rook.coordinates

        free_path = True
        if (i == i_origin):

            if j > j_origin:
                # rook moves to the right
                temp_j = j_origin + 1
                while free_path and (temp_j <= j):
                    free_path = self.is_square_free(i, temp_j)
                    temp_j = temp_j + 1

            elif j < j_origin:
                # rook moves to the left
                temp_j = j_origin - 1
                while free_path and (temp_j >= j):
                    free_path = self.is_square_free(i, temp_j)
                    temp_j = temp_j - 1

        elif (j == j_origin):

            if i > i_origin:
                # rook moves down
                temp_i = i_origin + 1
                while free_path and (temp_i <= i):
                    free_path = self.is_square_free(temp_i, j)
                    temp_i = temp_i + 1

            elif i < i_origin:
                # rook moves up
                temp_i = i_origin - 1
                while free_path and (temp_i >= i):
                    free_path = self.is_square_free(temp_i, j)
                    temp_i = temp_i - 1
        else:
            return False

        return free_path # to liberty

    def can_bishop_reach(self, i, j, bishop):
        # TODO: The bishop should stop (or eat) if it encounters a piece on its path
        i_origin, j_origin = bishop.coordinates

        if abs(i - i_origin) == abs(j - j_origin):
            free_path = True

            if (i > i_origin) and (j > j_origin):
                # move down and to the right
                temp_i = i_origin + 1
                temp_j = j_origin + 1
                while free_path and (temp_i <= i):
                    free_path = self.is_square_free(temp_i, temp_j)
                    temp_i = temp_i + 1
                    temp_j = temp_j + 1

            elif (i > i_origin) and (j < j_origin):
                # move down and to the left
                temp_i = i_origin + 1
                temp_j = j_origin - 1
                while free_path and (temp_i <= i):
                    free_path = self.is_square_free(temp_i, temp_j)
                    temp_i = temp_i + 1
                    temp_j = temp_j - 1

            elif (i < i_origin) and (j < j_origin):
                # move up and to the left
                temp_i = i_origin - 1
                temp_j = j_origin - 1
                while free_path and (temp_i >= i):
                    free_path = self.is_square_free(temp_i, temp_j)
                    temp_i = temp_i - 1
                    temp_j = temp_j - 1

            elif (i < i_origin) and (j > j_origin):
                # move up and to the right
                temp_i = i_origin - 1
                temp_j = j_origin + 1
                while free_path and (temp_i >= i):
                    free_path = self.is_square_free(temp_i, temp_j)
                    temp_i = temp_i - 1
                    temp_j = temp_j + 1 
        
            return free_path
                
        return False                                                                                

    def can_knight_reach(self, i, j, knight):
        # TODO: The knight should eat if final square is occupied
        i_origin, j_origin = knight.coordinates

        if self.is_square_free(i, j):
            return (abs(i - i_origin) == 1) and (abs(j - j_origin) == 2) \
                or \
                (abs(i - i_origin) == 2) and (abs(j - j_origin) == 1)

        return False

    def piece_mover(self, piece, i, j):
        piece.coordinates = [i, j]
        self.update_board()

    def list_to_update(self, player):
        if player == 'white':
            return self.pawns_w
        elif player == 'black':
            return self.pawns_b
        else:
            return None


    def move_pawn_to(self, col, line, player='white'):
        # we work only with white
        # TODO: Handle 'en passant' capture

        accepted_move = False
        i, j = self.transform_board_to_grid(col, line)
        pawn_list = self.list_to_update(player)

        for k in range(len(pawn_list)):
            if self.can_pawn_reach(i, j, pawn_list[k]):
                self.piece_mover(pawn_list[k], i, j)
                accepted_move = True
                break

        return accepted_move

    def move_bishop_to(self, col, line):
        # we work only with white

        accepted_move = False
        i,j  = self.transform_board_to_grid(col,line)
        
        for k in range(len(self.bishops_w)):
            if self.can_bishop_reach(i, j, self.bishops_w[k]):
                self.piece_mover(self.bishops_w[k], i, j)
                accepted_move = True
                break

        return accepted_move

    def move_knight_to(self, col, line):
        # we work only with white

        accepted_move = False
        i,j = self.transform_board_to_grid(col, line)

        for k in range(len(self.knights_w)):
            if self.can_knight_reach(i, j, self.knights_w[k]):
                self.piece_mover(self.knights_w[k], i, j)
                accepted_move = True
                break

        return accepted_move

    def move_rook_to(self, col, line):
        # we work only with white

        accepted_move = False
        i,j  = self.transform_board_to_grid(col,line)

        for k in range(len(self.rooks_w)):
            if self.can_rook_reach(i, j, self.rooks_w[k]):
                self.piece_mover(self.rooks_w[k], i, j)
                accepted_move = True
                break

        return accepted_move

    def move_king_to(self, col, line):
        # we work only with white
        accepted_move = False
        i,j = self.transform_board_to_grid(col,line)

        if self.can_king_reach(i, j, self.king_w[0]):
            self.piece_mover(self.king_w[0], i, j)
            accepted_move = True

        return accepted_move

    def move_queen_to(self, col, line):
        #we work only with white

        accepted_move = False
        i,j = self.transform_board_to_grid(col, line)

        for k in range(len(self.queen_w)):
            if self.can_queen_reach(i, j, self.queen_w[k]):
                self.piece_mover(self.queen_w[k], i, j)
                accepted_move = True
                break

        return accepted_move


    def transform_board_to_grid(self,col,line):
        columns_to_grid = {'a': 0,
                           'b': 1,
                           'c': 2,
                           'd': 3,
                           'e': 4,
                           'f': 5,
                           'g': 6,
                           'h': 7}

        lines_to_grid = {'8': 0,
                         '7': 1,
                         '6': 2,
                         '5': 3,
                         '4': 4,
                         '3': 5,
                         '2': 6,
                         '1': 7}
        return [lines_to_grid[line] ,columns_to_grid[col]]

    def transform_grid_to_board(self, i, j):
        grid_lines_to_board_lines = {0 : '8',
                                      1 : '7',
                                      2 : '6',
                                      3 : '5',
                                      4 : '4',
                                      5 : '3',
                                      6 : '2',
                                      7 : '1'}

        grid_columns_to_board_columns = {0 : 'a',
                                         1 : 'b',
                                         2 : 'c',
                                         3 : 'd',
                                         4 : 'e',
                                         5 : 'f',
                                         6 : 'g',
                                         7 : 'h'}

        return (grid_columns_to_board_columns[j], grid_lines_to_board_lines[i])

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
        self.Rules = MovementRules()


    def get_all_pieces(self):
        return(self.pawns_w + self.pawns_b + \
                     self.king_w + self.king_b + \
                     self.queen_w + self.queen_b + \
                     self.rooks_w + self.rooks_b + \
                     self.bishops_w + self.bishops_b + \
                     self.knights_w + self.knights_b)

    def get_all_black_pieces(self):
        return (self.pawns_b + self.knights_b + self.bishops_b + self.rooks_b + self.queen_b + self.king_w)

    def get_all_white_pieces(self):
        return (self.pawns_w + self.knights_w + self.bishops_w + self.rooks_w + self.queen_w + self.king_w)

    def get_piece_in_square(self, i, j):
        for piece in self.get_all_pieces():
            if piece.coordinates == [i, j]:
                return piece
        return []

    def get_piece_coords(self, piece):
        i, j = piece.coordinates
        col, line = self.transform_grid_to_board(i, j)
        return col, line

    def initialize_board(self):
        self.grid = list()
        for i in range(0,8):
            self.grid.append(list())
            for j in range(0, 8):
                self.grid[i].append(str((j + i) % 2))

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

        # Check function input
        if not(kind in ['p', 'k', 'q', 'b', 'r', 'n']):
            print 'Cannot initialize piece, invalid kind'
            return
        elif not(color in ['w', 'b']):
            print 'Cannot initialize piece, invalid color'
            return
        elif not( (coordinates[0] in range(8)) and (coordinates[1] in range(8)) ):
            print 'Cannot initialize piece, invalid coordinate' \
                  'return'

        # Check if square is available
        if not(self.is_square_free(coordinates[0], coordinates[1])):
            print 'Cannot initialize piece, occupied square'
            return

        #Initialize the piece
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

    def piece_mover(self, kind, col, line, player):
        move_rule_function = getattr(self.Rules, self.map_piece_to_moving(kind)[0])
        white_pieces = getattr(self, self.map_piece_to_moving(kind)[1])
        black_pieces = getattr(self, self.map_piece_to_moving(kind)[2])

        i, j = self.transform_board_to_grid(col, line)
        pieces_to_move = self.list_to_update(player, white_pieces, black_pieces)

        accepted_move = False
        for k in range(len(pieces_to_move)):
            piece = pieces_to_move[k]
            if move_rule_function(self, i, j, piece, player):
                pieces_to_move[k].coordinates = [i, j]
                accepted_move = True
                self.update_board()
                break

        return accepted_move

    def list_to_update(self, player, list_w, list_b):
        if player == 'white':
            return list_w
        elif player == 'black':
            return list_b
        else:
            return None


    def map_piece_to_eating(self,kind):

        map_piece_2_eat = { 'k':'is_king_eating_valid',
                                'b':'is_bishop_eating_valid',
                                'n':'is_knight_eating_valid',
                                'r':'is_rook_eating_valid',
                                'p':'is_pawn_eating_valid',
                                'q':'is_queen_eating_valid' }

        return map_piece_2_eat.get(kind)

    def map_piece_to_moving(self, kind):
        map_piece_2_move = {'k': ['is_king_movement_valid', 'king_w', 'king_b'],
                            'q': ['is_queen_movement_valid', 'queen_w', 'queen_b'],
                            'b': ['is_bishop_movement_valid', 'bishops_w', 'bishops_b'],
                            'n': ['is_knight_movement_valid', 'knights_w', 'knights_b'],
                            'r': ['is_rook_movement_valid', 'rooks_w', 'rooks_b'],
                            'p': ['is_pawn_movement_valid', 'pawns_w', 'pawns_b']}

        return map_piece_2_move[kind]





    def move_pawn_to(self, col, line, player='white'):
        return self.piece_mover('p', col, line, player)

    def move_bishop_to(self, col, line, player='white'):
        return self.piece_mover('b', col, line, player)

    def move_knight_to(self, col, line, player='white'):
        return self.piece_mover('n', col, line, player)

    def move_rook_to(self, col, line, player='white'):
        return self.piece_mover('r', col, line, player)

    def move_king_to(self, col, line, player='white'):
        return self.piece_mover('k', col, line, player)

    def move_queen_to(self, col, line, player = 'white'):
        return self.piece_mover('q', col, line, player)
        

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

class MovementRules(object):

    def is_lateral_move_valid(self, board,  i_origin, j_origin, i_end, j_end):
        free_path = True
        if j_end > j_origin: # movement to the right
            temp_j = j_origin + 1
            while free_path and (temp_j <=j_end):
                free_path = board.is_square_free(i_origin, temp_j)
                temp_j += 1
        elif j_end < j_origin: # movement to the left
            temp_j = j_origin - 1
            while free_path and (temp_j >= j_end):
                free_path = board.is_square_free(i_origin, temp_j)
                temp_j -= 1
        else:
            return False
        return free_path# to liberty

    def is_vertical_move_valid(self, board, i_origin, j_origin, i_end, j_end):
        free_path = True
        if i_end > i_origin:# movement down
            temp_i = i_origin + 1
            while free_path and (temp_i <= i_end):
                free_path = board.is_square_free(temp_i, j_origin)
                temp_i += 1
        elif i_end < i_origin:# movement up
            temp_i = i_origin - 1
            while free_path and (temp_i >= i_end):
                free_path = board.is_square_free(temp_i, j_origin)
                temp_i -= 1
        else:
            return False
        return free_path# to liberty

    def is_diagonal_move_valid(self, board, i_origin, j_origin, i_end, j_end):
        if abs(i_end - i_origin) and (j_end - j_origin):
            free_path = True

            if (i_end > i_origin) and (j_end > j_origin):# move down and to the right
                temp_i = i_origin + 1
                temp_j = j_origin + 1
                while free_path and (temp_i <= i_end):
                    free_path = board.is_square_free(temp_i, temp_j)
                    temp_i += 1
                    temp_j += 1

            elif (i_end > i_origin) and (j_end < j_origin):# move down and to the left
                temp_i = i_origin + 1
                temp_j = j_origin - 1
                while free_path and (temp_i <= i_end):
                    free_path = board.is_square_free(temp_i, temp_j)
                    temp_i += 1
                    temp_j -= 1

            elif (i_end < i_origin) and (j_end < j_origin):# move up and to the left
                temp_i = i_origin - 1
                temp_j = j_origin - 1
                while free_path and (temp_i >= i_end):
                    free_path = board.is_square_free(temp_i, temp_j)
                    temp_i -= 1
                    temp_j -= 1

            elif (i_end < i_origin) and (j_end > j_origin):# move up and to the right
                temp_i = i_origin - 1
                temp_j = j_origin + 1
                while free_path and (temp_i >= i_end):
                    free_path = board.is_square_free(temp_i, temp_j)
                    temp_i -= 1
                    temp_j += 1

            return free_path
        else:
            return False



        return free_path

    ## Simple movement rules
    def is_pawn_movement_valid(self, board, i, j, pawn, player = 'white'):
        i_origin, j_origin = pawn.coordinates

        if player == 'white':
            if j == j_origin:
                if i >= i_origin:
                    return False
                elif i_origin - i == 1:
                    return board.is_square_free(i, j)
                elif i_origin - i == 2:
                    return board.is_square_free(i + 1, j) and board.is_square_free(i, j) and i_origin == 6
                else:
                    return False
            else:
                return False
        elif player == 'black':
            if j == j_origin:
                if i <= i_origin:
                    return False
                elif i - i_origin == 1:
                    return board.is_square_free(i, j)
                elif i - i_origin == 2:
                    return board.is_square_free(i - 1, j) and board.is_square_free(i, j) and i_origin == 1
                else:
                    return False
            else:
                return False

    def is_king_movement_valid(self, board, i, j, king, player = 'white'):
        i_origin, j_origin = king.coordinates

        if ((abs(i - i_origin) == 1) and (abs(j - j_origin) <= 1)
            or (abs(j - j_origin) == 1) and (abs(i - i_origin) <= 1)):
            return board.is_square_free(i,j)
        return False

    def is_bishop_movement_valid(self, board, i, j, bishop,  player = 'white'):
        i_origin, j_origin = bishop.coordinates
        return self.is_diagonal_move_valid(board, i_origin, j_origin, i, j)

    def is_rook_movement_valid(self, board, i, j, rook, player = 'white'):
        # TODO: The rook should eat if final square is occupied
        # TODO: Requesting to leave the piece in place should not be considered a valid move
        i_origin, j_origin = rook.coordinates

        free_path = True
        if (i == i_origin):
            free_path = self.is_lateral_move_valid(board, i_origin, j_origin, i, j)
        elif (j == j_origin):
            free_path = self.is_vertical_move_valid(board, i_origin, j_origin, i, j)
        else:
            return False
        return free_path

    def is_queen_movement_valid(self, board, i, j, queen, player = 'white'):
        return self.is_rook_movement_valid(board, i, j, queen) or self.is_bishop_movement_valid(board, i, j, queen)

    def is_knight_movement_valid(self, board, i, j, knight, player = 'white'):
        # TODO: The knight should eat if final square is occupied
        i_origin, j_origin = knight.coordinates

        if board.is_square_free(i, j):
            return (abs(i - i_origin) == 1) and (abs(j - j_origin) == 2) \
                   or \
                   (abs(i - i_origin) == 2) and (abs(j - j_origin) == 1)

        return False

    ## Eating Rules
    def is_knight_eating_valid(self, board, i, j, knight):
        i_origin, j_origin = knight.coordinates

        if (i == i_origin) and (j == j_origin):
            return False
        elif board.is_square_free(i, j):
            return False
        else:
            victim = board.get_piece_in_square(i, j)
            if victim.color == knight.color:
                return False
            else:
                return (abs(i - i_origin) == 1) and (abs(j - j_origin) == 2) \
                        or \
                        (abs(i - i_origin) == 2) and (abs(j - j_origin) == 1)
        return False

    def is_king_eating_valid(self, board, i, j, king):
        i_origin, j_origin = king.coordinates

        if i == i_origin and j == j_origin:
            return False

        elif board.is_square_free(i, j):
            return False

        else:
            victim = board.get_piece_in_square(i, j)

            if victim.color == king.color:
                return False
            else:
                return ((abs(i - i_origin) == 1) and (abs(j - j_origin) <= 1)
                        or
                        (abs(j - j_origin) == 1) and (abs(i - i_origin) <= 1))
        return False

    def is_bishop_eating_valid(self, board, i, j, bishop):
        i_origin, j_origin = bishop.coordinates

        if i == i_origin and j == j_origin:
            return False

        elif board.is_square_free(i, j):
            return False

        else:

            victim = board.get_piece_in_square(i, j)

            if victim.color == bishop.color:
                return False

            elif abs(i - i_origin) == abs(j - j_origin):

                go_get_it = True
                if abs(i_origin - i) == 1:# Piece to be captured is next to rhe rook
                    return go_get_it

                elif (i >= i_origin) and (j >= j_origin):# move down and to the right before capturing
                    go_get_it = self.is_diagonal_move_valid(board, i_origin, j_origin, i - 1, j - 1)

                elif (i >= i_origin) and (j <= j_origin):# move down and to the left before capturing
                    go_get_it = self.is_diagonal_move_valid(board, i_origin, j_origin, i - 1, j + 1)

                elif (i <= i_origin) and (j <= j_origin):# move up and to the left before capturing
                    go_get_it = self.is_diagonal_move_valid(board, i_origin, j_origin, i + 1, j + 1)

                elif (i <= i_origin) and (j >= j_origin):# move up and to the right before capturing
                    go_get_it = self.is_diagonal_move_valid(board, i_origin, j_origin, i + 1, j - 1)

                return go_get_it

            return False

    def is_queen_eating_valid(self, board, i, j, queen):
        return ( self.is_rook_eating_valid(board, i, j, queen)
               or self.is_bishop_eating_valid(board, i, j, queen) )

    def is_pawn_eating_valid(self, board, i, j, pawn, player = 'white'):
        # TODO: handle 'en passant' pawn capture
        i_origin, j_origin = pawn.coordinates
        if (i == i_origin) and (j == j_origin):
            return False
        elif board.is_square_free(i, j):
            return False
        else:
            victim = board.get_piece_in_square(i, j)
            if pawn.color == victim.color:
                return False
            elif player == 'white':
                if (i_origin - i) == 1 and (abs(j - j_origin) == 1):
                    return True
                else:
                    return False
            elif player == 'black':
                if (i - i_origin == 1) and (abs(j - j_origin) == 1):
                    return True
                else:
                    return False
            return False

    def is_rook_eating_valid(self, board, i, j, rook):
        i_origin, j_origin = rook.coordinates

        if i == i_origin and j == j_origin:
            return False
        elif board.is_square_free(i, j):
            return False
        else:
            victim = board.get_piece_in_square(i, j)
            if rook.color == victim.color:
                return False
            else:
                free_path = True
                if (i == i_origin):
                    if abs(j_origin - j) == 1:# Piece to be captured is next to the rook
                        return free_path
                    elif j > j_origin:# rook moves to the right before capturing
                        free_path = self.is_lateral_move_valid(board, i_origin, j_origin, i, j - 1)
                    elif j < j_origin:# rook moves to the left before capturing
                        free_path = self.is_lateral_move_valid(board, i_origin, j_origin, i, j + 1)

                elif (j == j_origin):
                    if abs(i_origin - i) == 1:# Piece to be captured is next to the rook
                        return free_path
                    if i > i_origin:# rook moves down before capturing
                        free_path = self.is_vertical_move_valid(board, i_origin, j_origin, i - 1, j)
                    elif i < i_origin:# rook moves up before capturing
                        free_path = self.is_vertical_move_valid(board, i_origin, j_origin, i + 1, j)

                else:
                    return False

                return free_path

    def is_king_under_attack(self, board, kings_color = 'white'):

        if kings_color == 'white':
            opponent = 'black'
            the_king = board.king_w[0]
            attackers = board.get_all_black_pieces()

        else:
            opponent = 'white'
            the_king = board.king_b[0]
            attackers = board.get_all_white_pieces()

        i_king, j_king = the_king.coordinates

        checked = False

        for piece in attackers:
            eating_func =  getattr(board.Rules, board.map_piece_to_eating(piece.kind))
            if piece.kind != 'p':
                if eating_func(board, i_king, j_king, piece):
                    col, line = board.get_piece_coords(piece)
                    print "%s king under attack by %s  %s at (%s,%s)" % (kings_color, opponent, piece.kind,col,line)
                    checked = True
            else:
                if eating_func(board, i_king, j_king, piece, opponent):
                    col, line = board.get_piece_coords(piece)
                    print "%s king under attack by %s %s at (%s,%s)" % (kings_color, opponent, piece.kind,col,line)
                    checked = True

        return checked


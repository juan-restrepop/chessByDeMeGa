import unittest
import chess_board as cb

class TestChessBoard(unittest.TestCase):
    
    def test_initialize_board_object_number_of_pieces(self):
        b = cb.ChessBoard()
        
        expected = 32
        actual = len(b.get_all_pieces())
        self.assertEqual(expected, actual)

        expected = 2
        for knights in [b.knights_w, b.knights_b]:
            actual = len(knights)
            self.assertEqual(expected, actual)

        expected = 1
        for queens in [b.queen_w, b.queen_b]:
            actual = len(queens)
            self.assertEqual(expected, actual)

        expected = 1
        for kings in [b.king_w, b.king_b]:
            actual = len(kings)
            self.assertEqual(expected, actual)

        expected = 8 
        actual = len(b.pawns_w)
        self.assertEqual(expected, actual)

        expected = 8 
        actual = len(b.pawns_b)
        self.assertEqual(expected, actual)

        expected = 2 
        actual = len(b.rooks_w)
        self.assertEqual(expected, actual)

        expected = 2 
        actual = len(b.rooks_b)
        self.assertEqual(expected, actual)

        expected = 2 
        actual = len(b.bishops_w)
        self.assertEqual(expected, actual)

        expected = 2 
        actual = len(b.bishops_b)
        self.assertEqual(expected, actual)

    def test_initialize_board_object_position_of_pieces(self):
        b = cb.ChessBoard()

        # black pieces
        expected = True
        for pawn in b.pawns_b:
            positions = []
            for col in range(8):
                positions.append([1, col])
            actual = pawn.coordinates in positions
            self.assertEqual(expected, actual)

        expected = True 
        for rook in b.rooks_b:
            positions = [[0,0],[0,7]]
            actual = rook.coordinates in positions
            self.assertEqual(expected, actual)

        expected = True
        for knight in b.knights_b:
            positions = [[0,1],[0,6]]
            actual = knight.coordinates in positions
            self.assertEqual(expected, actual)

        expected = True
        for bishop in b.bishops_b:
            positions = [[0,2],[0,5]]
            actual = bishop.coordinates in positions
            self.assertEqual(expected, actual)

        expected = True
        for queen in b.queen_b:
            position = [0,3]
            actual = queen.coordinates == position
            self.assertEqual(expected, actual)

        expected = True
        for king in b.king_b:
            position = [0,4]
            actual = king.coordinates == position
            self.assertEqual(expected, actual)

        # white pieces
        expected = True
        for pawn in b.pawns_w:
            positions = []
            for col in range(8):
                positions.append([6, col])
            actual = pawn.coordinates in positions
            self.assertEqual(expected, actual)

        expected = True
        for rook in b.rooks_w:
            actual = rook.coordinates in [ [7, 0], [7,7]]
            self.assertEqual(expected, actual)

        expected = True
        for knight in b.knights_w:
            actual = knight.coordinates in [ [7, 1], [7,6]]
            self.assertEqual(expected, actual)

        expected = True
        for bishop in b.bishops_w:
            actual = bishop.coordinates in [ [7, 2], [7,5]]
            self.assertEqual(expected, actual)

        expected = True
        for queen in b.queen_w:
            actual = queen.coordinates == [7, 3]
            self.assertEqual(expected, actual)

        expected = True
        for king in b.king_w:
            actual = king.coordinates == [7, 4]
            self.assertEqual(expected, actual)

    def test_get_square_color(self):
        
        b = cb.ChessBoard()
        b.initialize_board()

        expected = 0
        actual = b.get_square_color(0, 0)
        self.assertEqual(expected, actual)

        expected = 1
        actual = b.get_square_color(1, 0)
        self.assertEqual(expected, actual)

    def test_clean_pieces(self):
        b = cb.ChessBoard()

        expected = 0
        
        b.clean_pieces()
        actual = len(b.get_all_pieces())
        self.assertEqual(expected, actual)


    def piece_initialization_test(self, kind, color, coordinates):

        b = cb.ChessBoard()
        ## Initialize single piece
        b.clean_pieces()
        b.initialize_single_piece(kind, color, coordinates)

        piece_to_pieces_list = {'wp':b.pawns_w,
                                'bp':b.pawns_b,
                                'wb':b.bishops_w,
                                'bb':b.bishops_b,
                                'wn':b.knights_w,
                                'bn':b.knights_b,
                                'wr':b.rooks_w,
                                'br':b.rooks_b,
                                'wk':b.king_w,
                                'bk':b.king_b,
                                'wq':b.queen_w,
                                'bq':b.queen_b}

        number_pieces_in_board = len(b.get_all_pieces())
        number_pieces_in_list = len(piece_to_pieces_list[color + kind])
        piece_coordinates = piece_to_pieces_list[color + kind][0].coordinates

        return (number_pieces_in_board, number_pieces_in_list, piece_coordinates)

    def test_initialize_single_pieces(self):
        b = cb.ChessBoard()

        pieces_kind = ['p', 'p', 'b', 'b', 'n', 'n', 'r', 'r', 'k', 'k', 'q', 'q']
        pieces_colors = ['w', 'b', 'w', 'b', 'w', 'b', 'w', 'b', 'w', 'b', 'w', 'b']
        pieces_coordinates = [[6, 0], [1, 0], [2, 5], [5, 2], [7, 2], [2, 7], [3, 5], [5,3], [3, 4], [4, 3]]

        for (kind, color, coords) in zip(pieces_kind, pieces_colors, pieces_coordinates):
            # Initialization of a single piece
            b.clean_pieces()
            (pieces_in_board, pieces_in_list, piece_coordinates) = self.piece_initialization_test(kind, color, coords)

            # Test if initialization created only 1 piece
            expected = 1
            self.assertEqual(expected, pieces_in_board)

            # Test if initialized the right piece
            expected = 1
            self.assertEqual(expected, pieces_in_list)

            # Test if piece initialized at right coordinates
            expected = coords
            self.assertEqual(expected, piece_coordinates)

    # Test eating rules
    def test_white_knight_eating_rules(self):
        B = cb.ChessBoard()
        B.clean_pieces()

        B.initialize_single_piece('n', 'w', B.transform_board_to_grid('d', '6'))
        B.initialize_single_piece('p', 'b', B.transform_board_to_grid('c', '8'))
        B.initialize_single_piece('p', 'w', B.transform_board_to_grid('e', '8'))
        B.initialize_single_piece('p', 'w', B.transform_board_to_grid('e', '6'))

        # Test eating well placed opponent
        expected = True
        i, j = B.transform_board_to_grid('c', '8')
        actual = B.Rules.is_knight_eating_valid(B, i, j, B.knights_w[0])
        self.assertEqual(expected, actual)

        # Test eating well placed same color
        expected = False
        i, j = B.transform_board_to_grid('e', '8')
        actual = B.Rules.is_knight_eating_valid(B, i, j, B.knights_w[0])
        self.assertEqual(expected, actual)

        # Test eating empty well placed square
        expected = False
        i, j = B.transform_board_to_grid('f', '5')
        actual = B.Rules.is_knight_eating_valid(B, i, j, B.knights_w[0])
        self.assertEqual(expected, actual)

        # Test eating ill placed opponent
        expected = False
        i, j = B.transform_board_to_grid('e', '6')
        actual = B.Rules.is_knight_eating_valid(B, i, j, B.knights_w[0])
        self.assertEqual(expected, actual)

        # Test eating one self
        expected = False
        i, j = B.transform_board_to_grid('d', '6')
        actual = B.Rules.is_knight_eating_valid(B, i, j, B.knights_w[0])
        self.assertEqual(expected, actual)

    def test_white_queen_eating_rules(self):
        B = cb.ChessBoard()
        B.clean_pieces()

        B.initialize_single_piece('q', 'w', B.transform_board_to_grid('e', '4'))
        B.initialize_single_piece('p', 'b', B.transform_board_to_grid('e', '8'))
        B.initialize_single_piece('p', 'b', B.transform_board_to_grid('h', '7'))
        B.initialize_single_piece('p', 'b', B.transform_board_to_grid('e', '6'))
        B.initialize_single_piece('p', 'b', B.transform_board_to_grid('c', '3'))
        B.initialize_single_piece('p', 'w', B.transform_board_to_grid('h', '4'))

        # Test eating well placed opponent
        movements = ['e6', 'h7']
        expected = True
        for move in movements:
            i, j = B.transform_board_to_grid(move[0], move[1])
            actual = B.Rules.is_queen_eating_valid(B, i, j, B.queen_w[0])
            self.assertEqual(expected, actual)

        # Test eating well placed same color
        move = 'h4'
        i, j = B.transform_board_to_grid(move[0], move[1])
        expected = False
        actual = B.Rules.is_queen_eating_valid(B, i, j, B.queen_w[0])
        self.assertEqual(expected, actual)

        # Test eating well placed empty square
        move = 'c4'
        i, j = B.transform_board_to_grid(move[0], move[1])
        expected = False
        actual = B.Rules.is_queen_eating_valid(B, i, j, B.queen_w[0])
        self.assertEqual(expected, actual)

        # Test ill placed opponent
        move = 'c3'
        i, j = B.transform_board_to_grid(move[0], move[1])
        expected = False
        actual = B.Rules.is_queen_eating_valid(B, i, j, B.queen_w[0])
        self.assertEqual(expected, actual)

        # Test blocked eating
        move = 'e8'
        i, j = B.transform_board_to_grid(move[0], move[1])
        expected = False
        actual = B.Rules.is_queen_eating_valid(B, i, j, B.queen_w[0])
        self.assertEqual(expected, actual)

        # Test eating itself
        move = 'e4'
        i, j = B.transform_board_to_grid(move[0], move[1])
        expected = False
        actual = B.Rules.is_queen_eating_valid(B, i, j, B.queen_w[0])
        self.assertEqual(expected, actual)

    def test_white_pawn_eating_rules(self):
        B = cb.ChessBoard()

        # Test eating well placed opponents
        B.clean_pieces()
        B.initialize_single_piece('p', 'w', B.transform_board_to_grid('d', '3'))
        B.initialize_single_piece('p', 'b', B.transform_board_to_grid('c', '4'))
        B.initialize_single_piece('p', 'b', B.transform_board_to_grid('e', '4'))

        movements = ['e4', 'c4']
        expected = True
        for move in movements:
            i, j = B.transform_board_to_grid(move[0], move[1])
            actual = B.Rules.is_pawn_eating_valid(B, i, j, B.pawns_w[0])
            self.assertEqual(expected, actual)

        # Test eating well placed same color
        B.clean_pieces()
        B.initialize_single_piece('p', 'w', B.transform_board_to_grid('d', '3'))
        B.initialize_single_piece('n', 'w', B.transform_board_to_grid('c', '4'))
        B.initialize_single_piece('r', 'w', B.transform_board_to_grid('e', '4'))

        movements = ['e4', 'c4']
        expected = False
        for move in movements:
            i, j = B.transform_board_to_grid(move[0], move[1])
            actual = B.Rules.is_pawn_eating_valid(B, i, j, B.pawns_w[0])
            self.assertEqual(expected, actual)

        # Test eating ill placed opponent
        B.clean_pieces()
        B.initialize_single_piece('p', 'w', B.transform_board_to_grid('d', '3'))
        B.initialize_single_piece('p', 'b', B.transform_board_to_grid('d', '4'))
        B.initialize_single_piece('p', 'b', B.transform_board_to_grid('c', '3'))
        B.initialize_single_piece('p', 'b', B.transform_board_to_grid('c', '2'))
        B.initialize_single_piece('p', 'b', B.transform_board_to_grid('d', '2'))
        B.initialize_single_piece('p', 'b', B.transform_board_to_grid('e', '2'))
        B.initialize_single_piece('p', 'b', B.transform_board_to_grid('e', '3'))

        movements = ['d4', 'c3', 'c2', 'd2', 'e2', 'e3']
        expected = False
        for move in movements:
            i, j = B.transform_board_to_grid(move[0], move[1])
            actual = B.Rules.is_pawn_eating_valid(B, i, j, B.pawns_w[0])
            self.assertEqual(expected, actual)

        # Test eating well placed empty square
        B.clean_pieces()
        B.initialize_single_piece('p', 'w', B.transform_board_to_grid('d', '3'))

        movements = ['c4', 'e4']
        expected = False
        for move in movements:
            i, j = B.transform_board_to_grid(move[0], move[1])
            actual = B.Rules.is_pawn_eating_valid(B, i, j, B.pawns_w[0])
            self.assertEqual(expected, actual)

        # And test eating itself
        move = 'd3'
        i, j = B.transform_board_to_grid(move[0], move[1])
        expected = False
        actual = B.Rules.is_pawn_eating_valid(B, i, j, B.pawns_w[0])
        self.assertEqual(expected, actual)

    def test_white_rook_eating_rules(self):
        B = cb.ChessBoard()
        B.clean_pieces()

        B.initialize_single_piece('r', 'w', B.transform_board_to_grid('d', '3'))
        B.initialize_single_piece('p', 'b', B.transform_board_to_grid('a', '3'))
        B.initialize_single_piece('p', 'b', B.transform_board_to_grid('d', '1'))
        B.initialize_single_piece('p', 'w', B.transform_board_to_grid('h', '3'))
        B.initialize_single_piece('p', 'w', B.transform_board_to_grid('d', '6'))
        B.initialize_single_piece('p', 'b', B.transform_board_to_grid('d', '4'))
        B.initialize_single_piece('p', 'b', B.transform_board_to_grid('d', '8'))


        # Test eating well placed opponent
        movements = ['a3', 'd1', 'd4']
        expected = True
        for move in movements:
            i, j = B.transform_board_to_grid(move[0], move[1])
            actual = B.Rules.is_rook_eating_valid(B, i, j, B.rooks_w[0])
            self.assertEqual(expected, actual)

        # Test eating well placed same color
        movements = ['h3', 'd6']
        expected = False
        for move in movements:
            i, j = B.transform_board_to_grid(move[0], move[1])
            actual = B.Rules.is_rook_eating_valid(B, i, j, B.rooks_w[0])
            self.assertEqual(expected, actual)

        # Test eating well placed empty square
        move = 'd5'
        expected = False
        i, j = B.transform_board_to_grid(move[0], move[1])
        actual = B.Rules.is_rook_eating_valid(B, i, j, B.rooks_w[0])
        self.assertEqual(expected, actual)

        # Test eating ill placed opponent
        move = 'e4'
        expected = False
        i, j = B.transform_board_to_grid(move[0], move[1])
        actual = B.Rules.is_rook_eating_valid(B, i, j, B.rooks_w[0])
        self.assertEqual(expected, actual)

        # Test blocked eating
        move = 'd8'
        expected = False
        i, j = B.transform_board_to_grid(move[0], move[1])
        actual = B.Rules.is_rook_eating_valid(B, i, j, B.rooks_w[0])
        self.assertEqual(expected, actual)

        #Test eating itself
        move = 'd3'
        expected = False
        i, j = B.transform_board_to_grid(move[0], move[1])
        actual = B.Rules.is_rook_eating_valid(B, i, j, B.rooks_w[0])
        self.assertEqual(expected, actual)

    def test_white_king_eating_rules(self):
        b = cb.ChessBoard()

        # accepted eating
        for kind, color, coords in  [('p', 'b', ['e','3']),
                                     ('q', 'b', ['e','5']),
                                     ('b', 'b', ['d','3']),
                                     ('r', 'b', ['f','5']),
                                     ('b', 'b', ['f','4'])
                                    ]:

            b.clean_pieces()
            b.initialize_single_piece('k','w',b.transform_board_to_grid('e','4'))
            i,j = b.transform_board_to_grid(coords[0],coords[1])
            b.initialize_single_piece(kind,color,[i,j])
            expected = True
            actual = b.Rules.is_king_eating_valid(b,i,j,b.king_w[0])
            self.assertEqual(expected, actual, msg = 'unable to eat %s at %s %s' %(kind, coords[0], coords[1]))

        # forbidden eating of same team (in the king case is the same test for forbidden blocked displacement)
        b.clean_pieces()
        b.initialize_single_piece('k', 'w', b.transform_board_to_grid('e','4'))
        i,j = b.transform_board_to_grid('e', '3')
        b.initialize_single_piece('p', 'w', [i, j])
        expected = False
        actual = b.Rules.is_king_eating_valid(b, i , j, b.king_w[0])
        self.assertEqual(expected, actual, msg = 'eating same team piece')

        # forbidden eating of empty square
        i,j = b.transform_board_to_grid('e', '5')
        expected = False
        actual = b.Rules.is_king_eating_valid(b, i, j, b.king_w[0])
        self.assertEqual(expected, actual, msg = 'eating nobody')

        # forbidden suicide
        i,j = b.transform_board_to_grid('e','4')
        expected = False
        actual = b.Rules.is_king_eating_valid(b,i,j,b.king_w[0])
        self.assertEqual(expected, actual, msg = 'suicidal king')

        # forbidden king displacement
        i,j = b.transform_board_to_grid('h','4')
        expected = False
        actual = b.Rules.is_king_eating_valid(b,i,j,b.king_w[0])
        self.assertEqual(expected, actual, msg = 'thy majesty is going way to far')

    def test_white_bishop_eating_rules(self):
        b = cb.ChessBoard()

        # accepted eating
        for kind, color, coords in  [('p', 'b', ['c','6']),
                                     ('q', 'b', ['f','3']),
                                     ('b', 'b', ['h','7']),
                                     ('r', 'b', ['a','8']),
                                    ]:
            b.clean_pieces()
            b.initialize_single_piece('b', 'w', b.transform_board_to_grid('e', '4'))
            i,j = b.transform_board_to_grid(coords[0], coords[1])
            b.initialize_single_piece(kind, color, [i, j])
            expected = True
            actual = b.Rules.is_bishop_eating_valid(b, i, j, b.bishops_w[0])
            self.assertEqual(expected,actual, msg = 'unable to eat %s at %s %s' %(kind, coords[0], coords[1]))

        # forbidden suicide
        b.clean_pieces()
        i,j = b.transform_board_to_grid('e','4')
        b.initialize_single_piece('b', 'w', [i, j])
        expected = False
        actual = b.Rules.is_bishop_eating_valid(b, i, j, b.bishops_w[0])
        self.assertEqual(expected, actual, msg = 'suicidal bishop')

        # forbidden displacement
        i, j  = b.transform_board_to_grid('h','4')
        b.initialize_single_piece('p', 'b', [i, j])
        expected = False
        actual = b.Rules.is_bishop_eating_valid(b, i, j, b.bishops_w[0])
        self.assertEqual(expected, actual, msg = "bishop shouldn't  eat at (h,4), forbidden displacement" )

        # forbidden kill teamate
        i, j  = b.transform_board_to_grid('g','6')
        b.initialize_single_piece('p', 'w', [i, j])
        expected = False
        actual = b.Rules.is_bishop_eating_valid(b, i, j, b.bishops_w[0])
        self.assertEqual(expected, actual, msg = 'bishop killing teamate')

        # forbidden blocked
        i, j  = b.transform_board_to_grid('h','7')
        b.initialize_single_piece('q', 'b', [i, j])
        expected = False
        actual = b.Rules.is_bishop_eating_valid(b, i, j, b.bishops_w[0])
        self.assertEqual(expected, actual, msg = "bishop shouldn't  eat at (h,7), someone in the same path" )

    # Test movement rules
    def test_black_pawn_movement_rules(self):
        # forbidden
        b = cb.ChessBoard()
        b.clean_pieces()

        moves = [['d','7'],['f','7'], # lateral
                 ['d','6'],['f','6'], # fwd-diagonal
                 ['c','8'],['d','8'],['e','8'], # backwards
                 ['e','4'],           # fwd, more than 2
                 ['e','7']]           # in-place

        expected = False
        for move in moves:
            b.clean_pieces()
            b.initialize_single_piece('p', 'b', b.transform_board_to_grid('e', '7'))
            actual = b.piece_mover('p',move[0],move[1],'black')
            self.assertEqual(actual,expected)

        # forbidden: more than 2 in line < 7
        b.clean_pieces()
        expected = False
        b.initialize_single_piece('p', 'b', b.transform_board_to_grid('e', '6'))
        move = ['e','4']
        actual  = b.piece_mover('p',move[0],move[1],'black')
        self.assertEqual(actual,expected)

        # accepted: single and double in the starting line
        expected = True
        moves = [['e', '6'], ['e', '5']]

        for move in moves:
            b.clean_pieces()
            b.initialize_single_piece('p', 'b', b.transform_board_to_grid('e', '7'))
            actual  = b.piece_mover('p',move[0],move[1],'black')
            self.assertEqual(actual,expected)

        # accepted: single elsewhere
        expected = True
        b.clean_pieces()
        b.initialize_single_piece('p', 'b', b.transform_board_to_grid('e', '4'))
        actual  = b.piece_mover('p','e','3','black')
        self.assertEqual(actual,expected)

    def test_black_pawn_blocked_movement(self):
        b = cb.ChessBoard()

        b.clean_pieces()
        expected = False
        b.initialize_single_piece('p', 'b', b.transform_board_to_grid('e', '7'))
        b.initialize_single_piece('n', 'w', b.transform_board_to_grid('e', '6'))

        actual  = b.piece_mover('p','e','6','black')
        self.assertEqual(expected, actual)

        actual  = b.piece_mover('p','e','5','black')
        self.assertEqual(expected, actual)

        b.clean_pieces()
        expected = False
        b.initialize_single_piece('p', 'b', b.transform_board_to_grid('e', '6'))
        b.initialize_single_piece('n', 'w', b.transform_board_to_grid('e', '5'))
        actual  = b.piece_mover('p','e','5','black')
        self.assertEqual(expected, actual)

    def test_white_pawn_movement_rules(self):
        b = cb.ChessBoard()

        ## Initialize white pawn on 'd2'
        b.clean_pieces()
        b.initialize_single_piece('p', 'w', b.transform_board_to_grid('d', '2'))

        ## Test forbidden moves
        # Test forbidden forward-diagonal moves
        expected = False
        for move in [['e','3'], ['c','3']]:
            actual = b.piece_mover('p',move[0], move[1], 'white')
            self.assertEqual(expected, actual)

        # Test forbidden lateral moves
        expected = False
        for move in [['e','2'], ['c','2']]:
            actual = b.piece_mover('p',move[0], move[1], 'white')
            self.assertEqual(expected, actual)

        # Test forbidden backwards moves
        expected = False
        for move in [['e','1'], ['c','1'], ['d', '1']]:
            actual = b.piece_mover('p',move[0], move[1], 'white')
            self.assertEqual(expected, actual)

        # Test forbidden forward move longer than 2
        expected = False
        actual = b.piece_mover('p','d', '5', 'white')
        self.assertEqual(expected, actual)

        # Test forbidden in-place move
        expected = False
        b.clean_pieces()
        b.initialize_single_piece('p', 'w', b.transform_board_to_grid('d', '2'))
        actual = b.piece_mover('p','d', '2', 'white')
        self.assertEqual(expected, actual)

        ## Test approved moves if initial position
        # simple initial move
        b.clean_pieces()
        b.initialize_single_piece('p', 'w', b.transform_board_to_grid('d', '2'))

        expected = True
        actual = b.piece_mover('p','d','3', 'white')
        self.assertEqual(expected, actual)

        # double initial move
        b.clean_pieces()
        b.initialize_single_piece('p', 'w', b.transform_board_to_grid('d', '2'))

        expected = True
        actual = b.piece_mover('p','d','4', 'white')
        self.assertEqual(expected, actual)

        ## Test approved moves
        # simple move
        b.clean_pieces()
        b.initialize_single_piece('p', 'w', b.transform_board_to_grid('d', '4'))

        expected = True
        actual = b.piece_mover('p','d','5', 'white')
        self.assertEqual(expected, actual)

        # double move
        b.clean_pieces()
        b.initialize_single_piece('p', 'w', b.transform_board_to_grid('d', '4'))

        expected = False
        actual = b.piece_mover('p','d','6', 'white')
        self.assertEqual(expected, actual)

    def test_white_pawn_blocked_movement_rules(self):
        b = cb.ChessBoard()

        ## Initialize white pawn on 'd2' and black knight on 'd3'
        b.clean_pieces()
        b.initialize_single_piece('p', 'w', [6, 3])
        b.initialize_single_piece('n', 'b', [5, 3])

        expected = False
        actual = b.piece_mover('p','d', '3','white')
        self.assertEqual(expected, actual)

        ## Initialize white pawn on 'd2' and black knight on 'd3'
        b.clean_pieces()
        b.initialize_single_piece('p', 'w', [6, 3])
        b.initialize_single_piece('n', 'b', [5, 3])

        expected = False
        actual = b.piece_mover('p','d', '4','white')
        self.assertEqual(expected, actual)

    def test_bishop_movement_rules(self):
        b = cb.ChessBoard()
        
        ## Accepted moves : down-left, down-right, up-left, up-right
        movements = [['d', '3'], ['f', '3'], ['c', '6'], ['h', '7']]
        for move in movements:

            # Test white bishop on 'e4'
            b.clean_pieces()
            b.initialize_single_piece('b', 'w', [4, 4])
            expected = True
            actual = b.piece_mover('b',move[0],move[1], 'white')
            self.assertEqual(expected, actual)

            # Test black bishop on 'e4'
            b.clean_pieces()
            b.initialize_single_piece('b', 'b', [4, 4])
            expected = True
            actual = b.piece_mover('b',move[0],move[1], 'black')
            self.assertEqual(expected, actual)

        ## Unaccepted moves : left, right, up, down
        movements = [['d', '4'], ['f', '4'], ['e', '6'],['e', '2']]
        for move in movements:

            # Test white bishop on 'e4'
            b.clean_pieces()
            b.initialize_single_piece('b', 'w', [4, 4])
            expected = False
            actual = b.piece_mover('b',move[0],move[1], 'white')
            self.assertEqual(expected, actual)

            # Test black bishop on 'e4'
            b.clean_pieces()
            b.initialize_single_piece('b', 'b', [4, 4])
            expected = False
            actual = b.piece_mover('b',move[0],move[1], 'black')
            self.assertEqual(expected, actual)

    def test_bishop_blocked_movement_rules(self):

        b = cb.ChessBoard()

        ## test not accepted moves : down-left,down-right,up-left,up-right
        movements = [['d','3'],['f','3'],['c','6'],['h','7']]
        blocking_pieces =  [[5,3], [5,5], [3,3],[2,6]]

        for move,blocking_piece in zip(movements, blocking_pieces):

            # Test white bishop on 'e4'
            b.clean_pieces()
            b.initialize_single_piece('b', 'w', [4, 4])
            b.initialize_single_piece('p', 'b', blocking_piece)
            expected = False
            actual = b.piece_mover('b',move[0],move[1], 'white')
            self.assertEqual(expected, actual, msg= 'Error while attempting move bishop  to (%s,%s)' % (move[0], move[1]))

            # Test black bishop on 'e4'
            b.clean_pieces()
            b.initialize_single_piece('b', 'b', [4, 4])
            b.initialize_single_piece('p', 'w', blocking_piece)
            expected = False
            actual = b.piece_mover('b',move[0],move[1], 'black')
            self.assertEqual(expected, actual, msg= 'Error while attempting move bishop  to (%s,%s)' % (move[0], move[1]))

        b.clean_pieces()
        
        # Do not accept a forbidden movement to an occupied place!
        b.initialize_single_piece('b', 'b', b.transform_board_to_grid('c','1'))
        blocking_piece = ['f','2']
        move = blocking_piece
        b.initialize_single_piece('p', 'w', b.transform_board_to_grid(blocking_piece[0],blocking_piece[1] ))
        expected = False
        actual = b.piece_mover('b',blocking_piece[0],blocking_piece[1], 'black')
        self.assertEqual(expected, actual, msg= 'Error while attempting move bishop  to (%s,%s)' % (move[0], move[1]))

    def test_knight_movement_rules(self):
        b = cb.ChessBoard()

        ## Test forbidden moves
        movements = [['d', '3'], ['d','5'], \
                        ['c', '4'], ['e', '4'], \
                        ['c', '5'], ['e', '5'], ['c', '3'], ['e', '3']]

        # Test white knight on 'd4'
        b.clean_pieces()
        b.initialize_single_piece('n', 'w', [4, 3])

        expected = False
        for move in movements:
            actual = b.piece_mover('n',move[0], move[1], 'white')
            self.assertEqual(expected, actual)

        # Test black knight on 'd4'
        b.clean_pieces()
        b.initialize_single_piece('n', 'b', [4, 3])

        expected = False
        for move in movements:
            actual = b.piece_mover('n',move[0], move[1], 'black')
            self.assertEqual(expected, actual)

        ## Test approved moves
        movements = [['b', '5'], ['f', '5'], \
                     ['b', '3'], ['f', '3'], \
                     ['c', '6'], ['e', '6'], \
                     ['c', '2'], ['e', '2']]

        # Test white knight on 'd4'
        b.clean_pieces()

        expected = True
        for move in movements:
            b.clean_pieces()
            b.initialize_single_piece('n', 'w', [4, 3])

            actual = b.piece_mover('n',move[0], move[1], 'white')
            self.assertEqual(expected, actual)

        # Test black knight on 'd4'
        b.clean_pieces()

        expected = True
        for move in movements:
            b.clean_pieces()
            b.initialize_single_piece('n', 'b', [4, 3])

            actual = b.piece_mover('n',move[0], move[1], 'black')
            self.assertEqual(expected, actual)

    def test_knight_blocked_movement_rules(self):
        b = cb.ChessBoard()

        ## Initialize white knight in 'b1' and white pawns in 'd2' and 'b2'
        b.clean_pieces()
        b.initialize_single_piece('n', 'w', [7, 1])
        b.initialize_single_piece('p', 'w', [6, 3])
        b.initialize_single_piece('p', 'w', [6, 1])

        # test blocked move
        expected = False
        actual = b.piece_mover('n','d', '4', 'white')
        self.assertEqual(expected, actual)

        # test approved move
        expected = True
        actual = b.piece_mover('n','a', '3', 'white')
        self.assertEqual(expected, actual)

        ## Initialize black knight in 'b1' and white pawns in 'd2' and 'b2'
        b.clean_pieces()
        b.initialize_single_piece('n', 'b', [7, 1])
        b.initialize_single_piece('p', 'w', [6, 3])
        b.initialize_single_piece('p', 'w', [6, 1])

        # test blocked move
        expected = False
        actual = b.piece_mover('n','d', '4', 'black')
        self.assertEqual(expected, actual)

        # test approved move
        expected = True
        actual = b.piece_mover('n','a', '3', 'black')
        self.assertEqual(expected, actual)

    def test_rook_movement_rules(self):
        b = cb.ChessBoard()

        ## Test forbidden moves
        movements = [['d', '3'], ['c', '2'], \
                     ['f','5'], ['g', '6']]

        # Test white rook on 'e4'
        b.clean_pieces()
        b.initialize_single_piece('r', 'w', [4, 4])
        expected = False
        for move in movements:
            actual = b.piece_mover('r',move[0], move[1], 'white')
            self.assertEqual(expected, actual)

        # Test black rook on 'e4'
        b.clean_pieces()
        b.initialize_single_piece('r', 'b', [4, 4])
        expected = False
        for move in movements:
            actual = b.piece_mover('r',move[0], move[1], 'black')
            self.assertEqual(expected, actual)

        ## Test approved moves
        movements = [['f','4'], ['g', '4'], \
                     ['e','7'], ['e', '8'], \
                     ['b', '4'], \
                     ['e', '1']]

        expected = True
        for move in movements:
            # Test white rook on 'e4'
            b.clean_pieces()
            b.initialize_single_piece('r', 'w', [4, 4])
            actual = b.piece_mover('r',move[0], move[1], 'white')
            self.assertEqual(expected, actual)

            # Test black rook on 'e4'
            b.clean_pieces()
            b.initialize_single_piece('r', 'b', [4, 4])
            actual = b.piece_mover('r',move[0], move[1], 'black')
            self.assertEqual(expected, actual)

    def test_rook_blocked_movement_rules(self):
        b = cb.ChessBoard()

        ## Blocking white pawn in 'g4' and black knight in 'e6'

        ## Test non-blocked movements
        movements = [['e', '5'], ['f', '4']]
        expected = True
        for move in movements:
            # Test white rook on 'e4'
            b.clean_pieces()
            b.initialize_single_piece('r', 'w', [4, 4])
            b.initialize_single_piece('p', 'w', [4, 6])
            b.initialize_single_piece('n', 'b', [2, 4])

            actual = b.piece_mover('r',move[0], move[1], 'white')
            self.assertEqual(expected, actual)

            # Test black rook on 'e4'
            b.clean_pieces()
            b.initialize_single_piece('r', 'b', [4, 4])
            b.initialize_single_piece('p', 'w', [4, 6])
            b.initialize_single_piece('n', 'b', [2, 4])

            actual = b.piece_mover('r',move[0], move[1], 'black')
            self.assertEqual(expected, actual)

        ## Test blocked movements
        movements = [['e', '6'], ['h', '4']]
        expected = False
        for move in movements:
            # Test white rook on 'e4'
            b.clean_pieces()
            b.initialize_single_piece('r', 'w', [4, 4])
            b.initialize_single_piece('p', 'w', [4, 6])
            b.initialize_single_piece('n', 'b', [2, 4])

            actual = b.piece_mover('r',move[0], move[1], 'white')
            self.assertEqual(expected, actual)

            # Test black rook on 'e4'
            b.clean_pieces()
            b.initialize_single_piece('r', 'b', [4, 4])
            b.initialize_single_piece('p', 'w', [4, 6])
            b.initialize_single_piece('n', 'b', [2, 4])

            actual = b.piece_mover('r',move[0], move[1], 'black')
            self.assertEqual(expected, actual)

    def test_king_movement_rules(self):
        b = cb.ChessBoard()

        ## Accepted moves
        movements = [['e', '6'], ['f', '6'], ['g', '6'],
                     ['e', '5'], ['g','5'],
                     ['e', '4'], ['f', '4'], ['g', '4']]

        for move in movements:
            # Test white king on 'f5'
            b.clean_pieces()
            b.initialize_single_piece('k', 'w', [3, 5])
            expected = True
            actual = b.piece_mover('k',move[0],move[1], 'white')
            self.assertEqual(expected, actual)

            # Test black king on 'f5'
            b.clean_pieces()
            b.initialize_single_piece('k', 'b', [3, 5])
            expected = True
            actual = b.piece_mover('k',move[0],move[1], 'black')
            self.assertEqual(expected, actual)
        
        ## Unaccepted moves c8,f7,h7,h5,h3,f3,c2
        movements = [['c', '8'], ['f', '7'],['h', '7'],
                     ['a', '5'], ['h', '5'],
                     ['h', '3'], ['f', '3'], ['c', '2'],
                     ['g', '3']]

        for move in movements:
            # Test white king on 'f5'
            b.clean_pieces()
            b.initialize_single_piece('k', 'w', [3, 5])
            expected = False
            actual = b.piece_mover('k',move[0],move[1], 'white')
            self.assertEqual(expected, actual)

            # Test black king on 'f5'
            b.clean_pieces()
            b.initialize_single_piece('k', 'b', [3, 5])
            expected = False
            actual = b.piece_mover('k',move[0],move[1], 'black')
            self.assertEqual(expected, actual)

    def test_king_blocked_movement_rules(self):
        b = cb.ChessBoard()

        movements = [['d', '4'], ['e', '4'], ['f', '4'],
                     ['d', '3'], ['f', '3'],
                     ['d', '2'], ['e', '2'], ['f', '2']]

        blocking_pieces_coordinates = [['d', '4'], ['e', '4'], ['f', '4'],
                           ['d', '3'], ['f', '3'],
                           ['d', '2'], ['e', '2'], ['f', '2']]

        expected = False
        for move, coords in zip(movements, blocking_pieces_coordinates):
            # Test white king on 'e3'
            b.clean_pieces()
            b.initialize_single_piece('k','w',[5,4])
            b.initialize_single_piece('k','w', b.transform_board_to_grid(coords[0],coords[1]))
            actual = b.piece_mover('k',coords[0], coords[1], 'white')
            self.assertEqual(expected, actual)

            # Test black king on 'e3'
            b.clean_pieces()
            b.initialize_single_piece('k','b',[5,4])
            b.initialize_single_piece('k','w', b.transform_board_to_grid(coords[0],coords[1]))
            actual = b.piece_mover('k',coords[0], coords[1], 'black')
            self.assertEqual(expected, actual)

    def test_queen_movement_rules(self):
        b = cb.ChessBoard()

        movements = [['b', '4'], ['a', '2'], ['c', '1'], ['f', '1'], ['g', '4'], ['g', '8'], ['c', '8'], ['a', '6']]
        expected = True

        for move in movements:
            # Test white queen on 'c4'
            b.clean_pieces()
            b.initialize_single_piece('q', 'w', [4, 2])
            actual = b.piece_mover('q',move[0], move[1], 'white')
            self.assertEqual(expected, actual)

            # Test black queen on 'c4'
            b.clean_pieces()
            b.initialize_single_piece('q', 'b', [4, 2])
            actual = b.piece_mover('q',move[0], move[1], 'black')
            self.assertEqual(expected, actual)

    def test_queen_blocked_movement_rules(self):
        b = cb.ChessBoard()

        # Blocking white pawn on 'g4', black rook in 'c6' and black knight in 'f7'
        movements = [['g', '4'], ['h', '4'], ['c', '7'], ['g', '8']]

        expected = False
        for move in movements:
            # Test white queen on 'c4'
            b.clean_pieces()
            b.initialize_single_piece('q', 'w', [4, 2])
            b.initialize_single_piece('p', 'w', [4, 6])
            b.initialize_single_piece('r', 'b', [2, 2])
            b.initialize_single_piece('n', 'b', [1, 5])

            actual = b.piece_mover('q',move[0], move[1], 'white')
            self.assertEqual(expected, actual)

            # Test black queen on 'c4'
            b.clean_pieces()
            b.initialize_single_piece('q', 'b', [4, 2])
            b.initialize_single_piece('p', 'w', [4, 6])
            b.initialize_single_piece('r', 'b', [2, 2])
            b.initialize_single_piece('n', 'b', [1, 5])

            actual = b.piece_mover('q',move[0], move[1], 'black')
            self.assertEqual(expected, actual)

    # Test if move correctly done
    def test_knight_movement(self):
        b = cb.ChessBoard()
        b_ref = cb.ChessBoard()

        # Test good move
        good_move = b.transform_grid_to_board(5, 6)
        b.clean_pieces()
        b.initialize_single_piece('n', 'b', [4, 4])
        b.piece_mover('n', good_move[0], good_move[1], 'black')

        b_ref.clean_pieces()
        b_ref.initialize_single_piece('n', 'b', [5, 6])

        expected = b_ref.color_augmented_grid()
        actual = b.color_augmented_grid()
        self.assertEqual(expected, actual)

        # Test bad move
        bad_move = b.transform_grid_to_board(5, 4)
        b.clean_pieces()
        b.initialize_single_piece('n', 'b', [4, 4])
        b.piece_mover('n', bad_move[0], bad_move[1], 'black')

        b_ref.clean_pieces()
        b_ref.initialize_single_piece('n', 'b', [4, 4])

        expected = b_ref.color_augmented_grid()
        actual = b.color_augmented_grid()
        self.assertEqual(expected, actual)



    def test_is_king_under_attack(self):
        b = cb.ChessBoard()

        pieces = [['r','w','a','4'],
                  ['b','w','a','1'],
                  ['n','w','c','2'],
                  ['q','w','d','8'],
                  ['p','w','e','3'],
                  ['p','w','c','3']]

        for piece, color, col, line in pieces:
            b.clean_pieces()
            b.initialize_single_piece('k', 'b', b.transform_board_to_grid('d', '4'))
            b.initialize_single_piece(piece, color, b.transform_board_to_grid(col, line))
            actual  = b.Rules.is_king_under_attack(b, 'black')
            expected = True
            self.assertEqual(expected, actual, msg= 'Error while attempting check with %s at (%s,%s)' % (piece, col, line))

            pieces = [['r','b','a','5'],
                      ['b','b','b','1'],
                      ['n','b','e','3'],
                      ['q','b','f','8'],
                      ['p','b','e','6'],
                      ['p','b','g','6']]

        for piece, color, col, line in pieces:
            b.clean_pieces()
            b.initialize_single_piece('k', 'w', b.transform_board_to_grid('f', '5'))
            b.initialize_single_piece(piece, color, b.transform_board_to_grid(col, line))
            actual  = b.Rules.is_king_under_attack(b, 'white')
            expected = True
            self.assertEqual(expected, actual, msg= 'Error while attempting check with %s at (%s,%s)' % (piece, col, line))


    def test_transform_coords(self):
        b = cb.ChessBoard()

        board_cols = ['a','b','c','d','e','f','g','h']
        grid_cols = [0, 1, 2, 3, 4, 5, 6, 7]

        board_lines = ['8', '7', '6', '5', '4', '3', '2', '1']
        grid_lines = [0, 1, 2, 3, 4, 5, 6, 7]

        for (col, line, i, j) in zip(board_cols, board_lines, grid_lines, grid_cols):
            new_col, new_line = b.transform_grid_to_board(i, j)
            new_i, new_j = b.transform_board_to_grid(col, line)

            self.assertEqual(col, new_col)
            self.assertEqual(line, new_line)
            self.assertEqual(i, new_i)
            self.assertEqual(j, new_j)

if __name__ == '__main__':
    unittest.main()






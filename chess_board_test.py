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

    def test_white_pawn_enpassant_eating_rules(self):
        # from wikipedia
        # the capturing pawn must be on its fifth rank.
        # the captured pawn must be on an adjacent file and must have just moved two squares in a single move.
        # the capture can only be made on the move immediately after the opposing pawn makes the double-step move.
        b = cb.ChessBoard()
        b.clean_pieces()

        #test accepted enpassant: black d7-d5 > white cxd6
        b.initialize_single_piece('p', 'b', b.transform_board_to_grid('d', '7'))
        b.initialize_single_piece('p', 'w', b.transform_board_to_grid('c', '5'))
        b.piece_mover('p','d','5', 'black')
        i,j = b.transform_board_to_grid('d', '6')
        expected = True
        actual = b.Rules.is_pawn_eating_valid(b, i, j, b.pawns_w[0])
        self.assertEqual(expected,actual, msg= "cxd6 capture should be allowed")

        #test forbidden enpassant: black d7-d5 > white c6xd7  (not 5th file)
        b.clean_pieces()
        b.initialize_single_piece('p', 'w', b.transform_board_to_grid('c', '6'))
        b.initialize_single_piece('p', 'b', b.transform_board_to_grid('d', '7'))
        b.piece_mover('p','d','5', 'black')
        i,j = b.transform_board_to_grid('d', '7')
        expected = False
        actual = b.Rules.is_pawn_eating_valid(b, i, j, b.pawns_w[0])
        self.assertEqual(expected,actual, msg= "cxd7 capture shouldn't be allowed")

        #test forbidden enpassant: black e7-e5 > white c5xe6 (not adjacent)
        b.clean_pieces()
        b.initialize_single_piece('p', 'w', b.transform_board_to_grid('c', '6'))
        b.initialize_single_piece('p', 'b', b.transform_board_to_grid('e', '7'))
        b.piece_mover('p','e','5', 'black')
        i,j = b.transform_board_to_grid('e', '6')
        expected = False
        actual = b.Rules.is_pawn_eating_valid(b, i, j, b.pawns_w[0])
        self.assertEqual(expected,actual, msg = "cxe5 capture shouldn't be allowed")

    def test_white_pawn_enpassant_eating_complex(self):
        # test forbidden enpassant:
        # black d7-d5 > white Rh1-Rh3
        # black Ra8-Ra6 > white c5xd6 (not immediately after)
        b = cb.ChessBoard()
        b.clean_pieces()
        b.initialize_single_piece('r', 'b', b.transform_board_to_grid('a', '8'))
        b.initialize_single_piece('p', 'b', b.transform_board_to_grid('d', '7'))
        b.initialize_single_piece('r', 'w', b.transform_board_to_grid('h', '1'))
        b.initialize_single_piece('p', 'w', b.transform_board_to_grid('c', '5'))

        b.piece_mover('p','d','5', 'black')
        b.piece_mover('r','h','3', 'white')
        b.piece_mover('r','a','6', 'black')
        i,j = b.transform_board_to_grid('d', '6')
        actual = b.Rules.is_pawn_eating_valid(b, i, j, b.pawns_w[0])
        expected = False
        self.assertEqual(expected,actual, msg= "cxd6 capture should be forbidden (late capture)")

    def test_black_pawn_enpassant_eating_rules(self):
        b = cb.ChessBoard()
        b.clean_pieces()

        # test accepted en passant: white b2 -> b4 > black cxb3
        b.initialize_single_piece('p', 'w', b.transform_board_to_grid('b', '2'))
        b.initialize_single_piece('p', 'b', b.transform_board_to_grid('c', '4'))
        b.piece_mover('p','b','4', 'white')
        i,j = b.transform_board_to_grid('b', '3')
        expected = True
        actual = b.Rules.is_pawn_eating_valid(b, i, j, b.pawns_b[0], 'black')
        self.assertEqual(expected,actual, msg= "cxb3 capture should be allowed")

        #test forbidden enpassant: white f2-f4 > black g3xf2  (not 5th file)
        b.clean_pieces()
        b.initialize_single_piece('p', 'b', b.transform_board_to_grid('g', '3'))
        b.initialize_single_piece('p', 'w', b.transform_board_to_grid('f', '2'))
        b.piece_mover('p','f','4', 'white')
        i,j = b.transform_board_to_grid('f', '2')
        expected = False
        actual = b.Rules.is_pawn_eating_valid(b, i, j, b.pawns_b[0], 'black')
        self.assertEqual(expected,actual, msg= "gxf2 capture shouldn't be allowed")

        #test forbidden enpassant: white e2-e4 > black c4xe3 (not adjacent)
        b.clean_pieces()
        b.initialize_single_piece('p', 'b', b.transform_board_to_grid('c', '4'))
        b.initialize_single_piece('p', 'w', b.transform_board_to_grid('e', '2'))
        b.piece_mover('p','e','4', 'white')
        i,j = b.transform_board_to_grid('e', '3')
        expected = False
        actual = b.Rules.is_pawn_eating_valid(b, i, j, b.pawns_b[0], 'black')
        self.assertEqual(expected,actual, msg = "cxe3 capture shouldn't be allowed")

    def test_black_pawn_enpassant_eating_complex(self):
        b = cb.ChessBoard()
        b.clean_pieces()
        b.initialize_single_piece('r', 'b', b.transform_board_to_grid('c', '5'))
        b.initialize_single_piece('p', 'b', b.transform_board_to_grid('c', '4'))
        b.initialize_single_piece('r', 'w', b.transform_board_to_grid('d', '6'))
        b.initialize_single_piece('p', 'w', b.transform_board_to_grid('b', '2'))

        b.piece_mover('p','b','4', 'white')
        b.piece_mover('r','a','5', 'black')
        b.piece_mover('r','d','8', 'white')
        i,j = b.transform_board_to_grid('b', '3')
        actual = b.Rules.is_pawn_eating_valid(b, i, j, b.pawns_b[0], 'black')
        expected = False
        self.assertEqual(expected,actual, msg= "cxb3 capture should be forbidden (late capture)")

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


    # Test if moves are  correctly done
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

    def test_rook_movement(self):
        b = cb.ChessBoard()
        b_ref = cb.ChessBoard()

        # Test good move
        good_move = b.transform_grid_to_board(4, 6)
        b.clean_pieces()
        b.initialize_single_piece('r', 'b', [4, 4])
        b.piece_mover('r', good_move[0], good_move[1], 'black')

        b_ref.clean_pieces()
        b_ref.initialize_single_piece('r', 'b', [4, 6])

        expected = b_ref.color_augmented_grid()
        actual = b.color_augmented_grid()
        self.assertEqual(expected, actual)

        # Test bad move
        bad_move = b.transform_grid_to_board(5, 5)
        b.clean_pieces()
        b.initialize_single_piece('r', 'b', [4, 4])
        b.piece_mover('r', bad_move[0], bad_move[1], 'black')

        b_ref.clean_pieces()
        b_ref.initialize_single_piece('r', 'b', [4, 4])

        expected = b_ref.color_augmented_grid()
        actual = b.color_augmented_grid()
        self.assertEqual(expected, actual)

    def test_queen_movement(self):
        b = cb.ChessBoard()
        b_ref = cb.ChessBoard()

        # Test good move
        good_move = b.transform_grid_to_board(6, 6)
        b.clean_pieces()
        b.initialize_single_piece('q', 'b', [4, 4])
        b.piece_mover('q', good_move[0], good_move[1], 'black')

        b_ref.clean_pieces()
        b_ref.initialize_single_piece('q', 'b', [6, 6])

        expected = b_ref.color_augmented_grid()
        actual = b.color_augmented_grid()
        self.assertEqual(expected, actual)

        # Test bad move
        bad_move = b.transform_grid_to_board(7, 5)
        b.clean_pieces()
        b.initialize_single_piece('q', 'b', [4, 4])
        b.piece_mover('q', bad_move[0], bad_move[1], 'black')

        b_ref.clean_pieces()
        b_ref.initialize_single_piece('q', 'b', [4, 4])

        expected = b_ref.color_augmented_grid()
        actual = b.color_augmented_grid()
        self.assertEqual(expected, actual)

    def test_king_movement(self):
        b = cb.ChessBoard()
        b_ref = cb.ChessBoard()

        # Test good move
        good_move = b.transform_grid_to_board(5, 4)
        b.clean_pieces()
        b.initialize_single_piece('k', 'b', [4, 4])
        b.piece_mover('k', good_move[0], good_move[1], 'black')

        b_ref.clean_pieces()
        b_ref.initialize_single_piece('k', 'b', [5, 4])

        expected = b_ref.color_augmented_grid()
        actual = b.color_augmented_grid()
        self.assertEqual(expected, actual)

        # Test bad move
        bad_move = b.transform_grid_to_board(7, 5)
        b.clean_pieces()
        b.initialize_single_piece('k', 'b', [4, 4])
        b.piece_mover('k', bad_move[0], bad_move[1], 'black')

        b_ref.clean_pieces()
        b_ref.initialize_single_piece('k', 'b', [4, 4])

        expected = b_ref.color_augmented_grid()
        actual = b.color_augmented_grid()
        self.assertEqual(expected, actual)

    def test_bishop_movement(self):
        b = cb.ChessBoard()
        b_ref = cb.ChessBoard()
        b.clean_pieces()
        b_ref.clean_pieces()
        # Test good bishop move
        b.initialize_single_piece('b', 'b', [ 4, 4])
        move  = b.transform_grid_to_board(5,5)
        b.piece_mover('b',move[0],move[1], 'black')
        b_ref.initialize_single_piece('b', 'b', [5, 5])
        # assert good bishop move
        expected = b_ref.color_augmented_grid()
        actual = b.color_augmented_grid()
        self.assertEqual(expected, actual)
        
        # Test bad bishop move
        b = cb.ChessBoard()
        b_ref = cb.ChessBoard()
        b.clean_pieces()
        b_ref.clean_pieces()
        b.initialize_single_piece('b', 'b', [ 4, 4])
        move  = b.transform_grid_to_board(5,4)
        b.piece_mover('b',move[0],move[1], 'black')
        b_ref.initialize_single_piece('b', 'b', [4, 4])
        # assert bad bishop move
        expected = b_ref.color_augmented_grid()
        actual = b.color_augmented_grid()
        self.assertEqual(expected, actual)

    def test_white_pawn_movement(self):
        b = cb.ChessBoard()
        b_ref = cb.ChessBoard()
        b.clean_pieces()
        b_ref.clean_pieces()
        
        # Test good move 'white' pawn
        b.initialize_single_piece('p', 'w', [ 4, 4])
        move  = b.transform_grid_to_board(3,4)
        b.piece_mover('p',move[0],move[1], 'white')
        b_ref.initialize_single_piece('p', 'w', [3, 4])

        # assert wpm
        expected = b_ref.color_augmented_grid()
        actual = b.color_augmented_grid()
        self.assertEqual(expected, actual)

        # Test good move 'white' pawn
        b.clean_pieces()
        b_ref.clean_pieces()
        b.initialize_single_piece('p', 'w', [ 4, 4])
        move  = b.transform_grid_to_board(2,4)
        b.piece_mover('p',move[0],move[1], 'white')
        b_ref.initialize_single_piece('p', 'w', [4, 4])

        # assert bad pm
        expected = b_ref.color_augmented_grid()
        actual = b.color_augmented_grid()
        self.assertEqual(expected, actual)

    def test_black_pawn_movement(self):
        b = cb.ChessBoard()
        b_ref = cb.ChessBoard()
        b.clean_pieces()
        b_ref.clean_pieces()

        # Test good move 'black' pawn
        b.initialize_single_piece('p', 'b', [ 4, 4])
        move  = b.transform_grid_to_board(5,4)
        b.piece_mover('p',move[0],move[1], 'black')
        b_ref.initialize_single_piece('p', 'b', [5, 4])

        #assert black pawn good move
        expected = b_ref.color_augmented_grid()
        actual = b.color_augmented_grid()
        self.assertEqual(expected, actual)

        # Test bad move 'white' pawn
        b.clean_pieces()
        b_ref.clean_pieces()
        b.initialize_single_piece('p', 'b', [ 4, 4])
        move  = b.transform_grid_to_board( 6,4)
        b.piece_mover('p',move[0],move[1], 'black')
        b_ref.initialize_single_piece('p', 'b', [4, 4])

        #assert black pawn bad move
        expected = b_ref.color_augmented_grid()
        actual = b.color_augmented_grid()
        self.assertEqual(expected, actual)

    # Test if captures are correctly done

    def test_white_knight_capture(self):
        b = cb.ChessBoard()
        b.clean_pieces()
        b_ref = cb.ChessBoard()
        b_ref.clean_pieces()
        # allowed capture
        b.initialize_single_piece('n', 'w',b.transform_board_to_grid('e','4') )
        b.initialize_single_piece('p', 'b',b.transform_board_to_grid('f','6') )
        b.piece_eater('n','f','6', 'white')
        b_ref.initialize_single_piece('n', 'w', b.transform_board_to_grid('f','6') )

        expected = b_ref.color_augmented_grid()
        actual = b.color_augmented_grid()
        self.assertEqual(expected, actual, msg ='should capture enemy')

        #forbidden capture 1 ()
        b.clean_pieces()
        b_ref.clean_pieces()
        b.initialize_single_piece('n', 'w',b.transform_board_to_grid('e','4') )
        b.initialize_single_piece('p', 'w',b.transform_board_to_grid('f','6') )
        b.piece_eater('n','f','6', 'white')
        b_ref.initialize_single_piece('n', 'w',b.transform_board_to_grid('e','4') )
        b_ref.initialize_single_piece('p', 'w',b.transform_board_to_grid('f','6') )

        expected = b_ref.color_augmented_grid()
        actual = b.color_augmented_grid()
        self.assertEqual(expected, actual, msg= "shouldn't capture teamate ")

        #forbidden capture 2 ()
        b.clean_pieces()
        b_ref.clean_pieces()
        b.initialize_single_piece('n', 'w',b.transform_board_to_grid('e','4') )
        b.initialize_single_piece('b', 'b',b.transform_board_to_grid('g','6') )
        b.piece_eater('n','g','6', 'white')
        b_ref.initialize_single_piece('n', 'w',b.transform_board_to_grid('e','4') )
        b_ref.initialize_single_piece('b', 'b',b.transform_board_to_grid('g','6') )

        expected = b_ref.color_augmented_grid()
        actual = b.color_augmented_grid()
        self.assertEqual(expected, actual, msg =  "shouldn't capture after forbidden move")

    def test_white_bishop_capture(self):
        b = cb.ChessBoard()
        b.clean_pieces()
        b_ref = cb.ChessBoard()
        b_ref.clean_pieces()
        # allowed capture
        b.initialize_single_piece('b', 'w',b.transform_board_to_grid('d','4') )
        b.initialize_single_piece('p', 'b',b.transform_board_to_grid('g','7') )
        b.piece_eater('b','g','7', 'white')
        b_ref.initialize_single_piece('b', 'w', b.transform_board_to_grid('g','7') )

        expected = b_ref.color_augmented_grid()
        actual = b.color_augmented_grid()
        self.assertEqual(expected, actual, msg =  'should capture enemy')

        #forbidden capture 1 
        b.clean_pieces()
        b_ref.clean_pieces()
        b.initialize_single_piece('b', 'w',b.transform_board_to_grid('d','4') )
        b.initialize_single_piece('q', 'w',b.transform_board_to_grid('c','3') )
        b.piece_eater('b','c','3', 'white')
        b_ref.initialize_single_piece('b', 'w',b.transform_board_to_grid('d','4') )
        b_ref.initialize_single_piece('q', 'w',b.transform_board_to_grid('c','3') )

        expected = b_ref.color_augmented_grid()
        actual = b.color_augmented_grid()
        self.assertEqual(expected, actual, msg= "shouldn't capture teamate ")

        #forbidden capture 2
        b.clean_pieces()
        b_ref.clean_pieces()
        b.initialize_single_piece('b', 'w',b.transform_board_to_grid('d','4') )
        b.initialize_single_piece('b', 'b',b.transform_board_to_grid('d','5') )
        b.piece_eater('b','d','5', 'white')
        b_ref.initialize_single_piece('b', 'w',b.transform_board_to_grid('d','4') )
        b_ref.initialize_single_piece('b', 'b',b.transform_board_to_grid('d','5') )

        expected = b_ref.color_augmented_grid()
        actual = b.color_augmented_grid()
        self.assertEqual(expected, actual, msg =  "shouldn't capture after forbidden move")

    def test_white_rook_capture(self):
        b = cb.ChessBoard()
        b.clean_pieces()
        b_ref = cb.ChessBoard()
        b_ref.clean_pieces()
        # allowed capture
        b.initialize_single_piece('r', 'w',b.transform_board_to_grid('c','4') )
        b.initialize_single_piece('p', 'b',b.transform_board_to_grid('c','8') )
        b.piece_eater('r','c','8', 'white')
        b_ref.initialize_single_piece('r', 'w', b.transform_board_to_grid('c','8') )

        expected = b_ref.color_augmented_grid()
        actual = b.color_augmented_grid()
        self.assertEqual(expected, actual, msg =  'should capture enemy')

        #forbidden capture 1 
        b.clean_pieces()
        b_ref.clean_pieces()
        b.initialize_single_piece('r', 'w',b.transform_board_to_grid('c','4') )
        b.initialize_single_piece('q', 'w',b.transform_board_to_grid('c','3') )
        b.piece_eater('r','c','3', 'white')
        b_ref.initialize_single_piece('r', 'w',b.transform_board_to_grid('c','4') )
        b_ref.initialize_single_piece('q', 'w',b.transform_board_to_grid('c','3') )

        expected = b_ref.color_augmented_grid()
        actual = b.color_augmented_grid()
        self.assertEqual(expected, actual, msg= "shouldn't capture teamate ")

        #forbidden capture 2
        b.clean_pieces()
        b_ref.clean_pieces()
        b.initialize_single_piece('r', 'w',b.transform_board_to_grid('c','4') )
        b.initialize_single_piece('b', 'b',b.transform_board_to_grid('d','5') )
        b.piece_eater('r','d','5', 'white')
        b_ref.initialize_single_piece('r', 'w',b.transform_board_to_grid('c','4') )
        b_ref.initialize_single_piece('b', 'b',b.transform_board_to_grid('d','5') )

        expected = b_ref.color_augmented_grid()
        actual = b.color_augmented_grid()
        self.assertEqual(expected, actual, msg =  "shouldn't capture after forbidden move")

    def test_white_queen_capture(self):
        b = cb.ChessBoard()
        b.clean_pieces()
        b_ref = cb.ChessBoard()
        b_ref.clean_pieces()
        # allowed capture
        b.initialize_single_piece('q', 'w',b.transform_board_to_grid('d','5') )
        b.initialize_single_piece('p', 'b',b.transform_board_to_grid('b','3') )
        b.piece_eater('q','b','3', 'white')
        b_ref.initialize_single_piece('q', 'w', b.transform_board_to_grid('b','3') )

        expected = b_ref.color_augmented_grid()
        actual = b.color_augmented_grid()
        self.assertEqual(expected, actual, msg = 'should capture enemy')

        #forbidden capture 1 
        b.clean_pieces()
        b_ref.clean_pieces()
        b.initialize_single_piece('q', 'w',b.transform_board_to_grid('d','5') )
        b.initialize_single_piece('q', 'w',b.transform_board_to_grid('d','3') )
        b.piece_eater('q','d','3', 'white')
        b_ref.initialize_single_piece('q', 'w',b.transform_board_to_grid('d','5') )
        b_ref.initialize_single_piece('q', 'w',b.transform_board_to_grid('d','3') )

        expected = b_ref.color_augmented_grid()
        actual = b.color_augmented_grid()
        self.assertEqual(expected, actual, msg= "shouldn't capture teamate ")

        #forbidden capture 2
        b.clean_pieces()
        b_ref.clean_pieces()
        b.initialize_single_piece('q', 'w',b.transform_board_to_grid('d','5') )
        b.initialize_single_piece('b', 'b',b.transform_board_to_grid('e','7') )
        b.piece_eater('q','e','7', 'white')
        b_ref.initialize_single_piece('q', 'w',b.transform_board_to_grid('d','5') )
        b_ref.initialize_single_piece('b', 'b',b.transform_board_to_grid('e','7') )

        expected = b_ref.color_augmented_grid()
        actual = b.color_augmented_grid()
        self.assertEqual(expected, actual, msg =  "shouldn't capture after forbidden move")

    def test_white_king_capture(self):
        b = cb.ChessBoard()
        b.clean_pieces()
        b_ref = cb.ChessBoard()
        b_ref.clean_pieces()
        # allowed capture
        b.initialize_single_piece('k', 'w',b.transform_board_to_grid('g','7') )
        b.initialize_single_piece('p', 'b',b.transform_board_to_grid('f','6') )
        b.piece_eater('k','f','6', 'white')
        b_ref.initialize_single_piece('k', 'w', b.transform_board_to_grid('f','6') )

        expected = b_ref.color_augmented_grid()
        actual = b.color_augmented_grid()
        self.assertEqual(expected, actual, msg = 'should capture enemy')

        #forbidden capture 1 
        b.clean_pieces()
        b_ref.clean_pieces()
        b.initialize_single_piece('k', 'w',b.transform_board_to_grid('g','7') )
        b.initialize_single_piece('q', 'w',b.transform_board_to_grid('h','7') )
        b.piece_eater('k','h','7', 'white')
        b_ref.initialize_single_piece('k', 'w',b.transform_board_to_grid('g','7') )
        b_ref.initialize_single_piece('q', 'w',b.transform_board_to_grid('h','7') )

        expected = b_ref.color_augmented_grid()
        actual = b.color_augmented_grid()
        self.assertEqual(expected, actual, msg= "shouldn't capture teamate ")

        #forbidden capture 2
        b.clean_pieces()
        b_ref.clean_pieces()
        b.initialize_single_piece('k', 'w',b.transform_board_to_grid('g','7') )
        b.initialize_single_piece('b', 'b',b.transform_board_to_grid('g','5') )
        b.piece_eater('k','g','5', 'white')
        b_ref.initialize_single_piece('k', 'w',b.transform_board_to_grid('g','7') )
        b_ref.initialize_single_piece('b', 'b',b.transform_board_to_grid('g','5') )

        expected = b_ref.color_augmented_grid()
        actual = b.color_augmented_grid()
        self.assertEqual(expected, actual, msg =  "shouldn't capture after forbidden move")

    def test_white_pawn_capture(self):
        b = cb.ChessBoard()
        b.clean_pieces()
        b_ref = cb.ChessBoard()
        b_ref.clean_pieces()

        # allowed capture
        b.initialize_single_piece('p', 'w',b.transform_board_to_grid('b','2') )
        b.initialize_single_piece('q', 'b',b.transform_board_to_grid('c','3') )
        b.piece_eater('p','c','3', 'white')
        b_ref.initialize_single_piece('p', 'w', b.transform_board_to_grid('c','3') )
 
        expected = b_ref.color_augmented_grid()
        actual = b.color_augmented_grid()
        self.assertEqual(expected, actual, msg = 'should capture enemy')

        #forbidden capture 1 
        b.clean_pieces()
        b_ref.clean_pieces()
        b.initialize_single_piece('p', 'w',b.transform_board_to_grid('b','2') )
        b.initialize_single_piece('q', 'w',b.transform_board_to_grid('a','3') )
        b.piece_eater('p','a','3', 'white')
        b_ref.initialize_single_piece('p', 'w',b.transform_board_to_grid('b','2') )
        b_ref.initialize_single_piece('q', 'w',b.transform_board_to_grid('a','3') )

        expected = b_ref.color_augmented_grid()
        actual = b.color_augmented_grid()
        self.assertEqual(expected, actual, msg= "shouldn't capture teamate ")

        #forbidden capture 2
        b.clean_pieces()
        b_ref.clean_pieces()
        b.initialize_single_piece('p', 'w',b.transform_board_to_grid('b','3') )
        b.initialize_single_piece('p', 'b',b.transform_board_to_grid('b','4') )
        b.piece_eater('p','b','4', 'white')
        b_ref.initialize_single_piece('p', 'w',b.transform_board_to_grid('b','3') )
        b_ref.initialize_single_piece('p', 'b',b.transform_board_to_grid('b','4') )

        expected = b_ref.color_augmented_grid()
        actual = b.color_augmented_grid()
        self.assertEqual(expected, actual, msg =  "shouldn't capture after forbidden move")

        #accepted  capture en passant
        b.clean_pieces()
        b_ref.clean_pieces()
        b.initialize_single_piece('p', 'w',b.transform_board_to_grid('b','5') )
        b.initialize_single_piece('p', 'b',b.transform_board_to_grid('c','7') )
        b.piece_mover('p','c','5', 'black')
        b.piece_eater('p','c','6', 'white')
        b_ref.initialize_single_piece('p', 'w',b.transform_board_to_grid('c','6') )

        expected = b_ref.color_augmented_grid()
        actual = b.color_augmented_grid()
        self.assertEqual(expected, actual, msg= "should capture en passant ")

    def test_black_pawn_capture(self):
        b = cb.ChessBoard()
        b.clean_pieces()
        b_ref = cb.ChessBoard()
        b_ref.clean_pieces()
        # allowed capture
        b.initialize_single_piece('p', 'b',b.transform_board_to_grid('c','6') )
        b.initialize_single_piece('b', 'w',b.transform_board_to_grid('d','5') )
        b.piece_eater('p','d','5', 'black')
        b_ref.initialize_single_piece('p', 'b', b.transform_board_to_grid('d','5') )
        expected = b_ref.color_augmented_grid()
        actual = b.color_augmented_grid()
        self.assertEqual(expected, actual, msg = 'should capture enemy')

        #forbidden capture 1
        b.clean_pieces()
        b_ref.clean_pieces()
        b.initialize_single_piece('p', 'b',b.transform_board_to_grid('c','6') )
        b.initialize_single_piece('q', 'b',b.transform_board_to_grid('b','5') )
        b.piece_eater('p','b','5', 'black')
        b_ref.initialize_single_piece('p', 'b',b.transform_board_to_grid('c','6') )
        b_ref.initialize_single_piece('q', 'b',b.transform_board_to_grid('b','5') )

        expected = b_ref.color_augmented_grid()
        actual = b.color_augmented_grid()
        self.assertEqual(expected, actual, msg= "shouldn't capture teamate ")

        #forbidden capture 2
        b.clean_pieces()
        b_ref.clean_pieces()
        b.initialize_single_piece('p', 'b',b.transform_board_to_grid('c','6') )
        b.initialize_single_piece('b', 'w',b.transform_board_to_grid('d','6') )
        b.piece_eater('p','d','6', 'black')
        b_ref.initialize_single_piece('p', 'b',b.transform_board_to_grid('c','6') )
        b_ref.initialize_single_piece('b', 'w',b.transform_board_to_grid('d','6') )

        expected = b_ref.color_augmented_grid()
        actual = b.color_augmented_grid()
        self.assertEqual(expected, actual, msg =  "shouldn't capture after forbidden move")

        #accepted  capture en passant
        b.clean_pieces()
        b_ref.clean_pieces()
        b.initialize_single_piece('p', 'b',b.transform_board_to_grid('c','4') )
        b.initialize_single_piece('p', 'w',b.transform_board_to_grid('b','2') )
        b.piece_mover('p','b','4', 'white')
        b.piece_eater('p','b','3', 'black')
        b_ref.initialize_single_piece('p', 'b',b.transform_board_to_grid('b','3') )

        expected = b_ref.color_augmented_grid()
        actual = b.color_augmented_grid()
        self.assertEqual(expected, actual, msg= "should capture en passant ")

    def test_promote(self):
        # accepted white
        b = cb.ChessBoard()
        b.clean_pieces()
        b_ref = cb.ChessBoard()
        b_ref.clean_pieces()

        b.initialize_single_piece('p', 'w', b.transform_board_to_grid('c','8') )
        b.promote('c','8','white', 'Q')
        b_ref.initialize_single_piece('q','w',b.transform_board_to_grid('c','8'))

        expected = b_ref.color_augmented_grid()
        actual = b.color_augmented_grid()
        self.assertEqual(expected, actual, msg= "should promote white pawn to a queen in (c,8) ")

        # accepted black
        b = cb.ChessBoard()
        b.clean_pieces()
        b_ref = cb.ChessBoard()
        b_ref.clean_pieces()

        b.initialize_single_piece('p', 'b',b.transform_board_to_grid('d','1') )
        b.promote('d','1','black', 'N')
        b_ref.initialize_single_piece('n','b',b.transform_board_to_grid('d','1'))

        expected = b_ref.color_augmented_grid()
        actual = b.color_augmented_grid()
        self.assertEqual(expected, actual, msg= "should promote balck pawn to a knight in (d,1) ")

        # forbidden white
        b = cb.ChessBoard()
        b.clean_pieces()
        b_ref = cb.ChessBoard()
        b_ref.clean_pieces()

        bad_configs = [ ( 'c','8', 'q', 'black', 'Q'), 
                        ( 'c','7', 'q', 'white', 'Q'),
                        ( 'd','1', 'q', 'white', 'Q')]

        for col,line,kind, color , promote_to in bad_configs:
            b.initialize_single_piece( 'p', 'w', b.transform_board_to_grid(col,line) )
            b.promote(col,line,color, promote_to)
            b_ref.initialize_single_piece( 'p','w',b.transform_board_to_grid(col,line) )

        expected = b_ref.color_augmented_grid()
        actual = b.color_augmented_grid()
        self.assertEqual(expected, actual, msg= "white pawn should not be promoted, %s"%line)

        # forbidden black
        b = cb.ChessBoard()
        b.clean_pieces()
        b_ref = cb.ChessBoard()
        b_ref.clean_pieces()

        bad_configs = [ ( 'd','1', 'q', 'white', 'Q'), 
                        ( 'd','2', 'q', 'black', 'Q'),
                        ( 'd','8', 'q', 'black', 'Q')]

        for col,line,kind, color , promote_to in bad_configs:
            b.initialize_single_piece( 'p', 'w', b.transform_board_to_grid(col,line) )
            b.promote(col,line,color, promote_to)
            b_ref.initialize_single_piece( 'p','w',b.transform_board_to_grid(col,line) )

        expected = b_ref.color_augmented_grid()
        actual = b.color_augmented_grid()
        self.assertEqual(expected, actual, msg= "white pawn should not be promoted, %s"%line)

    def test_is_square_under_attack(self):
        b = cb.ChessBoard()
        b.clean_pieces()

        # Test black and white attacks on empty square
        b.initialize_single_piece('b', 'b', b.transform_board_to_grid('f', '7'))
        b.initialize_single_piece('n', 'w', b.transform_board_to_grid('c', '3'))

        ## Square actually under attack
        square_coords = b.transform_board_to_grid('d', '5')

        expected = True
        actual_black_attack = b.Rules.is_square_under_attack(b, square_coords[0], square_coords[1], 'black')
        actual_white_attack = b.Rules.is_square_under_attack(b, square_coords[0], square_coords[1], 'white')
        self.assertEqual(expected, actual_black_attack, msg="'d5' is under attack by black bishop in 'f7'")
        self.assertEqual(expected, actual_white_attack, msg="'d5' is under attack by white knight in 'c3'")

        ## Square actually under attack
        square_coords = b.transform_board_to_grid('c', '5')

        expected = False
        actual_black_attack = b.Rules.is_square_under_attack(b, square_coords[0], square_coords[1], 'black')
        actual_white_attack = b.Rules.is_square_under_attack(b, square_coords[0], square_coords[1], 'white')
        self.assertEqual(expected, actual_black_attack, msg="'c5' is not under attack by any black piece")
        self.assertEqual(expected, actual_white_attack, msg="'c5' is not under attack by any white piece")

        # Test black and white attacks on occupied square

        ## Attacked square occupied by white piece
        b.clean_pieces()

        b.initialize_single_piece('b', 'b', b.transform_board_to_grid('f', '7'))
        b.initialize_single_piece('n', 'w', b.transform_board_to_grid('c', '3'))
        b.initialize_single_piece('p', 'w', b.transform_board_to_grid('d', '5'))
        square_coords = b.transform_board_to_grid('d', '5')

        expected_black_attack = True
        actual_black_attack = b.Rules.is_square_under_attack(b, square_coords[0], square_coords[1], 'black')

        expected_white_attack = False
        actual_white_attack = b.Rules.is_square_under_attack(b, square_coords[0], square_coords[1], 'white')

        self.assertEqual(expected_black_attack, actual_black_attack, msg="white pawn in 'd5' is under attack by black bishop in 'f7'")
        self.assertEqual(expected_white_attack, actual_white_attack, msg="white pawn in 'd5' is not under attack by white knight in 'c3'")

        ## Attacked square occupied by black piece
        b.clean_pieces()

        b.initialize_single_piece('b', 'b', b.transform_board_to_grid('f', '7'))
        b.initialize_single_piece('n', 'w', b.transform_board_to_grid('c', '3'))
        b.initialize_single_piece('p', 'b', b.transform_board_to_grid('d', '5'))
        square_coords = b.transform_board_to_grid('d', '5')

        expected_black_attack = False
        actual_black_attack = b.Rules.is_square_under_attack(b, square_coords[0], square_coords[1], 'black')

        expected_white_attack = True
        actual_white_attack = b.Rules.is_square_under_attack(b, square_coords[0], square_coords[1], 'white')

        self.assertEqual(expected_black_attack, actual_black_attack, msg="black pawn in 'd5' is not under attack by black bishop in 'f7'")
        self.assertEqual(expected_white_attack, actual_white_attack, msg="black pawn in 'd5' is under attack by white knight in 'c3'")

        ## Not attacked square occupied by white piece
        b.clean_pieces()

        b.initialize_single_piece('b', 'b', b.transform_board_to_grid('f', '7'))
        b.initialize_single_piece('n', 'w', b.transform_board_to_grid('c', '3'))
        b.initialize_single_piece('p', 'w', b.transform_board_to_grid('c', '5'))
        square_coords = b.transform_board_to_grid('c', '5')

        expected_black_attack = False
        actual_black_attack = b.Rules.is_square_under_attack(b, square_coords[0], square_coords[1], 'black')

        expected_white_attack = False
        actual_white_attack = b.Rules.is_square_under_attack(b, square_coords[0], square_coords[1], 'white')

        self.assertEqual(expected_black_attack, actual_black_attack, msg="white pawn in 'd5' is not under attack by black bishop in 'f7'")
        self.assertEqual(expected_white_attack, actual_white_attack, msg="white pawn in 'd5' is not under attack by white knight in 'c3'")

        ## Not attacked square occupied by black piece
        b.clean_pieces()

        b.initialize_single_piece('b', 'b', b.transform_board_to_grid('f', '7'))
        b.initialize_single_piece('n', 'w', b.transform_board_to_grid('c', '3'))
        b.initialize_single_piece('p', 'b', b.transform_board_to_grid('c', '5'))
        square_coords = b.transform_board_to_grid('c', '5')

        expected_black_attack = False
        actual_black_attack = b.Rules.is_square_under_attack(b, square_coords[0], square_coords[1], 'black')

        expected_white_attack = False
        actual_white_attack = b.Rules.is_square_under_attack(b, square_coords[0], square_coords[1], 'white')

        self.assertEqual(expected_black_attack, actual_black_attack, msg="black pawn in 'd5' is not under attack by black bishop in 'f7'")
        self.assertEqual(expected_white_attack, actual_white_attack, msg="black pawn in 'd5' is not under attack by white knight in 'c3'")


# Test if suicidal movement are blocked

    def test_blocked_white_king_suicidal_movement(self):
        b = cb.ChessBoard()
        b_ref = cb.ChessBoard()
        b.clean_pieces()
        b_ref.clean_pieces()

        # Test approved movement
        b.initialize_single_piece('k', 'w', b.transform_board_to_grid('d', '3'))
        b.initialize_single_piece('q', 'b', b.transform_board_to_grid('e', '6'))

        b.piece_mover('k', 'c', '4', 'white')
        b_ref.initialize_single_piece('k', 'w', b_ref.transform_board_to_grid('c', '4'))
        b_ref.initialize_single_piece('q', 'b', b_ref.transform_board_to_grid('e', '6'))

        expected = b_ref.color_augmented_grid()
        actual = b.color_augmented_grid()

        self.assertEqual(expected, actual, msg = "The white king should be allowed to go to 'c4'")

        # Test non approved movement
        b.clean_pieces()
        b_ref.clean_pieces()

        b.initialize_single_piece('k', 'w', b.transform_board_to_grid('d', '3'))
        b.initialize_single_piece('q', 'b', b.transform_board_to_grid('e', '6'))

        b.piece_mover('k', 'e', '4', 'white')
        b_ref.initialize_single_piece('k', 'w', b_ref.transform_board_to_grid('d', '3'))
        b_ref.initialize_single_piece('q', 'b', b_ref.transform_board_to_grid('e', '6'))

        expected = b_ref.color_augmented_grid()
        actual = b.color_augmented_grid()

        self.assertEqual(expected, actual, msg = "The white king should not be allowed to go to 'e4'")

    def test_blocked_black_king_suicidal_movement(self):
        b = cb.ChessBoard()
        b_ref = cb.ChessBoard()
        b.clean_pieces()
        b_ref.clean_pieces()

        # Test approved movement
        b.initialize_single_piece('k', 'b', b.transform_board_to_grid('d', '3'))
        b.initialize_single_piece('q', 'w', b.transform_board_to_grid('e', '6'))

        b.piece_mover('k', 'c', '4', 'black')
        b_ref.initialize_single_piece('k', 'b', b_ref.transform_board_to_grid('c', '4'))
        b_ref.initialize_single_piece('q', 'w', b_ref.transform_board_to_grid('e', '6'))

        expected = b_ref.color_augmented_grid()
        actual = b.color_augmented_grid()

        self.assertEqual(expected, actual, msg = "The black king should be allowed to go to 'c4'")

        # Test non approved movement
        b.clean_pieces()
        b_ref.clean_pieces()

        b.initialize_single_piece('k', 'b', b.transform_board_to_grid('d', '3'))
        b.initialize_single_piece('q', 'w', b.transform_board_to_grid('e', '6'))

        b.piece_mover('k', 'e', '4', 'black')
        b_ref.initialize_single_piece('k', 'b', b_ref.transform_board_to_grid('d', '3'))
        b_ref.initialize_single_piece('q', 'w', b_ref.transform_board_to_grid('e', '6'))

        expected = b_ref.color_augmented_grid()
        actual = b.color_augmented_grid()

        self.assertEqual(expected, actual, msg = "The black king should not be allowed to go to 'e4'")

    def test_blocked_white_treason_movement(self):
        b = cb.ChessBoard()
        b_ref = cb.ChessBoard()
        b.clean_pieces()
        b_ref.clean_pieces()

        # Test valid protecting piece movement
        b.initialize_single_piece('k', 'w', b.transform_board_to_grid('d', '3'))
        b.initialize_single_piece('b', 'w', b.transform_board_to_grid('f', '5'))
        b.initialize_single_piece('q', 'b', b.transform_board_to_grid('h', '7'))

        b.piece_mover('b', 'g', '6', 'white')

        b_ref.initialize_single_piece('k', 'w', b_ref.transform_board_to_grid('d', '3'))
        b_ref.initialize_single_piece('b', 'w', b_ref.transform_board_to_grid('g', '6'))
        b_ref.initialize_single_piece('q', 'b', b_ref.transform_board_to_grid('h', '7'))

        expected = b_ref.color_augmented_grid()
        actual = b.color_augmented_grid()

        self.assertEqual(expected, actual, msg="White bishop should be allowed to go to 'g6'")

        # Test invalid protecting piece treason
        b.clean_pieces()
        b_ref.clean_pieces()
        b.initialize_single_piece('k', 'w', b.transform_board_to_grid('d', '3'))
        b.initialize_single_piece('b', 'w', b.transform_board_to_grid('f', '5'))
        b.initialize_single_piece('q', 'b', b.transform_board_to_grid('h', '7'))

        b.piece_mover('b', 'h', '3', 'white')

        b_ref.initialize_single_piece('k', 'w', b_ref.transform_board_to_grid('d', '3'))
        b_ref.initialize_single_piece('b', 'w', b_ref.transform_board_to_grid('f', '5'))
        b_ref.initialize_single_piece('q', 'b', b_ref.transform_board_to_grid('h', '7'))

        expected = b_ref.color_augmented_grid()
        actual = b.color_augmented_grid()

        self.assertEqual(expected, actual, msg="White bishop should not be allowed to go to 'h3'")

    def test_blocked_black_treason_movement(self):
        b = cb.ChessBoard()
        b_ref = cb.ChessBoard()
        b.clean_pieces()
        b_ref.clean_pieces()

        # Test valid protecting piece movement
        b.initialize_single_piece('k', 'b', b.transform_board_to_grid('d', '3'))
        b.initialize_single_piece('b', 'b', b.transform_board_to_grid('f', '5'))
        b.initialize_single_piece('q', 'w', b.transform_board_to_grid('h', '7'))

        b.piece_mover('b', 'g', '6', 'black')

        b_ref.initialize_single_piece('k', 'b', b_ref.transform_board_to_grid('d', '3'))
        b_ref.initialize_single_piece('b', 'b', b_ref.transform_board_to_grid('g', '6'))
        b_ref.initialize_single_piece('q', 'w', b_ref.transform_board_to_grid('h', '7'))

        expected = b_ref.color_augmented_grid()
        actual = b.color_augmented_grid()

        self.assertEqual(expected, actual, msg="Black bishop should be allowed to go to 'g6'")

        # Test invalid protecting piece treason
        b.clean_pieces()
        b_ref.clean_pieces()
        b.initialize_single_piece('k', 'b', b.transform_board_to_grid('d', '3'))
        b.initialize_single_piece('b', 'b', b.transform_board_to_grid('f', '5'))
        b.initialize_single_piece('q', 'w', b.transform_board_to_grid('h', '7'))

        b.piece_mover('b', 'h', '3', 'black')

        b_ref.initialize_single_piece('k', 'b', b_ref.transform_board_to_grid('d', '3'))
        b_ref.initialize_single_piece('b', 'b', b_ref.transform_board_to_grid('f', '5'))
        b_ref.initialize_single_piece('q', 'w', b_ref.transform_board_to_grid('h', '7'))

        expected = b_ref.color_augmented_grid()
        actual = b.color_augmented_grid()

        self.assertEqual(expected, actual, msg="Black bishop should not be allowed to go to 'h3'")

    def test_white_king_out_of_check_movement(self):
        b = cb.ChessBoard()
        b_ref = cb.ChessBoard()
        b.clean_pieces()
        b_ref.clean_pieces()

        # Test valid escape from single check
        b.initialize_single_piece('k', 'w', b.transform_board_to_grid('d', '3'))
        b.initialize_single_piece('q', 'b', b.transform_board_to_grid('g', '6'))

        b.piece_mover('k', 'd', '4', 'white')

        b_ref.initialize_single_piece('k', 'w', b_ref.transform_board_to_grid('d', '4'))
        b_ref.initialize_single_piece('q', 'b', b_ref.transform_board_to_grid('g', '6'))

        expected = b_ref.color_augmented_grid()
        actual = b.color_augmented_grid()

        self.assertEqual(expected, actual, msg="White king should be allowed to escape to 'd4'")

        # Test valid escape plan by protecting piece
        b.clean_pieces()
        b_ref.clean_pieces()

        b.initialize_single_piece('k', 'w', b.transform_board_to_grid('d', '3'))
        b.initialize_single_piece('b', 'w', b.transform_board_to_grid('d', '7'))
        b.initialize_single_piece('q', 'b', b.transform_board_to_grid('g', '6'))

        b.piece_mover('b', 'f', '5', 'white')

        b_ref.initialize_single_piece('k', 'w', b_ref.transform_board_to_grid('d', '3'))
        b_ref.initialize_single_piece('b', 'w', b_ref.transform_board_to_grid('f', '5'))
        b_ref.initialize_single_piece('q', 'b', b_ref.transform_board_to_grid('g', '6'))

        expected = b_ref.color_augmented_grid()
        actual = b.color_augmented_grid()
        self.assertEqual(expected, actual, msg="The sacrifice of the white bishop to 'f5' saves the king")

        # Test invalid escape from single check
        b.clean_pieces()
        b_ref.clean_pieces()
        b.initialize_single_piece('k', 'w', b.transform_board_to_grid('d', '3'))
        b.initialize_single_piece('q', 'b', b.transform_board_to_grid('g', '6'))

        b.piece_mover('k', 'c', '2', 'white')

        b_ref.initialize_single_piece('k', 'w', b_ref.transform_board_to_grid('d', '3'))
        b_ref.initialize_single_piece('q', 'b', b_ref.transform_board_to_grid('g', '6'))

        expected = b_ref.color_augmented_grid()
        actual = b.color_augmented_grid()

        self.assertEqual(expected, actual, msg="White king should not be allowed to escape to 'c2'")

        # Test invalid from one check to another
        b.clean_pieces()
        b_ref.clean_pieces()

        b.initialize_single_piece('k', 'w', b.transform_board_to_grid('d', '3'))
        b.initialize_single_piece('q', 'b', b.transform_board_to_grid('g', '6'))
        b.initialize_single_piece('r', 'b', b.transform_board_to_grid('a', '4'))

        b.piece_mover('k', 'd', '4', 'white')

        b_ref.initialize_single_piece('k', 'w', b_ref.transform_board_to_grid('d', '3'))
        b_ref.initialize_single_piece('q', 'b', b_ref.transform_board_to_grid('g', '6'))
        b_ref.initialize_single_piece('r', 'b', b_ref.transform_board_to_grid('a', '4'))

        expected = b_ref.color_augmented_grid()
        actual = b.color_augmented_grid()

        self.assertEqual(expected, actual, msg="White king should not be allowed to escape to 'd4', he is under attack by a rook")

        # Test invalid escape plan by protecting piece
        b.clean_pieces()
        b_ref.clean_pieces()

        b.initialize_single_piece('k', 'w', b.transform_board_to_grid('d', '3'))
        b.initialize_single_piece('b', 'w', b.transform_board_to_grid('d', '7'))
        b.initialize_single_piece('q', 'b', b.transform_board_to_grid('g', '6'))
        b.initialize_single_piece('r', 'b', b.transform_board_to_grid('d', '8'))

        b.piece_mover('b', 'f', '5', 'white')

        b_ref.initialize_single_piece('k', 'w', b_ref.transform_board_to_grid('d', '3'))
        b_ref.initialize_single_piece('b', 'w', b_ref.transform_board_to_grid('d', '7'))
        b_ref.initialize_single_piece('q', 'b', b_ref.transform_board_to_grid('g', '6'))
        b_ref.initialize_single_piece('r', 'b', b_ref.transform_board_to_grid('d', '8'))

        expected = b_ref.color_augmented_grid()
        actual = b.color_augmented_grid()
        self.assertEqual(expected, actual, msg="The sacrifice of the white bishop to 'f5' is not enough")

# Test castling

    def test_white_king_short_castling_rules(self):
        b = cb.ChessBoard()
        ## Test castling with no opposing pieces

        # No one has moved
        b.clean_pieces()
        b.initialize_single_piece('k', 'w', b.transform_board_to_grid('e', '1'))
        b.initialize_single_piece('r', 'w', b.transform_board_to_grid('h', '1'))
        expected = True
        actual = b.Rules.is_king_castling_valid(b, 'white', 'short')
        self.assertEqual(expected, actual, msg="Short castling should be valid")

        # The king moved
        b.clean_pieces()
        b.initialize_single_piece('k', 'w', b.transform_board_to_grid('e', '1'))
        b.initialize_single_piece('r', 'w', b.transform_board_to_grid('h', '1'))

        b.piece_mover('k', 'f', '1', 'white')
        b.piece_mover('k', 'e', '1', 'white')

        expected = False
        actual = b.Rules.is_king_castling_valid(b, 'white', 'short')
        self.assertEqual(expected, actual, msg="The king has already moved")

        # The rook moved
        b.clean_pieces()
        b.initialize_single_piece('k', 'w', b.transform_board_to_grid('e', '1'))
        b.initialize_single_piece('r', 'w', b.transform_board_to_grid('h', '1'))

        b.piece_mover('r', 'h', '2', 'white')
        b.piece_mover('r', 'h', '1', 'white')

        expected = False
        actual = b.Rules.is_king_castling_valid(b, 'white', 'short')
        self.assertEqual(expected, actual, msg="The rook has already moved")

        # No one has moved but there's a blocking piece
        b.clean_pieces()
        b.initialize_single_piece('k', 'w', b.transform_board_to_grid('e', '1'))
        b.initialize_single_piece('r', 'w', b.transform_board_to_grid('h', '1'))
        b.initialize_single_piece('n', 'w', b.transform_board_to_grid('g', '1'))

        expected = False
        actual = b.Rules.is_king_castling_valid(b, 'white', 'short')
        self.assertEqual(expected, actual, msg="The castling is blocked by knight in 'g1'")

        ## Test castling with opposing pieces
        # King under attack
        b.clean_pieces()
        b.initialize_single_piece('k', 'w', b.transform_board_to_grid('e', '1'))
        b.initialize_single_piece('r', 'w', b.transform_board_to_grid('h', '1'))
        b.initialize_single_piece('q', 'b', b.transform_board_to_grid('g', '3'))

        expected = False
        actual = b.Rules.is_king_castling_valid(b, 'white', 'short')
        self.assertEqual(expected, actual, msg="White king under attack by black queen in 'g3'")

        # 'f1' under attack
        b.clean_pieces()
        b.initialize_single_piece('k', 'w', b.transform_board_to_grid('e', '1'))
        b.initialize_single_piece('r', 'w', b.transform_board_to_grid('h', '1'))
        b.initialize_single_piece('q', 'b', b.transform_board_to_grid('h', '3'))

        expected = False
        actual = b.Rules.is_king_castling_valid(b, 'white', 'short')
        self.assertEqual(expected, actual, msg="'f1' under attack by black queen in 'h3'")

        # 'g1' under attack
        b.clean_pieces()
        b.initialize_single_piece('k', 'w', b.transform_board_to_grid('e', '1'))
        b.initialize_single_piece('r', 'w', b.transform_board_to_grid('h', '1'))
        b.initialize_single_piece('r', 'b', b.transform_board_to_grid('g', '3'))

        expected = False
        actual = b.Rules.is_king_castling_valid(b, 'white', 'short')
        self.assertEqual(expected, actual, msg="'g1' under attack by black rook in 'g3'")

        # 'h1' under attack
        b.clean_pieces()
        b.initialize_single_piece('k', 'w', b.transform_board_to_grid('e', '1'))
        b.initialize_single_piece('r', 'w', b.transform_board_to_grid('h', '1'))
        b.initialize_single_piece('r', 'b', b.transform_board_to_grid('h', '3'))

        expected = False
        actual = b.Rules.is_king_castling_valid(b, 'white', 'short')
        self.assertEqual(expected, actual, msg="'h1' under attack by black rook in 'h3'")

        # Opposing pieces but path protected by white pawns
        b.clean_pieces()
        b.initialize_single_piece('k', 'w', b.transform_board_to_grid('e', '1'))
        b.initialize_single_piece('r', 'w', b.transform_board_to_grid('h', '1'))

        b.initialize_single_piece('p', 'w', b.transform_board_to_grid('f', '2'))
        b.initialize_single_piece('p', 'w', b.transform_board_to_grid('g', '2'))
        b.initialize_single_piece('p', 'w', b.transform_board_to_grid('h', '2'))

        b.initialize_single_piece('r', 'b', b.transform_board_to_grid('f', '3'))
        b.initialize_single_piece('q', 'b', b.transform_board_to_grid('g', '3'))
        b.initialize_single_piece('r', 'b', b.transform_board_to_grid('h', '3'))

        expected = True
        actual = b.Rules.is_king_castling_valid(b, 'white', 'short')
        self.assertEqual(expected, actual, msg="Path is protected by loyal pawns, castling should be valid")

    def test_white_king_long_castling_rules(self):
        b = cb.ChessBoard()
        b.clean_pieces()

        ## Test castling with no opposing pieces
        # No one has moved
        b.clean_pieces()
        b.initialize_single_piece('k', 'w', b.transform_board_to_grid('e', '1'))
        b.initialize_single_piece('r', 'w', b.transform_board_to_grid('a', '1'))

        expected = True
        actual = b.Rules.is_king_castling_valid(b, 'white', 'long')
        self.assertEqual(expected, actual, msg="Long castling should be valid")

        # The king moved
        b.clean_pieces()
        b.initialize_single_piece('k', 'w', b.transform_board_to_grid('e', '1'))
        b.initialize_single_piece('r', 'w', b.transform_board_to_grid('a', '1'))

        b.piece_mover('k', 'f', '1', 'white')
        b.piece_mover('k', 'e', '1', 'white')

        expected = False
        actual = b.Rules.is_king_castling_valid(b, 'white', 'long')
        self.assertEqual(expected, actual, msg="the king has already moved")

        # The rook moved
        b.clean_pieces()
        b.initialize_single_piece('k', 'w', b.transform_board_to_grid('e', '1'))
        b.initialize_single_piece('r', 'w', b.transform_board_to_grid('a', '1'))

        b.piece_mover('r', 'a', '2', 'white')
        b.piece_mover('k', 'a', '1', 'white')

        expected = False
        actual = b.Rules.is_king_castling_valid(b, 'white', 'long')
        self.assertEqual(expected, actual, msg="the rook has already moved")

        # No one has moved but there is a blocking piece
        b.clean_pieces()
        b.initialize_single_piece('k', 'w', b.transform_board_to_grid('e', '1'))
        b.initialize_single_piece('r', 'w', b.transform_board_to_grid('a', '1'))
        b.initialize_single_piece('b', 'w', b.transform_board_to_grid('c', '1'))

        expected = False
        actual = b.Rules.is_king_castling_valid(b, 'white', 'long')
        self.assertEqual(expected, actual, msg="Castling is blocked by bishop in 'c1'")

        ## Test castling with opposing pieces
        # king under attack
        b.clean_pieces()
        b.initialize_single_piece('k', 'w', b.transform_board_to_grid('e', '1'))
        b.initialize_single_piece('r', 'w', b.transform_board_to_grid('a', '1'))

        b.initialize_single_piece('r', 'b', b.transform_board_to_grid('e', '3'))

        expected = False
        actual = b.Rules.is_king_castling_valid(b, 'white', 'long')
        self.assertEqual(expected, actual, msg="White king under attack by black rook in 'e3'")

        # 'd1' under attack
        b.clean_pieces()
        b.initialize_single_piece('k', 'w', b.transform_board_to_grid('e', '1'))
        b.initialize_single_piece('r', 'w', b.transform_board_to_grid('a', '1'))

        b.initialize_single_piece('r', 'b', b.transform_board_to_grid('d', '3'))

        expected = False
        actual = b.Rules.is_king_castling_valid(b, 'white', 'long')
        self.assertEqual(expected, actual, msg="'d1' under attack by black rook in 'd3'")

        # 'c1' under attack
        b.clean_pieces()
        b.initialize_single_piece('k', 'w', b.transform_board_to_grid('e', '1'))
        b.initialize_single_piece('r', 'w', b.transform_board_to_grid('a', '1'))

        b.initialize_single_piece('r', 'b', b.transform_board_to_grid('c', '3'))

        expected = False
        actual = b.Rules.is_king_castling_valid(b, 'white', 'long')
        self.assertEqual(expected, actual, msg="'c1' under attack by black rook in 'c3'")

        # 'b1' under attack
        b.clean_pieces()
        b.initialize_single_piece('k', 'w', b.transform_board_to_grid('e', '1'))
        b.initialize_single_piece('r', 'w', b.transform_board_to_grid('a', '1'))

        b.initialize_single_piece('r', 'b', b.transform_board_to_grid('b', '3'))

        expected = False
        actual = b.Rules.is_king_castling_valid(b, 'white', 'long')
        self.assertEqual(expected, actual, msg="'b1' under attack by black rook in 'b3'")

        # 'b1' under attack
        b.clean_pieces()
        b.initialize_single_piece('k', 'w', b.transform_board_to_grid('e', '1'))
        b.initialize_single_piece('r', 'w', b.transform_board_to_grid('a', '1'))

        b.initialize_single_piece('r', 'b', b.transform_board_to_grid('a', '3'))

        expected = False
        actual = b.Rules.is_king_castling_valid(b, 'white', 'long')
        self.assertEqual(expected, actual, msg="'a1' under attack by black rook in 'a3'")

        # opposing pieces but path protected by loyal pawns
        b.clean_pieces()
        b.initialize_single_piece('k', 'w', b.transform_board_to_grid('e', '1'))
        b.initialize_single_piece('r', 'w', b.transform_board_to_grid('a', '1'))

        b.initialize_single_piece('r', 'b', b.transform_board_to_grid('a', '3'))
        b.initialize_single_piece('r', 'b', b.transform_board_to_grid('b', '3'))
        b.initialize_single_piece('r', 'b', b.transform_board_to_grid('c', '3'))
        b.initialize_single_piece('r', 'b', b.transform_board_to_grid('d', '3'))
        b.initialize_single_piece('r', 'b', b.transform_board_to_grid('e', '3'))

        b.initialize_single_piece('p', 'w', b.transform_board_to_grid('a', '2'))
        b.initialize_single_piece('p', 'w', b.transform_board_to_grid('b', '2'))
        b.initialize_single_piece('p', 'w', b.transform_board_to_grid('c', '2'))
        b.initialize_single_piece('p', 'w', b.transform_board_to_grid('d', '2'))
        b.initialize_single_piece('p', 'w', b.transform_board_to_grid('e', '2'))

        expected = True
        actual = b.Rules.is_king_castling_valid(b, 'white', 'long')
        self.assertEqual(expected, actual, msg="Castling should be valid, path protected by pawns")

    def test_black_king_short_castling_rules(self):
        b = cb.ChessBoard()
        ## Test castling with no opposing pieces

        # No one has moved
        b.clean_pieces()
        b.initialize_single_piece('k', 'b', b.transform_board_to_grid('e', '8'))
        b.initialize_single_piece('r', 'b', b.transform_board_to_grid('h', '8'))
        expected = True
        actual = b.Rules.is_king_castling_valid(b, 'black', 'short')
        self.assertEqual(expected, actual, msg="Short castling should be valid")

        # The king moved
        b.clean_pieces()
        b.initialize_single_piece('k', 'b', b.transform_board_to_grid('e', '8'))
        b.initialize_single_piece('r', 'b', b.transform_board_to_grid('h', '8'))

        b.piece_mover('k', 'f', '8', 'black')
        b.piece_mover('k', 'e', '8', 'black')

        expected = False
        actual = b.Rules.is_king_castling_valid(b, 'black', 'short')
        self.assertEqual(expected, actual, msg="The king has already moved")

        # The rook moved
        b.clean_pieces()
        b.initialize_single_piece('k', 'b', b.transform_board_to_grid('e', '8'))
        b.initialize_single_piece('r', 'b', b.transform_board_to_grid('h', '8'))

        b.piece_mover('r', 'h', '7', 'black')
        b.piece_mover('r', 'h', '8', 'black')

        expected = False
        actual = b.Rules.is_king_castling_valid(b, 'black', 'short')
        self.assertEqual(expected, actual, msg="The rook has already moved")

        # No one has moved but there's a blocking piece
        b.clean_pieces()
        b.initialize_single_piece('k', 'b', b.transform_board_to_grid('e', '8'))
        b.initialize_single_piece('r', 'b', b.transform_board_to_grid('h', '8'))
        b.initialize_single_piece('n', 'b', b.transform_board_to_grid('g', '8'))

        expected = False
        actual = b.Rules.is_king_castling_valid(b, 'black', 'short')
        self.assertEqual(expected, actual, msg="The castling is blocked by knight in 'g8'")

        ## Test castling with opposing pieces
        # King under attack
        b.clean_pieces()
        b.initialize_single_piece('k', 'b', b.transform_board_to_grid('e', '8'))
        b.initialize_single_piece('r', 'b', b.transform_board_to_grid('h', '8'))
        b.initialize_single_piece('q', 'w', b.transform_board_to_grid('g', '6'))

        expected = False
        actual = b.Rules.is_king_castling_valid(b, 'black', 'short')
        self.assertEqual(expected, actual, msg="black king under attack by white queen in 'g6'")

        # 'f8' under attack
        b.clean_pieces()
        b.initialize_single_piece('k', 'b', b.transform_board_to_grid('e', '8'))
        b.initialize_single_piece('r', 'b', b.transform_board_to_grid('h', '8'))
        b.initialize_single_piece('q', 'w', b.transform_board_to_grid('h', '6'))

        expected = False
        actual = b.Rules.is_king_castling_valid(b, 'black', 'short')
        self.assertEqual(expected, actual, msg="'f8' under attack by white queen in 'h6'")

        # 'g8' under attack
        b.clean_pieces()
        b.initialize_single_piece('k', 'b', b.transform_board_to_grid('e', '8'))
        b.initialize_single_piece('r', 'b', b.transform_board_to_grid('h', '8'))
        b.initialize_single_piece('r', 'w', b.transform_board_to_grid('g', '6'))

        expected = False
        actual = b.Rules.is_king_castling_valid(b, 'black', 'short')
        self.assertEqual(expected, actual, msg="'g8' under attack by white rook in 'g6'")

        # 'h8' under attack
        b.clean_pieces()
        b.initialize_single_piece('k', 'b', b.transform_board_to_grid('e', '8'))
        b.initialize_single_piece('r', 'b', b.transform_board_to_grid('h', '8'))
        b.initialize_single_piece('r', 'w', b.transform_board_to_grid('h', '6'))

        expected = False
        actual = b.Rules.is_king_castling_valid(b, 'black', 'short')
        self.assertEqual(expected, actual, msg="'h8' under attack by white rook in 'h6'")

        # Opposing pieces but path protected by white pawns
        b.clean_pieces()
        b.initialize_single_piece('k', 'b', b.transform_board_to_grid('e', '8'))
        b.initialize_single_piece('r', 'b', b.transform_board_to_grid('h', '8'))

        b.initialize_single_piece('p', 'b', b.transform_board_to_grid('f', '7'))
        b.initialize_single_piece('p', 'b', b.transform_board_to_grid('g', '7'))
        b.initialize_single_piece('p', 'b', b.transform_board_to_grid('h', '7'))

        b.initialize_single_piece('r', 'w', b.transform_board_to_grid('f', '6'))
        b.initialize_single_piece('q', 'w', b.transform_board_to_grid('g', '6'))
        b.initialize_single_piece('r', 'w', b.transform_board_to_grid('h', '6'))

        expected = True
        actual = b.Rules.is_king_castling_valid(b, 'black', 'short')
        self.assertEqual(expected, actual, msg="Path is protected by loyal pawns, castling should be valid")

    def test_black_king_long_castling_rules(self):
        b = cb.ChessBoard()
        b.clean_pieces()

        ## Test castling with no opposing pieces
        # No one has moved
        b.clean_pieces()
        b.initialize_single_piece('k', 'b', b.transform_board_to_grid('e', '8'))
        b.initialize_single_piece('r', 'b', b.transform_board_to_grid('a', '8'))

        expected = True
        actual = b.Rules.is_king_castling_valid(b, 'black', 'long')
        self.assertEqual(expected, actual, msg="Long castling should be valid")

        # The king moved
        b.clean_pieces()
        b.initialize_single_piece('k', 'b', b.transform_board_to_grid('e', '8'))
        b.initialize_single_piece('r', 'b', b.transform_board_to_grid('a', '8'))

        b.piece_mover('k', 'f', '8', 'black')
        b.piece_mover('k', 'e', '8', 'black')

        expected = False
        actual = b.Rules.is_king_castling_valid(b, 'black', 'long')
        self.assertEqual(expected, actual, msg="the king has already moved")

        # The rook moved
        b.clean_pieces()
        b.initialize_single_piece('k', 'b', b.transform_board_to_grid('e', '8'))
        b.initialize_single_piece('r', 'b', b.transform_board_to_grid('a', '8'))

        b.piece_mover('r', 'a', '6', 'black')
        b.piece_mover('k', 'a', '8', 'black')

        expected = False
        actual = b.Rules.is_king_castling_valid(b, 'black', 'long')
        self.assertEqual(expected, actual, msg="the rook has already moved")

        # No one has moved but there is a blocking piece
        b.clean_pieces()
        b.initialize_single_piece('k', 'b', b.transform_board_to_grid('e', '8'))
        b.initialize_single_piece('r', 'b', b.transform_board_to_grid('a', '8'))
        b.initialize_single_piece('b', 'b', b.transform_board_to_grid('c', '8'))

        expected = False
        actual = b.Rules.is_king_castling_valid(b, 'black', 'long')
        self.assertEqual(expected, actual, msg="Castling is blocked by bishop in 'c8'")

        ## Test castling with opposing pieces
        # king under attack
        b.clean_pieces()
        b.initialize_single_piece('k', 'b', b.transform_board_to_grid('e', '8'))
        b.initialize_single_piece('r', 'b', b.transform_board_to_grid('a', '8'))

        b.initialize_single_piece('r', 'w', b.transform_board_to_grid('e', '6'))

        expected = False
        actual = b.Rules.is_king_castling_valid(b, 'black', 'long')
        self.assertEqual(expected, actual, msg="Black king under attack by black rook in 'e6'")

        # 'd8' under attack
        b.clean_pieces()
        b.initialize_single_piece('k', 'b', b.transform_board_to_grid('e', '8'))
        b.initialize_single_piece('r', 'b', b.transform_board_to_grid('a', '8'))

        b.initialize_single_piece('r', 'w', b.transform_board_to_grid('d', '6'))

        expected = False
        actual = b.Rules.is_king_castling_valid(b, 'black', 'long')
        self.assertEqual(expected, actual, msg="'d8' under attack by white rook in 'd6'")

        # 'c8' under attack
        b.clean_pieces()
        b.initialize_single_piece('k', 'b', b.transform_board_to_grid('e', '8'))
        b.initialize_single_piece('r', 'b', b.transform_board_to_grid('a', '8'))

        b.initialize_single_piece('r', 'w', b.transform_board_to_grid('c', '6'))

        expected = False
        actual = b.Rules.is_king_castling_valid(b, 'black', 'long')
        self.assertEqual(expected, actual, msg="'c8' under attack by white rook in 'c6'")

        # 'b8' under attack
        b.clean_pieces()
        b.initialize_single_piece('k', 'b', b.transform_board_to_grid('e', '8'))
        b.initialize_single_piece('r', 'b', b.transform_board_to_grid('a', '8'))

        b.initialize_single_piece('r', 'w', b.transform_board_to_grid('b', '6'))

        expected = False
        actual = b.Rules.is_king_castling_valid(b, 'black', 'long')
        self.assertEqual(expected, actual, msg="'b8' under attack by white rook in 'b6'")

        # 'a8' under attack
        b.clean_pieces()
        b.initialize_single_piece('k', 'b', b.transform_board_to_grid('e', '8'))
        b.initialize_single_piece('r', 'b', b.transform_board_to_grid('a', '8'))

        b.initialize_single_piece('r', 'w', b.transform_board_to_grid('a', '6'))

        expected = False
        actual = b.Rules.is_king_castling_valid(b, 'black', 'long')
        self.assertEqual(expected, actual, msg="'a8' under attack by white rook in 'a6'")

        # opposing pieces but path protected by loyal pawns
        b.clean_pieces()
        b.initialize_single_piece('k', 'b', b.transform_board_to_grid('e', '8'))
        b.initialize_single_piece('r', 'b', b.transform_board_to_grid('a', '8'))

        b.initialize_single_piece('r', 'w', b.transform_board_to_grid('a', '6'))
        b.initialize_single_piece('r', 'w', b.transform_board_to_grid('b', '6'))
        b.initialize_single_piece('r', 'w', b.transform_board_to_grid('c', '6'))
        b.initialize_single_piece('r', 'w', b.transform_board_to_grid('d', '6'))
        b.initialize_single_piece('r', 'w', b.transform_board_to_grid('e', '6'))

        b.initialize_single_piece('p', 'b', b.transform_board_to_grid('a', '7'))
        b.initialize_single_piece('p', 'b', b.transform_board_to_grid('b', '7'))
        b.initialize_single_piece('p', 'b', b.transform_board_to_grid('c', '7'))
        b.initialize_single_piece('p', 'b', b.transform_board_to_grid('d', '7'))
        b.initialize_single_piece('p', 'b', b.transform_board_to_grid('e', '7'))

        expected = True
        actual = b.Rules.is_king_castling_valid(b, 'black', 'long')
        self.assertEqual(expected, actual, msg="Castling should be valid, path protected by pawns")













        

if __name__ == '__main__':
    unittest.main()






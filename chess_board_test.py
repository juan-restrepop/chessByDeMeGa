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


    def test_initialize_single_pawn(self):
        b = cb.ChessBoard()

        ## Initialization of single white pawn
        b.clean_pieces()
        b.initialize_single_piece('p', 'w', [6, 0])

        # Test if initialization of only 1 piece
        expected = 1
        actual = len(b.get_all_pieces())
        self.assertEqual(expected, actual)

        # Test if initialized piece is a white pawn
        expected = True
        actual = len(b.pawns_w) == 1
        self.assertEqual(expected, actual)

        # Test if initialized white pawn in the right position
        expected = True
        actual = b.pawns_w[0].coordinates == [6, 0]
        self.assertEqual(expected, actual)

        ## Initialization of single black pawn
        b.clean_pieces()
        b.initialize_single_piece('p', 'b', [1, 0])

        # Test if initialization of only 1 piece
        expected = 1
        actual = len(b.get_all_pieces())
        self.assertEqual(expected, actual)

        # Test if initialized piece is a black pawn
        expected = True
        actual = len(b.pawns_b) == 1
        self.assertEqual(expected, actual)

        # Test if initialized black pawn in the right position
        expected = True
        actual = b.pawns_b[0].coordinates == [1, 0]
        self.assertEqual(expected, actual)

    def test_initialize_single_rook(self):
        b = cb.ChessBoard()

        ## Test initialize single white rook
        b.clean_pieces()
        b.initialize_single_piece('r', 'w', [3,3])

        # Test if initialization of only 1 piece
        expected = 1
        actual = len(b.get_all_pieces())
        self.assertEqual(expected, actual)

        # Test if initialized piece is a white rook
        expected = True
        actual = len(b.rooks_w) == 1
        self.assertEqual(expected, actual)

        # Test if initialized white rook in the right position
        expected = True
        actual = b.rooks_w[0].coordinates == [3, 3]
        self.assertEqual(expected, actual)

        ## Test initialize single black rook
        b.clean_pieces()
        b.initialize_single_piece('r', 'b', [2, 2])

        # Test if initialization of only 1 piece
        expected = 1
        actual = len(b.get_all_pieces())
        self.assertEqual(expected, actual)

        # Test if initialized piece is a black rook
        expected = True
        actual = len(b.rooks_b) == 1
        self.assertEqual(expected, actual)

        # Test if initialized white rook in the right position
        expected = True
        actual = b.rooks_b[0].coordinates == [2, 2]
        self.assertEqual(expected, actual)

    def test_initialize_single_queen(self):
        b = cb.ChessBoard()

        ## Initialization of single white queen
        b.clean_pieces()
        b.initialize_single_piece('q', 'w', [3, 4])


        # Test if initialization of only 1 piece
        expected = 1
        actual = len(b.get_all_pieces())
        self.assertEqual(expected, actual)

        # Test if initialized piece is a white queen
        expected = True
        actual = len(b.queen_w) == 1
        self.assertEqual(expected, actual)

        # Test if initialized white queen in the right position
        expected = True
        actual = b.queen_w[0].coordinates == [3, 4]
        self.assertEqual(expected, actual)

        ## Initialization of single black queen
        b.clean_pieces()
        b.initialize_single_piece('q', 'b', [4, 3])

        # Test if initialization of only 1 piece
        expected = 1
        actual = len(b.get_all_pieces())
        self.assertEqual(expected, actual)

        # Test if initialized piece is a black queen
        expected = True
        actual = len(b.queen_b) == 1
        self.assertEqual(expected, actual)

        # Test if initialized black queen in the right position
        expected = True
        actual = b.queen_b[0].coordinates == [4, 3]
        self.assertEqual(expected, actual)

    def test_initialize_single_king(self):
        b = cb.ChessBoard()

        ## Initialization of a single white king
        b.clean_pieces()
        b.initialize_single_piece('k', 'w', [3,5])

        # Test if initialization of only 1 piece
        expected = True
        actual = len(b.get_all_pieces()) == 1
        self.assertEqual(expected, actual)

        # Test if initialized piece is a white king
        expected = True
        actual = len(b.king_w) == 1
        self.assertEqual(expected, actual)

        # Test if white king initialized in the right position
        expected = True
        actual = b.king_w[0].coordinates == [3, 5]
        self.assertEqual(expected, actual)

        ## Initialization of a single black king
        b.clean_pieces()
        b.initialize_single_piece('k', 'b', [5, 3])

        # Test if initialization of only 1 piece
        expected = True
        actual = len(b.get_all_pieces()) == 1
        self.assertEqual(expected, actual)

        # Test if initialized piece is a black king
        expected = True
        actual = len(b.king_b) == 1
        self.assertEqual(expected, actual)

        # Test if black king in the right position
        expected = True
        actual = b.king_b[0].coordinates == [5, 3]
        self.assertEqual(expected, actual)

    def test_initialize_single_bishop(self):
        b = cb.ChessBoard()

        ## Initialization of single white bishop
        b.clean_pieces()
        b.initialize_single_piece('b', 'w', [2, 5])

        # Test if initialization of only 1 piece
        expected = 1
        actual = len(b.get_all_pieces())
        self.assertEqual(expected, actual)

        # Test if initialized piece is a white bishop
        expected = True
        actual = len(b.bishops_w) == 1
        self.assertEqual(expected, actual)

        # Test if white bishop in the right position
        expected = True
        actual = b.bishops_w[0].coordinates == [2, 5]
        self.assertEqual(expected, actual)

        ## Initialization of single black bishop
        b.clean_pieces()
        b.initialize_single_piece('b', 'b', [5, 2])

        # Test if initialization of only 1 piece
        expected = 1
        actual = len(b.get_all_pieces())
        self.assertEqual(expected, actual)

        # Test if initialized piece is a black bishop
        actual = len(b.bishops_b) == 1
        self.assertEqual(expected, actual)

        # Test if black bishop in the right position
        expected = True
        actual = b.bishops_b[0].coordinates == [5, 2]
        self.assertEqual(expected, actual)

    def test_initialize_single_knight(self):
        b = cb.ChessBoard()

        # Initialization of single white knight
        b.clean_pieces()
        b.initialize_single_piece('n', 'w', [7,2])
        # Test for pieces length
        expected = 1
        actual = len(b.get_all_pieces())
        self.assertEqual(expected, actual)
        # Test for  white knights length
        expected = True
        actual = len(b.knights_w) == 1
        self.assertEqual(expected, actual)
        # Test for white knights coordinates
        expected = True
        actual = b.knights_w[0].coordinates == [7, 2]
        self.assertEqual(expected, actual)

        b.clean_pieces()
        # Initialization of single black knight
        b.clean_pieces()
        b.initialize_single_piece('n', 'b', [2,7])
        # Test for pieces length
        expected = 1
        actual = len(b.get_all_pieces())
        self.assertEqual(expected, actual)
        # Test for black knights length
        expected = True
        actual = len(b.knights_b) == 1
        self.assertEqual(expected, actual)
        # Test for black knights coordinates
        expected = True
        actual = b.knights_b[0].coordinates == [2, 7]
        self.assertEqual(expected, actual)


    def test_white_pawn_movement(self):
        b = cb.ChessBoard()

        ## Initialize white pawn on 'd2'
        b.clean_pieces()
        b.initialize_single_piece('p', 'w', [6, 3])

        ## Test forbidden moves
        # Test forbidden forward-diagonal moves
        expected = False
        for move in [['e','3'], ['c','3']]:
            actual = b.move_pawn_to(move[0], move[1])
            self.assertEqual(expected, actual)

        # Test forbidden lateral moves
        expected = False
        for move in [['e','2'], ['c','2']]:
            actual = b.move_pawn_to(move[0], move[1])
            self.assertEqual(expected, actual)

        # Test forbidden backwards moves
        expected = False
        for move in [['e','1'], ['c','3'], ['d', '1']]:
            actual = b.move_pawn_to(move[0], move[1])
            self.assertEqual(expected, actual)

        # Test forbidden forward move longer than 2
        expected = False
        actual = b.move_pawn_to('d', '5')
        self.assertEqual(expected, actual)

        ## Test approved moves if initial position
        # simple initial move
        b.clean_pieces()
        b.initialize_single_piece('p', 'w', [6, 3])

        expected = True
        actual = b.move_pawn_to('d','3')
        self.assertEqual(expected, actual)

        # double initial move
        b.clean_pieces()
        b.initialize_single_piece('p', 'w', [6, 3])

        expected = True
        actual = b.move_pawn_to('d','4')
        self.assertEqual(expected, actual)

        ## Test approved moves
        # simple move
        b.clean_pieces()
        b.initialize_single_piece('p', 'w', [4, 3])

        expected = True
        actual = b.move_pawn_to('d','5')
        self.assertEqual(expected, actual)

        # double move
        b.clean_pieces()
        b.initialize_single_piece('p', 'w', [4, 3])

        expected = False
        actual = b.move_pawn_to('d','6')
        self.assertEqual(expected, actual)

    def test_white_pawn_blocked_movement(self):
        b = cb.ChessBoard()

        ## Initialize white pawn on 'd2' and black knight on 'd3'
        b.clean_pieces()
        b.initialize_single_piece('p', 'w', [6, 3])
        b.initialize_single_piece('n', 'b', [5, 3])

        expected = False
        actual = b.move_pawn_to('d', '3')
        self.assertEqual(expected, actual)

        ## Initialize white pawn on 'd2' and black knight on 'd3'
        b.clean_pieces()
        b.initialize_single_piece('p', 'w', [6, 3])
        b.initialize_single_piece('n', 'b', [5, 3])

        expected = False
        actual = b.move_pawn_to('d', '4')

    def test_white_knight_movement(self):
        b = cb.ChessBoard()

        # test forbidden moves
        b.clean_pieces()
        b.initialize_single_piece('n', 'w', [4, 3])

        expected = False
        for move in [['d', '3'], ['d','5'], \
                        ['c', '4'], ['e', '4'], \
                        ['c', '5'], ['e', '5'], ['c', '3'], ['e', '3']]:
            actual = b.move_knight_to(move[0], move[1])
            self.assertEqual(expected, actual)

        #test approved moves
        expected = True

        for move in [['b', '5'], ['f', '5'], \
                     ['b', '3'], ['f', '3'], \
                     ['c', '6'], ['e', '6'], \
                     ['c', '2'], ['e', '2']]:
            b.clean_pieces()
            b.initialize_single_piece('n', 'w', [4, 3])

            actual = b.move_knight_to(move[0], move[1])
            self.assertEqual(expected, actual)




if __name__ == '__main__':
    unittest.main()






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

        # Initialization of single white pawn
        b.clean_pieces()
        b.initialize_single_piece('p', 'w', [6, 0])

        expected = 1
        actual = len(b.get_all_pieces())
        self.assertEqual(expected, actual)

        expected = True
        actual = len(b.pawns_w) == 1
        self.assertEqual(expected, actual)

        expected = True
        actual = b.pawns_w[0].coordinates == [6, 0]
        self.assertEqual(expected, actual)

        # Initialization of single black pawn
        b.clean_pieces()
        b.initialize_single_piece('p', 'b', [1, 0])

        expected = 1
        actual = len(b.get_all_pieces())
        self.assertEqual(expected, actual)

        expected = True
        actual = len(b.pawns_b) == 1
        self.assertEqual(expected, actual)

        expected = True
        actual = b.pawns_b[0].coordinates == [1, 0]
        self.assertEqual(expected, actual)

    def test_initialize_single_rook(self):
        b = cb.ChessBoard()

        # Test initialize single white rook
        b.clean_pieces()
        b.initialize_single_piece('r', 'w', [3,3])

        expected = 1
        actual = len(b.get_all_pieces())
        self.assertEqual(expected, actual)

        expected = True
        actual = len(b.rooks_w) == 1
        self.assertEqual(expected, actual)

        expected = True
        actual = b.rooks_w[0].coordinates == [3, 3]
        self.assertEqual(expected, actual)

        # Test initialize single black rook
        b.clean_pieces()
        b.initialize_single_piece('r', 'b', [2, 2])

        expected = 1
        actual = len(b.get_all_pieces())
        self.assertEqual(expected, actual)

        expected = True
        actual = len(b.rooks_b) == 1
        self.assertEqual(expected, actual)

        expected = True
        actual = b.rooks_b[0].coordinates == [2, 2]
        self.assertEqual(expected, actual)


    def test_initialize_single_queen(self):
        b = cb.ChessBoard()

        # Initialization of single white queen
        b.clean_pieces()
        b.initialize_single_piece('q', 'w', [3, 4])

        expected = 1
        actual = len(b.get_all_pieces())
        self.assertEqual(expected, actual)

        expected = True
        actual = len(b.queen_w) == 1
        self.assertEqual(expected, actual)

        expected = True
        actual = b.queen_w[0].coordinates == [3, 4]
        self.assertEqual(expected, actual)

        # Initialization of single black queen
        b.clean_pieces()
        b.initialize_single_piece('q', 'b', [4, 3])

        expected = 1
        actual = len(b.get_all_pieces())
        self.assertEqual(expected, actual)

        actual = len(b.queen_b) == 1
        self.assertEqual(expected, actual)

        expected = True
        actual = b.queen_b[0].coordinates == [4, 3]
        self.assertEqual(expected, actual)

    def test_initialize_single_bishop(self):
        b = cb.ChessBoard()

        # Initialization of single white bishop
        b.clean_pieces()
        b.initialize_single_piece('b', 'w', [2, 5])

        expected = 1
        actual = len(b.get_all_pieces())
        self.assertEqual(expected, actual)

        expected = True
        actual = len(b.bishops_w) == 1
        self.assertEqual(expected, actual)

        expected = True
        actual = b.bishops_w[0].coordinates == [2, 5]
        self.assertEqual(expected, actual)

        # Initialization of single black bishop
        b.clean_pieces()
        b.initialize_single_piece('b', 'b', [5, 2])

        expected = 1
        actual = len(b.get_all_pieces())
        self.assertEqual(expected, actual)

        actual = len(b.bishops_b) == 1
        self.assertEqual(expected, actual)

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



if __name__ == '__main__':
    unittest.main()






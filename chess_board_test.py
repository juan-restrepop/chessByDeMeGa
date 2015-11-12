import unittest
import chess_board as cb

class TestChessBoard(unittest.TestCase):
    
    def test_initialize_board_object(self):
        b = cb.ChessBoard()
        
        expected = 32
        actual = len(b.get_all_pieces())
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
        print "square test", len(b.get_all_pieces())

    def test_clean_pieces(self):
        b = cb.ChessBoard()

        expected = 0
        
        b.clean_pieces()
        actual = len(b.get_all_pieces())
        self.assertEqual(expected, actual)
        print "clean test", len(b.get_all_pieces())


    def test_initialize_single_piece(self):
        b = cb.ChessBoard()
        b.clean_pieces()


        expected = True
        actual = True
        self.assertEqual(expected, actual) 
        print "initialize test", len(b.get_all_pieces())  


if __name__ == '__main__':
    unittest.main()





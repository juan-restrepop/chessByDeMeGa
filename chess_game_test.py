import unittest
import chess_game as cg

class TestChessGame(unittest.TestCase):

    def test_has_quit(self):
        c  = cg.ChessGame()

        expected = True
        actual = c.has_quit('q')
        self.assertEqual(expected, actual)
        
        expected = False
        actual = c.has_quit('bla')
        self.assertEqual(expected, actual)

    def test_is_pawn(self):
        c  = cg.ChessGame()
        
        expected = True
        for col in c.column_names:
            
            actual = c.is_pawn(col +'1')
            self.assertEqual(expected, actual)

            actual = c.is_pawn(col + 'x1d')
            self.assertEqual(expected, actual)

        expected = False
        actual = c.is_pawn('B1')
        self.assertEqual(expected, actual)
        
        expected = False
        actual = c.is_pawn('Kx1')
        self.assertEqual(expected, actual)

    def test_is_main_piece(self):
        c  = cg.ChessGame()
        # basic case
        expected = True
        for piece in ['K','Q','N','B','R']:

            actual = c.is_main_piece(piece +'1')
            self.assertEqual(expected, actual)
        # real moves
        expected = True
        for input_move in ['Kf3','Bxa2','Rxd2']:

            actual = c.is_main_piece(piece +'x1')
            self.assertEqual(expected, actual)
        # wrong moves
        expected = False
        for input_move in ['q','axc1','b3']:

            actual = c.is_main_piece(input_move)
            self.assertEqual(expected, actual)



if __name__ == '__main__':
    unittest.main()
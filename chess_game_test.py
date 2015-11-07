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

if __name__ == '__main__':
    unittest.main()
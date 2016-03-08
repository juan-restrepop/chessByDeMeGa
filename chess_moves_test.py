import unittest

import utils
import chess_moves as cm

class TestMoves(unittest.TestCase):
    
    def test_is_check(self):
        expected = True
        test_cases = ['Bf5+','a6#']
        for input_move in test_cases:
            actual = cm.is_check(input_move)
            self.assertEqual(actual,expected)

    def test_is_promotion(self):
        expected = (True,'a8','Q')
        actual =  cm.is_promotion('a8=Q')
        self.assertEqual(expected,actual)

        expected = (False,'a8','')
        actual =  cm.is_promotion('a8')
        self.assertEqual(expected,actual)

    def test_is_pawn(self):
        expected = True
        for col in utils.COLUMN_NAMES:

            actual = cm.is_pawn(col +'1')
            self.assertEqual(expected, actual)

            actual = cm.is_pawn(col + 'x1d')
            self.assertEqual(expected, actual)

        expected = False
        actual = cm.is_pawn('B1')
        self.assertEqual(expected, actual)

        expected = False
        actual = cm.is_pawn('Kx1')
        self.assertEqual(expected, actual)

    def test_is_main_piece(self):
        # basic case
        expected = True
        for piece in ['K','Q','N','B','R']:

            actual = cm.is_main_piece(piece +'1')
            self.assertEqual(expected, actual)
        # real moves
        expected = True
        for input_move in ['Kf3','Bxa2','Rxd2']:

            actual = cm.is_main_piece(input_move)
            self.assertEqual(expected, actual)
        # wrong moves
        expected = False
        for input_move in ['q','axc1','b3']:
            actual = cm.is_main_piece(input_move)
            self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()

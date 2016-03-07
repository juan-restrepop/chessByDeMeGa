import unittest

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

if __name__ == '__main__':
    unittest.main()

""" input_parser_test.py """

import unittest
import input_parser

class TestInputParser(unittest.TestCase):

    def test_piece_eats(self):
        expected = True
        for input_move in ['Kxf3','axb2','Rxd2']:

            actual = input_parser.piece_eats(input_move)
            self.assertEqual(expected, actual)

        expected = False
        for input_move in ['a2','Bf3','q']:

            actual = input_parser.piece_eats(input_move)
            self.assertEqual(expected, actual)

    def test_parse_pawn_coordinates(self):
        expected = [('a','2', None, None),
                    ('b','2', None, None)]

        test_cases = ['a2','axb2']

        for k in range(len(test_cases)):
            input_move = test_cases[k]
            actual = input_parser.parse_pawn_coordinates(input_move)
            self.assertEqual(expected[k], actual)

if __name__ == '__main__':
    unittest.main()

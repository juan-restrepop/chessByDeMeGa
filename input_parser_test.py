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

    def test_parse_main_pieces_coordinates(self):
        expected = [('f','2', None, None),
                    ('b','3', None, None),
                    ('f','2', None, '3'),
                    ('g','4', 'a', None),
                    ('h','3', 'c', '3') ,
                    ('f','4', 'd', None), 
                    ('h','8', 'a', '1')]

        test_cases = ['Bf2','Qxb3', 'B3f2', 'Bag4', 'Rc3h3','Qdxf4', 'Qa1xh8' ]

        for k in range(len(test_cases)):
            input_move = test_cases[k]
            actual = input_parser.parse_main_pieces_coordinates(input_move)
            self.assertEqual(expected[k], actual)

if __name__ == '__main__':
    unittest.main()

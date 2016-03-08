""" chess_validator_test: tests for chess_validator  """

import unittest
import utils
import chess_validator as validator

class TestValidator(unittest.TestCase):

    def test_are_coordinates_valid(self):
        expected = True
        for coords in [('a', '1'), ('d', '5'), ('h', '8')]:
            actual = validator.are_coordinates_valid(coords[0], coords[1])
            self.assertEqual(expected, actual)

        expected = False
        for coords in [('a', '-1'), ('z', '5'), ('z', '17'), ('A', '5')]:
            actual = validator.are_coordinates_valid(coords[0], coords[1])
            self.assertEqual(expected, actual)

    def test_validate_move_case(self):
        expected = True
        for piece in ['K','Q','N','B','R']:
            actual = validator.validate_move_case(piece +'f3')
            self.assertEqual(expected, actual)

        expected = True
        for col in utils.COLUMN_NAMES:
            actual = validator.validate_move_case(col +'3')
            self.assertEqual(expected, actual)

        expected = False
        for piece in ['K','Q','N','B','R']:
            actual = validator.validate_move_case(piece +'3')
            self.assertEqual(expected, actual)

        for col in utils.COLUMN_NAMES:
            actual = validator.validate_move_case(col)
            self.assertEqual(expected, actual)

    def test_validate_eat_case(self):
        expected = True
        for input_move in ['Kxf3', 'axb2', 'Rxd2']:

            actual = validator.validate_eat_case(input_move)
            self.assertEqual(expected, actual)

        expected = False
        for input_move in ['Kf3', 'a2', 'Rxd']:

            actual = validator.validate_eat_case(input_move)
            self.assertEqual(expected, actual)

    def test_is_valid_promotion(self):
        expected = True
        actual = validator.is_valid_promotion('a8', 'Q')
        self.assertEqual(expected,actual, msg = 'should be valid here')

        expected = True
        actual = validator.is_valid_promotion('b1', 'N')
        self.assertEqual(expected,actual, msg = 'should be valid here too')

        expected = False
        for new_piece in ['a','b','c','d','e','f','g','h','K']:
            actual = validator.is_valid_promotion('a8',new_piece)
            self.assertEqual(expected,actual, msg = 'no way this is valid')

if __name__ == '__main__':
    unittest.main()

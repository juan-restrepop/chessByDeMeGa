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

if __name__ == '__main__':
    unittest.main()

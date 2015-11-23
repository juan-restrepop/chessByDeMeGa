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

            actual = c.is_main_piece(input_move)
            self.assertEqual(expected, actual)
        # wrong moves
        expected = False
        for input_move in ['q','axc1','b3']:
            actual = c.is_main_piece(input_move)
            self.assertEqual(expected, actual)

    def test_piece_eats(self):
        c  = cg.ChessGame()
        expected = True
        for input_move in ['Kxf3','axb2','Rxd2']:

            actual = c.piece_eats(input_move)
            self.assertEqual(expected, actual)

        expected = False
        for input_move in ['a2','Bf3','q']:

            actual = c.piece_eats(input_move)
            self.assertEqual(expected, actual)

    def test_validate_eat_case(self):
        c  = cg.ChessGame()
        expected = True
        for input_move in ['Kxf3','axb2','Rxd2','Rxd222']:

            actual = c.validate_eat_case(input_move)
            self.assertEqual(expected, actual)

        expected = False
        for input_move in ['Kf3','a2','Rxd']:

            actual = c.validate_eat_case(input_move)
            self.assertEqual(expected, actual)

    def test_validate_normal_case(self):
        c  = cg.ChessGame()

        expected = True
        for piece in ['K','Q','N','B','R']:
            actual = c.validate_normal_case(piece +'f3')
            self.assertEqual(expected, actual)

        expected = True
        for col in c.column_names:
            actual = c.validate_normal_case(col +'3')
            self.assertEqual(expected, actual)

        expected = False
        for piece in ['K','Q','N','B','R']:
            actual = c.validate_normal_case(piece +'3')
            self.assertEqual(expected, actual)

        for col in c.column_names:
            actual = c.validate_normal_case(col)
            self.assertEqual(expected, actual)

    def test_is_user_move_valid(self):
        c  = cg.ChessGame()

        expected = True
        for input_move in ['a2','axb2','Bf3','Bxa2']:
            actual = c.is_user_move_valid(input_move)
            self.assertEqual(expected, actual)

        expected = False
        for input_move in ['ax2','B3','Abcd']:
            actual = c.is_user_move_valid(input_move)
            self.assertEqual(expected, actual)

    def test_are_coordinates_valid(self):
        c = cg.ChessGame()

        expected = True
        for coords in [('a', '1'), ('d', '5'), ('h', '8')]:
            actual = c.are_coordinates_valid(coords[0], coords[1])
            self.assertEqual(expected, actual)

        expected = False
        for coords in [('a', '-1'), ('z', '5'), ('z', '17'), ('A', '5')]:
            actual = c.are_coordinates_valid(coords[0], coords[1])
            self.assertEqual(expected, actual)

    def test_parse_pawn_coordinates(self):
        c = cg.ChessGame()

        expected = [('a','2'),
                    ('b','2')]

        test_cases = ['a2','axb2']

        for k in range(len(test_cases)):
            input_move = test_cases[k]
            actual = c.parse_pawn_coordinates(input_move)
            self.assertEqual(expected[k], actual)


    def test_parse_main_pieces_coordinates(self):
        c = cg.ChessGame()

        expected = [('f','2'),
                    ('b','3')]

        test_cases = ['Bf2','Qxb3']

        for k in range(len(test_cases)):
            input_move = test_cases[k]
            actual = c.parse_main_pieces_coordinates(input_move)
            self.assertEqual(expected[k], actual)

    def test_is_check(self):
        c = cg.ChessGame()

        expected = True
        test_cases = ['Bf5+','a6#']
        for input_move in test_cases:
            actual = c.is_check(input_move)
            self.assertEqual(actual,expected)


if __name__ == '__main__':
    unittest.main()

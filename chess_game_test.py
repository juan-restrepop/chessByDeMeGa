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
        for input_move in ['Kxf3', 'axb2', 'Rxd2']:

            actual = c.validate_eat_case(input_move)
            self.assertEqual(expected, actual)

        expected = False
        for input_move in ['Kf3', 'a2', 'Rxd']:

            actual = c.validate_eat_case(input_move)
            self.assertEqual(expected, actual)

    def test_validate_move_case(self):
        c  = cg.ChessGame()

        expected = True
        for piece in ['K','Q','N','B','R']:
            actual = c.validate_move_case(piece +'f3')
            self.assertEqual(expected, actual)

        expected = True
        for col in c.column_names:
            actual = c.validate_move_case(col +'3')
            self.assertEqual(expected, actual)

        expected = False
        for piece in ['K','Q','N','B','R']:
            actual = c.validate_move_case(piece +'3')
            self.assertEqual(expected, actual)

        for col in c.column_names:
            actual = c.validate_move_case(col)
            self.assertEqual(expected, actual)

    def test_is_user_move_valid(self):
        c  = cg.ChessGame()

        expected = True
        k = 1
        for input_move in ['a2','axb2','Bf3','Bxa2']:
            actual = c.is_user_move_valid(input_move)
            self.assertEqual(expected, actual, msg='Error on test # %i: %s' % (k, input_move))
            k += 1

        expected = False
        k = 1
        for input_move  in ['ax2','B3','Abcd']:
            #print input_move, actual
            actual = c.is_user_move_valid(input_move)
            self.assertEqual(expected, actual, msg='Error on test # %i: %s'  %(k,input_move) )
            k += 1

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

        expected = [('a','2', None, None),
                    ('b','2', None, None)]

        test_cases = ['a2','axb2']

        for k in range(len(test_cases)):
            input_move = test_cases[k]
            actual = c.parse_pawn_coordinates(input_move)
            self.assertEqual(expected[k], actual)


    def test_parse_main_pieces_coordinates(self):
        c = cg.ChessGame()

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
            actual = c.parse_main_pieces_coordinates(input_move)
            self.assertEqual(expected[k], actual)

    def test_is_check(self):
        c = cg.ChessGame()

        expected = True
        test_cases = ['Bf5+','a6#']
        for input_move in test_cases:
            actual = c.is_check(input_move)
            self.assertEqual(actual,expected)

    def test_is_promotion(self):
        c  = cg.ChessGame()

        expected = (True,'a8','Q')
        actual =  c.is_promotion('a8=Q')
        self.assertEqual(expected,actual)

        expected = (False,'a8','')
        actual =  c.is_promotion('a8')
        self.assertEqual(expected,actual)

    def test_is_valid_promotion(self):
        c = cg.ChessGame()

        expected = True
        actual = c.is_valid_promotion('a8', 'Q')
        self.assertEqual(expected,actual, msg = 'should be valid here')

        expected = True
        actual = c.is_valid_promotion('b1', 'N')
        self.assertEqual(expected,actual, msg = 'should be valid here too')

        expected = False
        for new_piece in ['a','b','c','d','e','f','g','h','K']:
            actual = c.is_valid_promotion('a8',new_piece)
            self.assertEqual(expected,actual, msg = 'no way this is valid')

    # chess rules related tests
    # checks
    def test_black_king_out_of_check_mvt_1(self):
        c = cg.ChessGame()
        b = c.board
        c_ref = cg.ChessGame()
        b_ref = c_ref.board
        b.clean_pieces()
        b_ref.clean_pieces()

        c.player = 'black'
        c_ref.player = 'black'
        
        # Test valid escape from single check
        b.initialize_single_piece('k', 'b', b.transform_board_to_grid('d', '3'))
        b.initialize_single_piece('q', 'w', b.transform_board_to_grid('g', '6'))
        c.parse_user_move('Kd4')

        b_ref.initialize_single_piece('k', 'b', b_ref.transform_board_to_grid('d', '4'))
        b_ref.initialize_single_piece('q', 'w', b_ref.transform_board_to_grid('g', '6'))
        
        # test good board 
        expected = b_ref.color_augmented_grid()
        actual = c.board.color_augmented_grid()
        self.assertEqual(expected, actual, msg="Black king should be allowed to escape to 'd4'")

        # test good player
        exp_player = 'white'
        actual_player = c.player
        self.assertEqual(exp_player, actual_player, msg="Once out of check, should switch player")

    def test_black_king_out_of_check_mvt_2(self):
        c = cg.ChessGame()
        b = c.board
        b.clean_pieces()
        c.player = 'black'

        c_ref = cg.ChessGame()
        b_ref = c_ref.board
        b_ref.clean_pieces()
        c_ref.player = 'black'

        # Test valid escape plan by protecting piece
        b.initialize_single_piece('k', 'b', b.transform_board_to_grid('d', '3'))
        b.initialize_single_piece('b', 'b', b.transform_board_to_grid('d', '7'))
        b.initialize_single_piece('q', 'w', b.transform_board_to_grid('g', '6'))
        c.parse_user_move('Bf5')

        b_ref.initialize_single_piece('k', 'b', b_ref.transform_board_to_grid('d', '3'))
        b_ref.initialize_single_piece('b', 'b', b_ref.transform_board_to_grid('f', '5'))
        b_ref.initialize_single_piece('q', 'w', b_ref.transform_board_to_grid('g', '6'))

        expected = b_ref.color_augmented_grid()
        actual = c.board.color_augmented_grid()
        self.assertEqual(expected, actual, msg="The sacrifice of the black bishop to 'f5' saves the king")

        # test good player
        exp_player = 'white'
        actual_player = c.player
        self.assertEqual(exp_player, actual_player, msg="Once out of check, should switch player")

    def test_black_king_out_of_check_mvt_3(self):
        c = cg.ChessGame()
        b = c.board
        b.clean_pieces()
        c.player = 'black'

        c_ref = cg.ChessGame()
        b_ref = c_ref.board
        b_ref.clean_pieces()
        c_ref.player = 'black'

        b.initialize_single_piece('k', 'b', b.transform_board_to_grid('d', '3'))
        b.initialize_single_piece('q', 'w', b.transform_board_to_grid('g', '6'))
        c.parse_user_move('Kc2') #WARNING! c.board is updated in parse_move() so now c.board != b

        b_ref.initialize_single_piece('k', 'b', b_ref.transform_board_to_grid('d', '3'))
        b_ref.initialize_single_piece('q', 'w', b_ref.transform_board_to_grid('g', '6'))

        # test good player
        exp_player = 'black'
        actual_player = c.player
        self.assertEqual(exp_player, actual_player, msg="Still in check, still same player")

        expected = b_ref.color_augmented_grid()
        actual = c.board.color_augmented_grid() 
        self.assertEqual(expected, actual, msg="Black king should not be allowed to escape to 'c2'")

    def test_black_king_out_of_check_mvt_4(self):
        c = cg.ChessGame()
        b = c.board
        b.clean_pieces()
        c.player = 'black'

        c_ref = cg.ChessGame()
        b_ref = c_ref.board
        b_ref.clean_pieces()
        c_ref.player = 'black'

        b.initialize_single_piece('k', 'b', b.transform_board_to_grid('d', '3'))
        b.initialize_single_piece('q', 'w', b.transform_board_to_grid('g', '6'))
        b.initialize_single_piece('r', 'w', b.transform_board_to_grid('a', '4'))
        c.parse_user_move('Kd4') 

        b_ref.initialize_single_piece('k', 'b', b_ref.transform_board_to_grid('d', '3'))
        b_ref.initialize_single_piece('q', 'w', b_ref.transform_board_to_grid('g', '6'))
        b_ref.initialize_single_piece('r', 'w', b_ref.transform_board_to_grid('a', '4'))
        # test good player
        exp_player = 'black'
        actual_player = c.player
        self.assertEqual(exp_player, actual_player, msg="Still in check, still same player")

        expected = b_ref.color_augmented_grid()
        actual = c.board.color_augmented_grid() 
        self.assertEqual(expected, actual, msg="Black king should not be allowed to escape to 'd4', he is under attack by a rook ")

    def test_black_king_out_of_check_mvt_5(self):
        c = cg.ChessGame()
        b = c.board
        b.clean_pieces()
        c.player = 'black'

        c_ref = cg.ChessGame()
        b_ref = c_ref.board
        b_ref.clean_pieces()
        c_ref.player = 'black'

        b.initialize_single_piece('k', 'b', b.transform_board_to_grid('d', '3'))
        b.initialize_single_piece('b', 'b', b.transform_board_to_grid('d', '7'))
        b.initialize_single_piece('q', 'w', b.transform_board_to_grid('g', '6'))
        b.initialize_single_piece('r', 'w', b.transform_board_to_grid('d', '8'))
        c.parse_user_move('Bf5')

        b_ref.initialize_single_piece('k', 'b', b_ref.transform_board_to_grid('d', '3'))
        b_ref.initialize_single_piece('b', 'b', b_ref.transform_board_to_grid('d', '7'))
        b_ref.initialize_single_piece('q', 'w', b_ref.transform_board_to_grid('g', '6'))
        b_ref.initialize_single_piece('r', 'w', b_ref.transform_board_to_grid('d', '8'))

        # test good player
        exp_player = 'black'
        actual_player = c.player
        self.assertEqual(exp_player, actual_player, msg="Still in check, still same player")
        # test board
        expected = b_ref.color_augmented_grid()
        actual = c.board.color_augmented_grid() 
        self.assertEqual(expected, actual, msg="The sacrifice of the black bishop to 'f5' is not enough, still in check")

    def test_white_king_out_of_check_mvt_1(self):
        c = cg.ChessGame()
        b = c.board
        b.clean_pieces()
        c.player = 'white'

        c_ref = cg.ChessGame()
        b_ref = c_ref.board
        b_ref.clean_pieces()
        c_ref.player = 'black'

        # Test valid escape from single check
        b.initialize_single_piece('k', 'w', b.transform_board_to_grid('d', '3'))
        b.initialize_single_piece('q', 'b', b.transform_board_to_grid('g', '6'))
        c.parse_user_move('Kd4')

        b_ref.initialize_single_piece('k', 'w', b_ref.transform_board_to_grid('d', '4'))
        b_ref.initialize_single_piece('q', 'b', b_ref.transform_board_to_grid('g', '6'))

        expected = b_ref.color_augmented_grid()
        actual = c.board.color_augmented_grid()
        self.assertEqual(expected, actual, msg="White king should be allowed to escape to 'd4', no longer in check")

        # test good player
        exp_player = c_ref.player
        actual_player = c.player
        self.assertEqual(exp_player, actual_player, msg="out-of check ok, switch player")

    def test_white_king_out_of_check_mvt_2(self):
        c = cg.ChessGame()
        b = c.board
        b.clean_pieces()
        c.player = 'white'

        c_ref = cg.ChessGame()
        b_ref = c_ref.board
        b_ref.clean_pieces()
        c_ref.player = 'black'

        # Test valid escape plan by protecting piece
        b.initialize_single_piece('k', 'w', b.transform_board_to_grid('d', '3'))
        b.initialize_single_piece('b', 'w', b.transform_board_to_grid('d', '7'))
        b.initialize_single_piece('q', 'b', b.transform_board_to_grid('g', '6'))
        c.parse_user_move('Bf5')

        b_ref.initialize_single_piece('k', 'w', b_ref.transform_board_to_grid('d', '3'))
        b_ref.initialize_single_piece('b', 'w', b_ref.transform_board_to_grid('f', '5'))
        b_ref.initialize_single_piece('q', 'b', b_ref.transform_board_to_grid('g', '6'))

        expected = b_ref.color_augmented_grid()
        actual = b.color_augmented_grid()
        self.assertEqual(expected, actual, msg="The sacrifice of the white bishop to 'f5' saves the king, no longer in check")

        # test good player
        exp_player = c_ref.player
        actual_player = c.player
        self.assertEqual(exp_player, actual_player, msg="out-of check ok, switch player")

       

if __name__ == '__main__':
    unittest.main()

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
        actual = c.board.color_augmented_grid()
        self.assertEqual(expected, actual, msg="The sacrifice of the white bishop to 'f5' saves the king, no longer in check")

        # test good player
        exp_player = c_ref.player
        actual_player = c.player
        self.assertEqual(exp_player, actual_player, msg="out of check ok, switch player")

    def test_white_king_out_of_check_mvt_3(self):
        c = cg.ChessGame()
        b = c.board
        b.clean_pieces()
        c.player = 'white'

        c_ref = cg.ChessGame()
        b_ref = c_ref.board
        b_ref.clean_pieces()
        c_ref.player = 'white'

         # Test invalid escape from single check
        b.initialize_single_piece('k', 'w', b.transform_board_to_grid('d', '3'))
        b.initialize_single_piece('q', 'b', b.transform_board_to_grid('g', '6'))
        c.parse_user_move('Kc2')

        b_ref.initialize_single_piece('k', 'w', b_ref.transform_board_to_grid('d', '3'))
        b_ref.initialize_single_piece('q', 'b', b_ref.transform_board_to_grid('g', '6'))

        expected = b_ref.color_augmented_grid()
        actual = c.board.color_augmented_grid()
        self.assertEqual(expected, actual, msg="White king should not be allowed to escape to 'c2'")

        # test good player
        exp_player = c_ref.player
        actual_player = c.player
        self.assertEqual(exp_player, actual_player, msg="still in check, don't switch player")

    def test_white_king_out_of_check_mvt_4(self):
        c = cg.ChessGame()
        b = c.board
        b.clean_pieces()
        c.player = 'white'

        c_ref = cg.ChessGame()
        b_ref = c_ref.board
        b_ref.clean_pieces()
        c_ref.player = 'white'

        # Test invalid from one check to another
        b.initialize_single_piece('k', 'w', b.transform_board_to_grid('d', '3'))
        b.initialize_single_piece('q', 'b', b.transform_board_to_grid('g', '6'))
        b.initialize_single_piece('r', 'b', b.transform_board_to_grid('a', '4'))
        c.parse_user_move('Kd4')

        b_ref.initialize_single_piece('k', 'w', b_ref.transform_board_to_grid('d', '3'))
        b_ref.initialize_single_piece('q', 'b', b_ref.transform_board_to_grid('g', '6'))
        b_ref.initialize_single_piece('r', 'b', b_ref.transform_board_to_grid('a', '4'))

        expected = b_ref.color_augmented_grid()
        actual = c.board.color_augmented_grid()
        self.assertEqual(expected, actual, msg="White king should not be allowed to escape to 'd4', he is under attack by a rook")
        
        # test good player
        exp_player = c_ref.player
        actual_player = c.player
        self.assertEqual(exp_player, actual_player, msg="still in check, don't switch player")

    def test_white_king_out_of_check_mvt_5(self):
        c = cg.ChessGame()
        b = c.board
        b.clean_pieces()
        c.player = 'white'

        c_ref = cg.ChessGame()
        b_ref = c_ref.board
        b_ref.clean_pieces()
        c_ref.player = 'white'

         # Test invalid escape plan by protecting piece
        b.initialize_single_piece('k', 'w', b.transform_board_to_grid('d', '3'))
        b.initialize_single_piece('b', 'w', b.transform_board_to_grid('d', '7'))
        b.initialize_single_piece('q', 'b', b.transform_board_to_grid('g', '6'))
        b.initialize_single_piece('r', 'b', b.transform_board_to_grid('d', '8'))
        c.parse_user_move('Bf5')

        b_ref.initialize_single_piece('k', 'w', b_ref.transform_board_to_grid('d', '3'))
        b_ref.initialize_single_piece('b', 'w', b_ref.transform_board_to_grid('d', '7'))
        b_ref.initialize_single_piece('q', 'b', b_ref.transform_board_to_grid('g', '6'))
        b_ref.initialize_single_piece('r', 'b', b_ref.transform_board_to_grid('d', '8'))

        expected = b_ref.color_augmented_grid()
        actual = c.board.color_augmented_grid()
        self.assertEqual(expected, actual, msg="The sacrifice of the white bishop to 'f5' is not enough, still in check")

        # test good player
        exp_player = c_ref.player
        actual_player = c.player
        self.assertEqual(exp_player, actual_player, msg="still in check, don't switch player")

    def test_blocked_black_pinned_bishop(self):
        c = cg.ChessGame()
        b = c.board
        b.clean_pieces()
        c.player = 'black'

        c_ref = cg.ChessGame()
        b_ref = c_ref.board
        b_ref.clean_pieces()
        c_ref.player = 'white'

        # Test valid protecting piece movement
        b.initialize_single_piece('k', 'b', b.transform_board_to_grid('d', '3'))
        b.initialize_single_piece('b', 'b', b.transform_board_to_grid('f', '5'))
        b.initialize_single_piece('q', 'w', b.transform_board_to_grid('h', '7'))
        c.parse_user_move('Bg6')

        b_ref.initialize_single_piece('k', 'b', b_ref.transform_board_to_grid('d', '3'))
        b_ref.initialize_single_piece('b', 'b', b_ref.transform_board_to_grid('g', '6'))
        b_ref.initialize_single_piece('q', 'w', b_ref.transform_board_to_grid('h', '7'))

        expected = b_ref.color_augmented_grid()
        actual = c.board.color_augmented_grid()
        self.assertEqual(expected, actual, msg="Black bishop should be allowed to go to 'g6'")
        # test good player
        exp_player = c_ref.player
        actual_player = c.player
        self.assertEqual(exp_player, actual_player, msg="not in check, switch player")

    def test_blocked_black_pinned_bishop_2(self):
        c = cg.ChessGame()
        b = c.board
        b.clean_pieces()
        c.player = 'black'

        c_ref = cg.ChessGame()
        b_ref = c_ref.board
        b_ref.clean_pieces()
        c_ref.player = 'black'

        # Test invalid protecting piece treason
        b.initialize_single_piece('k', 'b', b.transform_board_to_grid('d', '3'))
        b.initialize_single_piece('b', 'b', b.transform_board_to_grid('f', '5'))
        b.initialize_single_piece('q', 'w', b.transform_board_to_grid('h', '7'))
        c.parse_user_move('Bh3')

        b_ref.initialize_single_piece('k', 'b', b_ref.transform_board_to_grid('d', '3'))
        b_ref.initialize_single_piece('b', 'b', b_ref.transform_board_to_grid('f', '5'))
        b_ref.initialize_single_piece('q', 'w', b_ref.transform_board_to_grid('h', '7'))

        expected = b_ref.color_augmented_grid()
        actual = c.board.color_augmented_grid()
        self.assertEqual(expected, actual, msg="Black bishop should not be allowed to go to 'h3'")
        # test good player
        exp_player = c_ref.player
        actual_player = c.player
        self.assertEqual(exp_player, actual_player, msg="not in check, switch player")

    def test_blocked_white_pinned_bishop(self):
        c = cg.ChessGame()
        b = c.board
        b.clean_pieces()
        c.player = 'white'

        c_ref = cg.ChessGame()
        b_ref = c_ref.board
        b_ref.clean_pieces()
        c_ref.player = 'black'

        # Test valid protecting piece movement
        b.initialize_single_piece('k', 'w', b.transform_board_to_grid('d', '3'))
        b.initialize_single_piece('b', 'w', b.transform_board_to_grid('f', '5'))
        b.initialize_single_piece('q', 'b', b.transform_board_to_grid('h', '7'))
        c.parse_user_move('Bg6')
        
        b_ref.initialize_single_piece('k', 'w', b_ref.transform_board_to_grid('d', '3'))
        b_ref.initialize_single_piece('b', 'w', b_ref.transform_board_to_grid('g', '6'))
        b_ref.initialize_single_piece('q', 'b', b_ref.transform_board_to_grid('h', '7'))

        expected = b_ref.color_augmented_grid()
        actual = c.board.color_augmented_grid()
        self.assertEqual(expected, actual, msg="White bishop should be allowed to go to 'g6'")
        # test good player
        exp_player = c_ref.player
        actual_player = c.player
        self.assertEqual(exp_player, actual_player, msg="not in check, switch player")

    def test_blocked_white_pinned_bishop_2(self):
        c = cg.ChessGame()
        b = c.board
        b.clean_pieces()
        c.player = 'white'

        c_ref = cg.ChessGame()
        b_ref = c_ref.board
        b_ref.clean_pieces()
        c_ref.player = 'white'

       # Test invalid protecting piece treason
        b.clean_pieces()
        b_ref.clean_pieces()
        b.initialize_single_piece('k', 'w', b.transform_board_to_grid('d', '3'))
        b.initialize_single_piece('b', 'w', b.transform_board_to_grid('f', '5'))
        b.initialize_single_piece('q', 'b', b.transform_board_to_grid('h', '7'))
        c.parse_user_move('Bh3')

        b_ref.initialize_single_piece('k', 'w', b_ref.transform_board_to_grid('d', '3'))
        b_ref.initialize_single_piece('b', 'w', b_ref.transform_board_to_grid('f', '5'))
        b_ref.initialize_single_piece('q', 'b', b_ref.transform_board_to_grid('h', '7'))

        expected = b_ref.color_augmented_grid()
        actual = c.board.color_augmented_grid()
        self.assertEqual(expected, actual, msg="White bishop should not be allowed to go to 'h3'")
        # test good player
        exp_player = c_ref.player
        actual_player = c.player
        self.assertEqual(exp_player, actual_player, msg="check, still same player")

    def test_blocked_white_king_selfdestroy_1(self):
        c = cg.ChessGame()
        b = c.board
        b.clean_pieces()
        c.player = 'white'

        c_ref = cg.ChessGame()
        b_ref = c_ref.board
        b_ref.clean_pieces()
        c_ref.player = 'white'

        # Test forbidden movement
        b.initialize_single_piece('k', 'w', b.transform_board_to_grid('d', '3'))
        b.initialize_single_piece('q', 'b', b.transform_board_to_grid('e', '6'))
        c.parse_user_move('Kc4')

        b_ref.initialize_single_piece('k', 'w', b_ref.transform_board_to_grid('d', '3'))
        b_ref.initialize_single_piece('q', 'b', b_ref.transform_board_to_grid('e', '6'))

        expected = (b_ref.color_augmented_grid(), c.player)
        actual = (c.board.color_augmented_grid(), c_ref.player)
        self.assertEqual(expected, actual, msg = "The white king should not be allowed to go to 'c4'")

    def test_blocked_white_king_selfdestroy_2(self):
        c = cg.ChessGame()
        b = c.board
        b.clean_pieces()
        c.player = 'white'

        c_ref = cg.ChessGame()
        b_ref = c_ref.board
        b_ref.clean_pieces()
        c_ref.player = 'white'

        # Test not approved movement
        b.initialize_single_piece('k', 'w', b.transform_board_to_grid('d', '3'))
        b.initialize_single_piece('q', 'b', b.transform_board_to_grid('e', '6'))
        c.parse_user_move('Ke4')

        b_ref.initialize_single_piece('k', 'w', b_ref.transform_board_to_grid('d', '3'))
        b_ref.initialize_single_piece('q', 'b', b_ref.transform_board_to_grid('e', '6'))

        expected = (b_ref.color_augmented_grid(), c.player)
        actual = (c.board.color_augmented_grid(), c_ref.player)
        self.assertEqual(expected, actual, msg = "The white king should not be allowed to go to 'e4'")

    def test_blocked_black_king_selfdestroy(self):
        c = cg.ChessGame()
        b = c.board
        b.clean_pieces()
        c.player = 'black'

        c_ref = cg.ChessGame()
        b_ref = c_ref.board
        b_ref.clean_pieces()
        c_ref.player = 'black'

        # Test not approved movement
        b.initialize_single_piece('k', 'b', b.transform_board_to_grid('d', '3'))
        b.initialize_single_piece('q', 'w', b.transform_board_to_grid('e', '6'))
        c.parse_user_move('Kc4')
        
        b_ref.initialize_single_piece('k', 'b', b_ref.transform_board_to_grid('d', '3'))
        b_ref.initialize_single_piece('q', 'w', b_ref.transform_board_to_grid('e', '6'))
        expected = (b_ref.color_augmented_grid(), c.player)
        actual = (c.board.color_augmented_grid(), c_ref.player)
        self.assertEqual(expected, actual, msg = "The black king should not be allowed to go to 'c4'")

    def test_blocked_black_king_selfdestroy(self):
        c = cg.ChessGame()
        b = c.board
        b.clean_pieces()
        c.player = 'black'

        c_ref = cg.ChessGame()
        b_ref = c_ref.board
        b_ref.clean_pieces()
        c_ref.player = 'black'

        # Test non approved movement
        b.initialize_single_piece('k', 'b', b.transform_board_to_grid('d', '3'))
        b.initialize_single_piece('q', 'w', b.transform_board_to_grid('e', '6'))
        c.parse_user_move('Ke4')

        b_ref.initialize_single_piece('k', 'b', b_ref.transform_board_to_grid('d', '3'))
        b_ref.initialize_single_piece('q', 'w', b_ref.transform_board_to_grid('e', '6'))

        expected = (b_ref.color_augmented_grid(), c.player)
        actual = (c.board.color_augmented_grid(), c_ref.player)
        self.assertEqual(expected, actual, msg = "The black king should not be allowed to go to 'e4'")

    # End-of-game tests
    def test_fastest_checkmate(self):
        c= cg.ChessGame()

        c.player = 'white'
        c.parse_user_move('f4')
        c.parse_user_move('e6')
        c.parse_user_move('g4')
        c.parse_user_move('Qh4')

        expected = ("black", False, True)
        actual = (c.player, \
                  c.board.Rules.can_opponent_keep_playing(c.board, c.player), \
                  c.board.Rules.is_king_under_attack(c.board, "white"))
        self.assertEqual(actual, expected)

    def test_fools_checkmate_white(self):
        c= cg.ChessGame()

        c.player = 'white'
        c.parse_user_move('d4') #w
        c.parse_user_move('g5') #b
        c.parse_user_move('Bxg5') #w
        c.parse_user_move('f6') #b
        c.parse_user_move('e4') #w
        c.parse_user_move('fxg5') #b
        c.parse_user_move('Qh5') #w

        expected = ("white", False, True)
        actual = (c.player, \
                  c.board.Rules.can_opponent_keep_playing(c.board, c.player), \
                  c.board.Rules.is_king_under_attack(c.board, "black"))
        self.assertEqual(actual, expected)
    
    def test_checkmate_promote(self):
        c= cg.ChessGame()
        b = c.board
        b.clean_pieces()

        b.initialize_single_piece('k', 'w', b.transform_board_to_grid('b', '1'))
        b.initialize_single_piece('k', 'b', b.transform_board_to_grid('b', '3'))
        b.initialize_single_piece('p', 'b', b.transform_board_to_grid('g', '2'))

        c.player = 'black'
        c.parse_user_move('g1=Q')

        expected = ('black', False, True)
        actual = (c.player, \
                  c.board.Rules.can_opponent_keep_playing(c.board,c.player), \
                  c.board.Rules.is_king_under_attack(c.board,"white"))
        self.assertEqual(actual ,expected)

    def test_stalemate(self):
        c= cg.ChessGame()
        b = c.board
        b.clean_pieces()

        b.initialize_single_piece('k', 'w', b.transform_board_to_grid('a', '1'))
        b.initialize_single_piece('k', 'b', b.transform_board_to_grid('a', '3'))
        b.initialize_single_piece('q', 'b', b.transform_board_to_grid('e', '4'))
        c.player = "black"
        c.parse_user_move('Qd3')

        expected = ("black", False, False)
        actual = (c.player, \
                  c.board.Rules.can_opponent_keep_playing(c.board, c.player), \
                  c.board.Rules.is_king_under_attack(c.board, "white"))
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()

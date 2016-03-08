""" input_parser: parses chess game inputs """

import utils
import chess_validator as validator

def piece_eats(input_move):
    return validator.validate_eat_case(input_move)  
""" input_parser: parses chess game inputs """

import utils
import chess_validator as validator

def piece_eats(input_move):
    return validator.validate_eat_case(input_move)

def parse_pawn_coordinates(input_move):
    col_filter, line_filter = None, None
    col,line = input_move[-2],input_move[-1]
    # ambiguities only if eating
    if piece_eats(input_move):
        if len(input_move)== 4:
            if input_move[1]in utils.COLUMN_NAMES:
                col_filter = input_move[1]
            elif input_move[1]in utils.LINE_NAMES:
                line_filter = input_move[1]
        elif len(input_move)== 5:
            col_filter, line_filter = input_move[1],input_move[2]

    return col, line, col_filter, line_filter

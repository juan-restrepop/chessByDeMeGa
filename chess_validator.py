""" chess_validator: validator functions for game inputs  """

import utils
import chess_moves as cm

def are_coordinates_valid(col, line):
    return (line in utils.LINE_NAMES) and (col in utils.COLUMN_NAMES)


def validate_move_case(input_move):

    if cm.is_pawn(input_move):
        return len(input_move) == 2 and input_move[1] in utils.LINE_NAMES

    if (not cm.is_main_piece(input_move) )or \
        not are_coordinates_valid(input_move[-2], input_move[-1]):
        return False

    return ( len(input_move) == 3
                or
                ( input_move[1] in utils.COLUMN_NAMES+ utils.LINE_NAMES
                and
                len(input_move) == 4 )
                or
                ( are_coordinates_valid(input_move[1], input_move[2]) 
                and
                len(input_move) == 5 )
            )
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

def validate_eat_case(input_move):
    if len(input_move) < 4 or \
        input_move[-3] != 'x' or \
        (not are_coordinates_valid(input_move[-2], input_move[-1])):
        return False

    return (  ( len(input_move) == 4 
                and (cm.is_pawn(input_move) or cm.is_main_piece(input_move)) 
                ) 
            or 
              ( len(input_move) == 5 
                and ( cm.is_main_piece(input_move))
                and ( input_move[1] in utils.COLUMN_NAMES + utils.LINE_NAMES )
                )
            or
              ( len(input_move) == 6 
                and ( cm.is_main_piece(input_move))
                and ( are_coordinates_valid(input_move[1], input_move[2]) )
                )
            )

def is_valid_promotion(input_move, promoted_to):
    return input_move[-1] in [ '1','8' ] and \
           promoted_to in ['B','N','R','Q'] and \
           (validate_move_case(input_move) or validate_eat_case(input_move))


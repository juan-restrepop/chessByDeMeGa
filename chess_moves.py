""" Useful functions for parsing user input moves """

import utils

def is_pawn(input_move):
    return input_move[0] in utils.COLUMN_NAMES

def is_bishop(input_move):
    return input_move[0] == 'B'

def is_rook(input_move):
    return input_move[0] == 'R'

def is_knight(input_move):
    return input_move[0] == 'N'

def is_queen(input_move):
    return input_move[0] == 'Q'

def is_king(input_move):
    return input_move[0] == 'K'

def is_main_piece(input_move):
    return input_move[0] in ['K','Q','N','B','R']

def is_any_piece(input_move):
    return is_pawn(input_move) or \
            is_bishop(input_move) or \
            is_rook(input_move) or \
            is_knight(input_move) or \
            is_queen(input_move) or \
            is_king (input_move)

def is_check(input_move):
    return input_move[-1] in ['+','#']

def is_castling(input_move):
    res = input_move in ['O-O','O-O-O']
    return res 

def is_short_castling(input_move):
    return input_move == 'O-O'

def is_long_castling(input_move):
    return input_move == 'O-O-O'

def is_special_case(input_move):
    return is_end_of_game(input_move)

def is_end_of_game(input_move):
    res = input_move in ['1-0','0-1', '1/2-1/2']
    if res:
        print "End of game: " + input_move
    return res

def is_promotion(input_move):
    if not '=' in input_move:
        return (False, input_move,'')
    else:
        idx = input_move.index('=')
        return (True,input_move[:idx],input_move[idx+1:])

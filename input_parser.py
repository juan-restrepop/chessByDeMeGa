""" input_parser: parses chess game inputs """

import utils
import chess_moves as cm
import chess_validator as validator

def input_to_kind(input_move):
    kind = None
    
    if cm.is_any_piece(input_move):
        if cm.is_pawn(input_move):
            kind = 'p'

        elif cm.is_bishop(input_move):
            kind = 'b'

        elif cm.is_knight(input_move):
            kind = 'n'

        elif cm.is_rook(input_move):
            kind = 'r'

        elif cm.is_king(input_move):
            kind = 'k'

        elif cm.is_queen(input_move):
            kind = 'q'

    return kind

def parse_coordinates(input_move):
    if cm.is_pawn(input_move):
        move_to_col, move_to_line, col_filter, line_filter = parse_pawn_coordinates(input_move)

    elif cm.is_main_piece(input_move):
        move_to_col, move_to_line, col_filter, line_filter = parse_main_pieces_coordinates(input_move)

    else:
        move_to_col, move_to_line = None, None
        col_filter, line_filter = None, None

    return move_to_col, move_to_line, col_filter, line_filter

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

def parse_main_pieces_coordinates(input_move):
    col_filter, line_filter = None, None
    col,line = input_move[-2],input_move[-1]

    if piece_eats(input_move):
        if len(input_move)== 5:
            if input_move[1]in utils.COLUMN_NAMES:
                col_filter = input_move[1]
            elif input_move[1]in utils.LINE_NAMES:
                line_filter = input_move[1]
        elif len(input_move)== 6:
                col_filter, line_filter = input_move[1],input_move[2]
    else:
        if len(input_move)== 4:
            if input_move[1]in utils.COLUMN_NAMES:
                col_filter = input_move[1]
            elif input_move[1]in utils.LINE_NAMES:
                line_filter = input_move[1]
        elif len(input_move)== 5:
                col_filter, line_filter = input_move[1],input_move[2]
    return col,line, col_filter, line_filter

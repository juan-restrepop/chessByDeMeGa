""" chess_validator: validator functions for game inputs  """

import utils

def are_coordinates_valid(col, line):
    return (line in utils.LINE_NAMES) and (col in utils.COLUMN_NAMES)

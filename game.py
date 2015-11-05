def print_board(board_size):
    board_string = ''
    for i in range(0, board_size):
        for j in range(0, board_size):
            board_string = board_string + str( (j + i) % 2)

        board_string = board_string + '\n'

    print board_string


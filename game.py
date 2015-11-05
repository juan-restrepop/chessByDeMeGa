class Game(object):
    grid = list()

    def __init__(self):
        for i in range(0,8):
            self.grid.append(list())

            for j in range(0, 8):
                self.grid[i].append(str((j + i) % 2))

    def print_board(self):

        board_string = ''
        for i in range(0, 8):
            for j in range(0, 8):
                board_string = board_string + ' ' + self.grid[i][j]

            board_string = board_string + '\n'

        print board_string



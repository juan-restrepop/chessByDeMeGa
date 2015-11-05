class Pawn(object):
    kind = 'p'
    coordinate = list()

    def __init__(self, color, coordinates):
        self.initialize_pawn(color, coordinates)

    def initialize_pawn(self, color, coordinates):
        self.color = color
        self.coordinates = coordinates

class Game(object):
    grid = list()
    pawn = Pawn('w', [1, 0])

    def __init__(self):
        self.initialize_board()
        self.initialize_board_with_pieces()

    def initialize_board_with_pieces(self):
        rowCoord = self.pawn.coordinates[0]
        colCoord = self.pawn.coordinates[1]

        self.grid[rowCoord][colCoord] = self.pawn.kind


    def initialize_board(self):
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

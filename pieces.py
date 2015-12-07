class Piece(object):
    kind = str()
    color = str()
    coordinates = list()

    def __init__(self, kind, color, coordinate):
        self.initialize_piece(kind, color, coordinate)

    def initialize_piece(self, kind, color, coordinate):
        self.kind = kind
        self.color = color
        self.coordinates = coordinate

class Pawn(Piece):
    def __init__(self, color, coordinates):
        Piece.__init__(self, 'p', color, coordinates)

class Rook(Piece):
    def __init__(self, color, coordinates):
        Piece.__init__(self, 'r', color, coordinates)
        self.has_moved = False

class Bishop(Piece):
    def __init__(self, color, coordinates):
        Piece.__init__(self, 'b', color, coordinates)

class Knight(Piece):
    def __init__(self, color, coordinates):
        Piece.__init__(self, 'n', color, coordinates)

class Queen(Piece):
    def __init__(self, color, coordinates):
        Piece.__init__(self, 'q', color, coordinates)

class King(Piece):
    def __init__(self, color, coordinates):
        Piece.__init__(self, 'k', color, coordinates)
        self.has_moved = False

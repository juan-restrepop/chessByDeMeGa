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
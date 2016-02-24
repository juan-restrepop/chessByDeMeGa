class Piece(object):
    kind = str()
    color = str()
    coordinates = list()
    has_moved = False

    def __init__(self, kind, color, coordinate):
        self.initialize_piece(kind, color, coordinate)

    def initialize_piece(self, kind, color, coordinate):
        self.kind = kind
        self.color = color
        self.coordinates = coordinate

    def get_natural_moves(self):
        pass

    def get_diagonal_moves(self):
        line,col = self.coordinates
        nat_moves = []
        # down right
        nat_moves = [ [line+k,col+k] for k in range(1,8) if (line+k)<8 and (col+k<8)]
        # down left
        nat_moves = nat_moves + [ [line+k,col-k] for k in range(1,8) if (line+k)<8 and (col-k)>=0]
        # up right
        nat_moves = nat_moves + [ [line-k,col+k] for k in range(1,8) if (line-k)>=0 and (col+k)<8]
        # up left
        nat_moves = nat_moves + [ [line-k,col-k] for k in range(1,8) if (line-k)>=0 and (col-k)>=0]
        return nat_moves   

    def get_straight_moves(self):
        line,col = self.coordinates
        nat_moves = []
        nat_moves = [[k,col] for k in range(8) if k!=line ]
        nat_moves = nat_moves + [[line,j] for j in range(8) if j!=col ]
        return nat_moves

class Pawn(Piece):
    def __init__(self, color, coordinates):
        Piece.__init__(self, 'p', color, coordinates)

    def get_natural_moves(self):
        line,col = self.coordinates
        nat_moves = []

        if self.color == 'w':
            nat_moves = [ [line-1,col+k] for k in [-1,0,1] if (line>0) and (col+k) in range(0,7) ]
            # +possible initial white jump
            if line == 1:
                nat_moves = nat_moves + [line,3]

        elif self.color == 'b':
            nat_moves = [ [line+1,col+k] for k in [-1,0,1] if (line<7) and (col+k) in range(0,7) ]
            # + possible initial black jump
            if line == 6:
                nat_moves = nat_moves + [line,4]
        else:
            raise Exception
        return nat_moves

class Rook(Piece):
    def __init__(self, color, coordinates):
        Piece.__init__(self, 'r', color, coordinates)

    def get_natural_moves(self):
        return self.get_straight_moves()

class Bishop(Piece):
    def __init__(self, color, coordinates):
        Piece.__init__(self, 'b', color, coordinates)

    def get_natural_moves(self):
        return self.get_diagonal_moves()

class Knight(Piece):
    def __init__(self, color, coordinates):
        Piece.__init__(self, 'n', color, coordinates)

    def get_natural_moves(self):
        line,col = self.coordinates
        nat_moves = []
        nat_moves = [ [line+k,col+j] for [k,j] in [ [2,1], [2,-1], [1,2], [1,-2], [-1,2], [-1,-2], [-2,1], [-2,-1] ] \
                        if ( (line+k) in range(8) and (col+j) in range(8) ) ]
        return nat_moves

class Queen(Piece):
    def __init__(self, color, coordinates):
        Piece.__init__(self, 'q', color, coordinates)

    def get_natural_moves(self):
        return self.get_diagonal_moves() + self.get_straight_moves()

class King(Piece):
    def __init__(self, color, coordinates):
        Piece.__init__(self, 'k', color, coordinates)

    def get_natural_moves(self):
        line,col = self.coordinates
        nat_moves = []
        # generate all possible coordinates
        nat_moves = [[line+k,col+j] for k in [-1,0,+1] for j in [-1,0,1] if not(k==0 and j==0)]
        # filter to get valid board coordinates
        nat_moves = [ [k,j] for [k,j] in nat_moves if (k>=0 and j>=0) and (k<8 and j<8) ]
        return nat_moves


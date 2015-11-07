import chess_board

class ChessGame(object):

    column_names = ['a','b','c','d','e','f','g','h']
    line_names = ['1','2','3','4','5','6','7','8']

    def __init__(self):
        self.board = chess_board.ChessBoard()

    def run(self):
        stay_in_game = True
        while(stay_in_game):
            self.board.print_board()
            stay_in_game = self.read_user_move()        

    def read_user_move(self):
        new_move_str = raw_input("Please enter a new move: \ntype 'q' to quit the game\n")
        
        return(self.parse_user_move(new_move_str))

    def has_quit(self, input_move):
        return input_move == "q"

    def is_special_case(self, input_move):
        res = input_move in ['O-O','O-O-O','1-0','0-1', '1/2-1/2']
        if res:
            print "Castling or End of game" 
        return res

    def is_pawn(self, input_move):
        return input_move[0] in self.column_names
        
    def is_main_piece(self, input_move):
        return input_move[0] in ['K','Q','N','B','R']

    def piece_eats(self, input_move):
        return (len(input_move)>1) and (input_move[1] == 'x')

    def validate_eat_case(self, input_move):
        if self.piece_eats(input_move) and len(input_move) >= 4:
            return True
        return False

    def validate_normal_case(self, input_move):
        # not eating move
        if self.is_pawn(input_move):
            if len(input_move) <= 1:
                return False
        elif self.is_main_piece(input_move):
            if len(input_move)< 3:
                return False
        return True            

    def is_user_move_valid(self, input_move):

        if len(input_move) <= 1:
            print 'wrong input try again'
            return False

        if self.is_special_case(input_move):
            print 'special cases are not supported yet'
            return False

        if self.piece_eats(input_move) and (not self.validate_eat_case(input_move)):
            print 'eat case not valid try again'
            return False

        if not self.piece_eats(input_move):
            if not self.validate_normal_case(input_move):
                print 'case not valid try again'
                return False

        if not self.is_pawn(input_move) and not self.is_main_piece(input_move):
            print 'case not valid, not a chess piece'
            return False

        return True

    def are_coordinates_valid(self, col, line):
        return (line in self.line_names) and (col in self.column_names)
        
    def parse_user_move(self, input_move):
        # TODO: Handle ambiguities
        # TODO: Handle check, check-mate

        input_move = input_move.lstrip()

        if self.has_quit(input_move):
            return False

        if not self.is_user_move_valid(input_move):
            return True

        move_to_col, move_to_line = None, None

        if self.is_pawn(input_move):
            move_to_col, move_to_line = self.parse_pawn_coordinates(input_move)

        if self.is_main_piece(input_move):
            move_to_col, move_to_line = self.parse_main_pieces_coordinates(input_move)

        if not self.are_coordinates_valid(move_to_col, move_to_line):
            print 'coordinates not valid try again'
            return True

        # print accepted move
        is_pawn = self.is_pawn(input_move)
        is_captured = self.piece_eats(input_move)
        out_str = self.print_move(is_pawn, is_captured, move_to_col, move_to_line)

        print("Your move is : " + input_move + '. ' + out_str)

        return True

    def parse_pawn_coordinates(self, input_move):

        if self.piece_eats(input_move):
            return input_move[2], input_move[3]

        return input_move[0], input_move[1]

    def parse_main_pieces_coordinates(self, input_move):
        
        if self.piece_eats(input_move):
            return input_move[2], input_move[3] 

        return input_move[1], input_move[2]

    def print_move(self, is_pawn, is_captured, move_to_col, move_to_line):
        out_str  = ""
        if is_pawn:
            out_str = "Move pawn"
        else:
            out_str = "Move not_pawn"

        if is_captured: 
            out_str = out_str + " and capture piece at (%s,%s)" % (move_to_col,move_to_line)
        else: 
            out_str = out_str + " to (%s,%s)" % (move_to_col, move_to_line)

        return  out_str

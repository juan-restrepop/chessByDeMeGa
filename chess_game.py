import chess_board

class ChessGame(object):

    column_names = ['a','b','c','d','e','f','g','h']
    line_names = ['1','2','3','4','5','6','7','8']
    player = 'white'

    def __init__(self):
        self.board = chess_board.ChessBoard()

    def run(self):
        stay_in_game = True
        while(stay_in_game):
            self.board.print_board()
            stay_in_game = self.read_user_move()        

    def read_user_move(self):
        print "%s player's turn." % self.player
        new_move_str = raw_input("Please enter a new move: (type 'q' to quit the game) \n")
        
        return(self.parse_user_move(new_move_str))

    def has_quit(self, input_move):
        return input_move == "q"


    def is_special_case(self, input_move):
        return self.is_castling(input_move) or self.is_end_of_game(input_move)

    def is_castling(self, input_move):
        res = input_move in ['O-O','O-O-O']
        if res:
            print "Castling"
        return res

    def is_end_of_game(self, input_move):
        res = input_move in ['1-0','0-1', '1/2-1/2']
        if res:
            print "End of game"
        return res

    def is_promotion(self,input_move):
        if not '=' in input_move:
            return (False, input_move,'')
        else:
            idx = input_move.index('=')
            return (True,input_move[:idx],input_move[idx+1:]) 

    def is_check(self,input_move):
        return input_move[-1] in ['+','#']


    def is_pawn(self, input_move):
        return input_move[0] in self.column_names

    def is_bishop(self, input_move):
        return input_move[0] == 'B'

    def is_rook(self,input_move):
        return input_move[0] == 'R'

    def is_knight(self,input_move):
        return input_move[0] == 'N'

    def is_queen(self,input_move):
        return input_move[0] == 'Q'

    def is_king(self,input_move):
        return input_move[0] == 'K'
        

    def is_main_piece(self, input_move):
        return input_move[0] in ['K','Q','N','B','R']


    def validate_eat_case(self, input_move):
        if len(input_move) >= 4:
            if input_move[-3] == 'x':
                if self.are_coordinates_valid(input_move[-2],input_move[-1]):
                    return len(input_move) == 4 and (self.is_pawn(input_move) or self.is_main_piece(input_move))

        return False

    def validate_move_case(self, input_move):

        if self.is_pawn(input_move):
            if len(input_move) != 2:
                return False
            return input_move[1] in self.line_names

        elif self.is_main_piece(input_move):
            if len(input_move) != 3:
                return False
            return self.are_coordinates_valid(input_move[1], input_move[2])
        return False

    def is_valid_promotion(self, input_promotion):
        return input_promotion in ['B','N','R','Q']

    def is_user_move_valid(self, input_move):

        if len(input_move) <= 1:
            print 'wrong input try again'
            return False

        if self.is_special_case(input_move):
            print 'special cases are not supported yet'
            return False

        if not self.is_pawn(input_move) and not self.is_main_piece(input_move):
            print 'case not valid, not a chess piece'
            return False

        if self.validate_eat_case(input_move):
            print 'valid eat input'
            return True

        if self.validate_move_case(input_move):
            print 'valid move input'
            return True

        print 'wrong input, try again'
        return False


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

        if self.is_check(input_move):
            input_move = input_move[:-1]

        promotion,input_move,promoted_to = self.is_promotion(input_move)

        if promotion and not self.is_valid_promotion(promoted_to):
            return True

        move_to_col, move_to_line = None, None

        if self.is_pawn(input_move):
            move_to_col, move_to_line = self.parse_pawn_coordinates(input_move)

        if self.is_main_piece(input_move):
            move_to_col, move_to_line = self.parse_main_pieces_coordinates(input_move)

        accepted_move = self.move_piece_to(input_move, move_to_col, move_to_line)

        self.board.Rules.is_king_under_attack(self.board) #prints when white king is checked
        self.board.Rules.is_king_under_attack(self.board,'black') #when black king is checked
        if accepted_move:
            out_str = self.print_move(input_move, move_to_col, move_to_line)
            print("Your move is : " + input_move + '. ' + out_str)
            self.switch_player()

        else:
            print "Move not accepted"



        return True

    def switch_player(self):
        print self.player
        if self.player == 'white':
            self.player = 'black'
            return
        self.player = 'white'
        return



    def parse_pawn_coordinates(self, input_move):
        return input_move[-2],input_move[-1]

    def parse_main_pieces_coordinates(self, input_move):
        return input_move[-2],input_move[-1]

    def piece_eats(self, input_move):
        return self.validate_eat_case(input_move)

    def move_piece_to(self, input_move, move_to_col, move_to_line):
        
        if self.is_pawn(input_move):
            kind = 'p'

        elif self.is_bishop(input_move):
            kind = 'b'

        elif self.is_knight(input_move):
            kind = 'n'

        elif self.is_rook(input_move):
            kind = 'r'

        elif self.is_king(input_move):
            kind = 'k'

        elif self.is_queen(input_move):
            kind = 'q'

        else:
            return False
        if self.piece_eats(input_move):
            return self.board.piece_eater(kind, move_to_col,move_to_line,self.player)
        else:
            return self.board.piece_mover(kind, move_to_col,move_to_line,self.player)


    def print_move(self, input_move, move_to_col, move_to_line):
        out_str  = ""

        if self.is_pawn(input_move):
            out_str = "Move %s pawn" % self.player

        elif self.is_bishop(input_move):
            out_str = "Move %s bishop" % self.player
        
        elif self.is_knight(input_move):
            out_str = "Move %s knight" % self.player
        
        elif self.is_rook(input_move):
            out_str = "Move %s rook" % self.player
        
        elif self.is_king(input_move):
            out_str = "Move %s king" % self.player
        
        elif self.is_queen(input_move):
            out_str = "Move %s queen" % self.player
        else:
            out_str = "not supported move. Merry Xmas"

        if self.piece_eats(input_move):
            out_str = out_str + " and capture piece at (%s,%s)" % (move_to_col,move_to_line)
        else: 
            out_str = out_str + " to (%s,%s)" % (move_to_col, move_to_line)

        return  out_str

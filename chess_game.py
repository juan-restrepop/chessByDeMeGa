import chess_board

class ChessGame(object):
    
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

    def column_names(self):
        return ['a','b','c','d','e','f','g','h']

    def is_pawn(self, input_move):
        return input_move[0] in self.column_names()
        
    def is_main_piece(self, input_move):
        return input_move[0] in ['K','Q','N','B','R']

    def piece_eats(self, input_move):
        return input_move[1] == 'x'

    def is_valid_eat_case(self, input_move):
        'eat case should like "bxb6" or "Kxb7"'
        return len(input_move) >= 4

    def validate_eat_case(self, input_move):
        if self.piece_eats(input_move):
            if not self.is_valid_eat_case(input_move):
                return False
        return True

    def validate_normal_case(self, input_move):
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

        if not self.validate_eat_case(input_move):
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

    def parse_user_move(self, input_move):
        # TODO: Handle ambiguities
        # TODO: Handle check, check-mate

        input_move = input_move.lstrip()

        if self.has_quit(input_move):
            return False

        if not self.is_user_move_valid(input_move):
            return True

        all_cols = ['a','b','c','d','e','f','g','h']
        all_lines = ['1','2','3','4','5','6','7','8']
        out_str = ''

        # standard cases

        if self.is_pawn(input_move):

            if self.piece_eats(input_move):
                move_to_col = input_move[2]
                move_to_line = input_move[3]   
            else:
                move_to_col = input_move[0]
                move_to_line = input_move[1]

        elif self.is_main_piece(input_move):

            if self.piece_eats(input_move):
                move_to_col = input_move[2]
                move_to_line = input_move[3] 
            else: 
                move_to_col = input_move[1]
                move_to_line = input_move[2]
        else:
            return True

        if (move_to_line not in all_lines) or (move_to_col not in all_cols):
            return True

        # print accepted move
        is_pawn = self.is_pawn(input_move)
        is_captured = self.piece_eats(input_move)
        out_str = self.print_move(is_pawn,is_captured,move_to_col,move_to_line)

        print("Your move is : "+input_move + '. '+ out_str)

        return True

    def print_move(self,is_pawn,is_captured,move_to_col,move_to_line):
        out_str  = ""
        if is_pawn:
            out_str = "Move pawn"
        else:
            out_str = "Move not_pawn"

        if is_captured: 
            out_str = out_str + " and capture piece at (%s,%s)"%(move_to_col,move_to_line)
        else: 
            out_str = out_str + " to (%s,%s)"%(move_to_col,move_to_line)

        return  out_str


  


        

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
        
    def is_piece(self, input_move):
        return input_move[0] in ['K','Q','N','B','R'] or self.is_pawn(input_move)

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

    def parse_user_move(self, input_move):
        # TODO: Handle ambiguities
        # TODO: Handle check, check-mate

        input_move = input_move.lstrip()

        if self.has_quit(input_move):
            return False

        if len(input_move) <= 1:
            print 'wrong input try again'
            return True

        all_cols = ['a','b','c','d','e','f','g','h']
        all_lines = ['1','2','3','4','5','6','7','8']
        out_str = ''

        if self.is_special_case(input_move):
            return True

        if not self.validate_eat_case(input_move):
            print 'eat case not valid try again'
            return True

        # standard cases

        if self.is_pawn(input_move):

            if self.piece_eats(input_move):
                move_to_col = input_move[2]
                move_to_line = input_move[3]   
            else:
                move_to_col = input_move[0]
                move_to_line = input_move[1]

        elif self.is_piece(input_move):
            
            if self.piece_eats(input_move):
                move_to_col = input_move[2]
                move_to_line = input_move[3] 
            else: 
                if len(input_move)< 3:
                    return True
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


  


        

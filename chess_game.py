import copy
import utils
import input_parser
import chess_board
import chess_moves as cm
import chess_validator as validator

class ChessGame(object):

    column_names = utils.COLUMN_NAMES
    line_names = utils.LINE_NAMES
    player = 'white'

    def __init__(self):
        self.board = chess_board.ChessBoard()
        self.player = 'white'

    def run(self, play_generator = None):
        stay_in_game = True

        while(stay_in_game):
            self.board.print_board()
            stay_in_game = self.read_user_move(play_generator)

    def is_match(self):
        return len(self.board.king_w)>0 and len(self.board.king_b)>0

    def restart(self):
        self.__init__()
        print "New Game!"

    def hit_endgame(self):
        if not self.board.Rules.can_opponent_keep_playing(self.board,self.player):
            opponent = 'black' if (self.player == 'white') else 'white'

            if self.board.Rules.is_king_under_attack(self.board,opponent):
                print "Game over\n FATALITY (check-mate), %s wins! "%self.player
            else:
                print "Game over\n FATALITY (stalemate), no one wins!!  "
            return True

        return False

    def read_user_move(self, play_generator = None):
        print "%s player's turn." % self.player
        if play_generator is None:
            try:
                new_move = raw_input("Please enter a new move: (type 'q' to quit the game) \n")
            except EOFError:
                print "Quitting"
                return False
        else: 
            try:
                new_move = play_generator.next()
            except StopIteration:
                new_move = 'q'

        return self.parse_user_move(new_move)

    def has_quit(self, input_move):
        return input_move == "q"
        
    def parse_user_move(self, input_move):
        # TODO: Handle draws (50+ moves without exchange, or same state repeated 3 times)

        input_move = input_move.strip()

        if self.has_quit(input_move):
            return False

        if len(input_move)>1 and cm.is_check(input_move):
            input_move = input_move[:-1]

        if not validator.is_user_move_valid(input_move):
            return True

        promotion,input_move,promoted_to = cm.is_promotion(input_move)

        move_to_col,move_to_line,col_filter,line_filter = self.parse_coordinates(input_move)
        
        parallel_board = copy.deepcopy(self.board)
        accepted_move = self.move_piece_to(input_move, move_to_col, move_to_line, col_filter, line_filter)

        if promotion:
            self.board.promote( move_to_col, move_to_line, self.player, promoted_to )

        if self.board.Rules.is_king_under_attack(self.board,self.player):
            print "Cannot leave %s player in check!"%self.player
            accepted_move = False
            self.board = parallel_board

        if accepted_move:
            self.print_move(input_move, move_to_col, move_to_line)

            if self.is_match() and self.hit_endgame():
                return False
            else:
                self.switch_player()
        
        if cm.is_special_case(input_move):
                self.restart()
        return True

    def switch_player(self):
        self.player = 'black' if (self.player == 'white') else 'white'
        return

    def parse_coordinates(self,input_move):
        if cm.is_pawn(input_move):
            move_to_col, move_to_line, col_filter, line_filter = self.parse_pawn_coordinates(input_move)

        elif cm.is_main_piece(input_move):
            move_to_col, move_to_line, col_filter, line_filter = self.parse_main_pieces_coordinates(input_move)

        else:
            move_to_col, move_to_line = None, None
            col_filter, line_filter = None, None

        return move_to_col, move_to_line, col_filter, line_filter

    def parse_pawn_coordinates(self, input_move):
        col_filter, line_filter = None, None
        col,line = input_move[-2],input_move[-1]
        # ambiguities only if eating
        if input_parser.piece_eats(input_move):
            if len(input_move)== 4:
                if input_move[1]in self.column_names:
                    col_filter = input_move[1]
                elif input_move[1]in self.line_names:
                    line_filter = input_move[1]
            elif len(input_move)== 5:
                    col_filter, line_filter = input_move[1],input_move[2]

        return col,line, col_filter, line_filter

    def parse_main_pieces_coordinates(self, input_move):
        col_filter, line_filter = None, None
        col,line = input_move[-2],input_move[-1]

        # if eating
        if input_parser.piece_eats(input_move):
            if len(input_move)== 5:
                if input_move[1]in self.column_names:
                    col_filter = input_move[1]
                elif input_move[1]in self.line_names:
                    line_filter = input_move[1]
            elif len(input_move)== 6:
                    col_filter, line_filter = input_move[1],input_move[2]
        else:
            if len(input_move)== 4:
                if input_move[1]in self.column_names:
                    col_filter = input_move[1]
                elif input_move[1]in self.line_names:
                    line_filter = input_move[1]
            elif len(input_move)== 5:
                    col_filter, line_filter = input_move[1],input_move[2]
        return col,line, col_filter, line_filter

    def move_piece_to(self, input_move, move_to_col, move_to_line, col_filter = None, line_filter = None):
        if cm.is_castling(input_move):
            if cm.is_short_castling(input_move):
                return self.board.castler(self.player,'short')
            else:
                return self.board.castler(self.player,'long')

        if cm.is_pawn(input_move):
            kind = 'p'

        elif cm.is_bishop(input_move):
            kind = 'b'

        elif cm.is_knight(input_move):
            kind = 'n'

        elif cm.is_rook(input_move):
            kind = 'r'

        elif cm.is_king(input_move):
            kind = 'k'

        elif cm.is_queen(input_move):
            kind = 'q'

        else:
            return False
        if input_parser.piece_eats(input_move):
            return self.board.piece_eater(kind, move_to_col,move_to_line,self.player, orig_col_filter = col_filter, orig_line_filter = line_filter)
        else:
            return self.board.piece_mover(kind, move_to_col,move_to_line,self.player, orig_col_filter = col_filter, orig_line_filter = line_filter)


    def print_move(self, input_move, move_to_col, move_to_line):
        out_str  = ""

        if cm.is_short_castling(input_move):
            out_str = "Short castling for %s" % self.player
        
        elif cm.is_long_castling(input_move):
            out_str = "long castling for %s" % self.player

        elif cm.is_pawn(input_move):
            out_str = "Move %s pawn" % self.player

        elif cm.is_bishop(input_move):
            out_str = "Move %s bishop" % self.player
        
        elif cm.is_knight(input_move):
            out_str = "Move %s knight" % self.player
        
        elif cm.is_rook(input_move):
            out_str = "Move %s rook" % self.player
        
        elif cm.is_king(input_move):
            out_str = "Move %s king" % self.player
        
        elif cm.is_queen(input_move):
            out_str = "Move %s queen" % self.player
        else:
            out_str = "not supported move. Merry Xmas"

        if not cm.is_castling(input_move):
            if input_parser.piece_eats(input_move):
                out_str = out_str + " and capture piece at (%s,%s)" % (move_to_col,move_to_line)
            else: 
                out_str = out_str + " to (%s,%s)" % (move_to_col, move_to_line)

        print("Your move is : " + input_move + '. ' + out_str)

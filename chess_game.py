import copy
import chess_board

class ChessGame(object):

    column_names = ['a','b','c','d','e','f','g','h']
    line_names = ['1','2','3','4','5','6','7','8']
    player = 'white'

    def __init__(self):
        self.board = chess_board.ChessBoard()
        self.player = 'white'

    def run(self, play_generator = None):
        stay_in_game = True

        while(stay_in_game):
            self.board.print_board()
            stay_in_game = self.read_user_move(play_generator)

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


    def is_special_case(self, input_move):
        return self.is_end_of_game(input_move)

    def is_castling(self, input_move):
        res = input_move in ['O-O','O-O-O']
        return res 

    def is_short_castling(self,input_move):
        return input_move == 'O-O'

    def is_long_castling(self,input_move):
        return input_move == 'O-O-O'

    def is_end_of_game(self, input_move):
        res = input_move in ['1-0','0-1', '1/2-1/2']
        if res:
            print "End of game: " + input_move
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
        if len(input_move) < 4 or \
            input_move[-3] != 'x' or \
            (not self.are_coordinates_valid(input_move[-2], input_move[-1])):
            return False

        return (  ( len(input_move) == 4 
                    and (self.is_pawn(input_move) or self.is_main_piece(input_move)) 
                    ) 
                or 
                  ( len(input_move) == 5 
                    and ( self.is_main_piece(input_move))
                    and ( input_move[1] in self.column_names + self.line_names )
                    )
                or
                  ( len(input_move) == 6 
                    and ( self.is_main_piece(input_move))
                    and ( self.are_coordinates_valid(input_move[1], input_move[2]) )
                    )
                )

    def validate_move_case(self, input_move):

        if self.is_pawn(input_move):
            if len(input_move) != 2:
                return False
            return input_move[1] in self.line_names

        elif self.is_main_piece(input_move):

            if self.are_coordinates_valid(input_move[-2], input_move[-1]):
                return ( len(input_move) == 3
                        or
                        ( input_move[1] in self.column_names + self.line_names 
                        and 
                        len(input_move) == 4 )
                        or
                        ( self.are_coordinates_valid(input_move[1], input_move[2]) 
                        and 
                        len(input_move) == 5 )
                        )
            else:
                return False
        return False

    def is_valid_promotion(self, input_move, promoted_to):
        return (input_move[-1] in [ '1','8' ]) and (promoted_to in ['B','N','R','Q']) and (self.validate_move_case(input_move) or self.validate_eat_case(input_move))

    def is_user_move_valid(self, input_move):
        if len(input_move) <= 1:
            print 'wrong input try again'
            return False

        if self.is_check(input_move):
            print "CHECK"
            input_move = input_move[:-1]

        if self.is_castling(input_move):
            return True

        if self.is_special_case(input_move):
            return True

        if not self.is_pawn(input_move) and not self.is_main_piece(input_move):
            print 'case not valid, not a chess piece'
            return False

        if self.validate_eat_case(input_move):
            print 'valid eat input'
            return True

        if self.validate_move_case(input_move):
            print 'valid move input'
            return True

        promotion,input_move,promoted_to = self.is_promotion(input_move)

        if promotion:
            if not self.is_valid_promotion(input_move,promoted_to):
                return False
            else:
                return True

        print 'wrong input, try again'
        return False


    def are_coordinates_valid(self, col, line):
        return (line in self.line_names) and (col in self.column_names)
        
    def parse_user_move(self, input_move):
        # TODO: Handle ambiguities
        # TODO: Handle check, check-mate

        input_move = input_move.strip()

        if self.has_quit(input_move):
            return False

        if len(input_move)>1 and self.is_check(input_move):
            input_move = input_move[:-1]

        if not self.is_user_move_valid(input_move):
            return True

        promotion,input_move,promoted_to = self.is_promotion(input_move)

        move_to_col, move_to_line = None, None
        col_filter, line_filter = None, None

        if self.is_pawn(input_move):
            move_to_col, move_to_line, col_filter, line_filter = self.parse_pawn_coordinates(input_move)

        if self.is_main_piece(input_move):
            move_to_col, move_to_line, col_filter, line_filter = self.parse_main_pieces_coordinates(input_move)

        parallel_board = copy.deepcopy(self.board)
        accepted_move = self.move_piece_to(input_move, move_to_col, move_to_line, col_filter, line_filter)

        if promotion:
            self.board.promote( move_to_col, move_to_line, self.player, promoted_to )

        if self.board.Rules.is_king_under_attack(self.board,self.player):
            print "Cannot leave %s player in check!"%self.player
            accepted_move = False
            self.board = parallel_board

        if accepted_move:
            out_str = self.print_move(input_move, move_to_col, move_to_line)
            print("Your move is : " + input_move + '. ' + out_str)

            # avoid interference with tests
            if ( len(self.board.king_w)>0 and  len(self.board.king_b)>0 ): 

                if not self.board.Rules.can_opponent_keep_playing(self.board,self.player):
                    print "game over!"
                    if self.player == "white":
                        opponent = "black"
                    else:
                        opponent ="white"

                    if self.board.Rules.is_king_under_attack(self.board,opponent):
                        print "FATALITY %s wins!"%self.player
                    else:
                        print "FATALITY, no one wins!!"
                    return False
                else:
                    self.switch_player()

            else:                   
                self.switch_player()

        else:
            if self.is_special_case(input_move):
                print "we should reinitialize the board, let's try it"
                self.__init__()
                print "New Game!"
            #print "Move not accepted"

        return True

    def switch_player(self):
        print self.player
        if self.player == 'white':
            self.player = 'black'
            return
        self.player = 'white'
        return



    def parse_pawn_coordinates(self, input_move):
        col_filter, line_filter = None, None
        col,line = input_move[-2],input_move[-1]
        # ambiguities only if eating
        if self.piece_eats(input_move):
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
        if self.piece_eats(input_move):
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

    def piece_eats(self, input_move):
        return self.validate_eat_case(input_move)

    def move_piece_to(self, input_move, move_to_col, move_to_line, col_filter = None, line_filter = None):
        if self.is_castling(input_move):
            if self.is_short_castling(input_move):
                return self.board.castler(self.player,'short')
            else:
                return self.board.castler(self.player,'long')

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
            return self.board.piece_eater(kind, move_to_col,move_to_line,self.player, orig_col_filter = col_filter, orig_line_filter = line_filter)
        else:
            return self.board.piece_mover(kind, move_to_col,move_to_line,self.player, orig_col_filter = col_filter, orig_line_filter = line_filter)


    def print_move(self, input_move, move_to_col, move_to_line):
        out_str  = ""

        if self.is_short_castling(input_move):
            out_str = "Short castling for %s" % self.player
        
        elif self.is_long_castling(input_move):
            out_str = "long castling for %s" % self.player

        elif self.is_pawn(input_move):
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

        if not self.is_castling(input_move):
            if self.piece_eats(input_move):
                out_str = out_str + " and capture piece at (%s,%s)" % (move_to_col,move_to_line)
            else: 
                out_str = out_str + " to (%s,%s)" % (move_to_col, move_to_line)

        return  out_str

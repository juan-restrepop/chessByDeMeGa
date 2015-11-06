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

    def parse_user_move(self, input_move):
        if input_move == "q":
            return False
        print("Your move is : "+input_move)
        return True

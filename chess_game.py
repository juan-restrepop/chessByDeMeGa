import chess_board

class ChessGame(object):
    
    def __init__(self):
        self.board = chess_board.ChessBoard()

    def run(self):
        while(True):
            self.board.print_board()
            self.read_user_move()        

    def read_user_move(self):
        new_move_str = raw_input("Please enter a new move: \n")
        self.parse_user_move(new_move_str)

    def parse_user_move(self, input_move):
        print("Your move is : "+input_move)
        
        







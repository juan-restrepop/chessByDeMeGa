import sys
import pgn_reader
import chess_game

if __name__ == '__main__':
	
	c = chess_game.ChessGame()
	
	if len (sys.argv)>1:

		reader = pgn_reader.pgnBasicReader()
		c.run( reader.play_generator(sys.argv[1]) )
	
	else:
		c.run()

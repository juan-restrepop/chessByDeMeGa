import sys
import pgn_reader
import chess_game

if __name__ == '__main__':
	
	c = chess_game.ChessGame()
	
	if len (sys.argv)>1:
		try:
			reader = pgn_reader.pgnBasicReader()
			c.run( reader.play_generator(sys.argv[1]) )

		except IOError as e:
			print "Error #%s, "%e.errno,
			print e.strerror

		except:
			print "Unknown Error"

	else:
		c.run()

import sys
import pgn_reader
import chess_game

def run_chess():
    c = chess_game.ChessGame()
    
    if len (sys.argv)<=1:
        c.run()
        return

    try:
        reader = pgn_reader.pgnBasicReader()
        c.run( reader.play_generator(sys.argv[1]) )

    except IOError as e:
        print "Error #%s, "%e.errno,
        print e.strerror

    except EOFError as e:
        print "Ctrl-d: User quit"
        
    except Exception:
        raise

if __name__ == '__main__':
    run_chess()
    


import os

""" import module or run with:
    	$ python pgn_reader.py <pgn_file>
"""

class pgnBasicReader(object):

	def play_generator(self,filename):
		""" play_generator cuts a pgn file into single plays within single matches 
		    and gets rid of the turn number in the pgn format.
			For example, "1.e4 d5" generates "e4", "d5"

				Args: 
					string: chess-match filename of in pgn format.
				Returns:
					string: a play by play string generator
				Example:
					>>> pgn_reader = pgnBasicReader()
					>>> for play in pgn_reader.play_generator('my_chess_game.pgn'):
					>>>	    print play
		"""
		bare_game_gr = self.read_single_pgn_game(filename)
		return self.pgn_generator(bare_game_gr)

	def basic_fileobject_reader(self, file_object):
		""" basic_fileobject_reader:
				reads an open file_object
			    filters the pgn information and yields a cleaned up string with the plays
		"""
		out = ""
		for line in file_object:

			if self.pgn_meta_info(line):
				pass

			else:
				out = out + line.strip() + " "
				if self.hit_game_end(line.strip()):

					yield out
					out = ""
					interaction_str = raw_input("Press ENTER to continue, 'q' to quit\n")
					if interaction_str == 'q':
						break

	def pgn_meta_info(self, line):
		return line.strip() == "" or line.strip()[0] =='['

	def hit_game_end(self,line):
		if len(line.strip())>=3 and len(line.strip())<7:

			return line[-3:] in ['1-0','0-1']
		elif len(line.strip())>= 7:
			return line[-3:] in ['1-0','0-1'] or line[-7:] == '1/2-1/2'
		else:
			print "string too short"
			return False


	def read_single_pgn_game(self,filename):
		f = None
		bare_game_str = ""
		try:
			f = open(filename,'r')
			print "OPEN f%s"%filename
			yield self.basic_fileobject_reader(f)

		except IOError as e:
			print "IOError reading %s"%filename
			raise e

		finally:
			print "CLOSE f%s"%filename
			f.close()

	def pgn_generator(self, bare_game_str_gr):
		""" pgn_generator:
				Takes a bare game string generator as input
				yields a play string (1 move at a time)
		"""
		try:
			bare_game_str = bare_game_str_gr.next()

			for stuff in bare_game_str:
				k = 0
				nextk = 1

				while k < len(stuff)-1:
					# match empty character
					while nextk<len(stuff)-1 and stuff[nextk] not in [" ", '\n']:
						nextk+=1

					chunk_play = stuff[k:nextk]
					# skip turn number
					if '.' in chunk_play:
						chunk_play = chunk_play.split('.')[1]
					yield chunk_play

					# jump for next match. we already retrieved the patterns: now make inits for next match
					if stuff[nextk] in [" ", '\n']:
						# fix possible parsing error
						if nextk > len(stuff)-1:
							print "oh la la"
							break
						# re-initialize indexes
						else:
							k = nextk+1
							nextk = k+1
					else:
						# should not go here
						break
		except StopIteration:
			print "something bad may happen here"

# simple execution with 1 game
if __name__=="__main__":

	import sys
	
	if len (sys.argv)>1:
	
		pgn_reader = pgnBasicReader()
		
		print "start chess match"
		black = False
		for k in pgn_reader.play_generator(sys.argv[1]):

			player =  "w:" if not black else "b:"
			print player, k
			black = not black

		print "end chess match"

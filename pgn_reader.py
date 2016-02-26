import os

""" import module or run with: '$ python pgn_reader.py dataBase/Kasparov_game0001.pgn' """

class pgnBasicReader(object):

	def play_generator(self,filename):
		""" play_generator cuts a pgn file (with a single chessgame) into single 
		    plays and gets rid of the turn number.
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

		bare_game = self.read_single_pgn_game(filename)
		return self.pgn_generator(bare_game)

	def basic_fileobject_reader(self, file_object):
		out = ""
		for line in file_object.readlines():

			if self.pgn_meta_info(line):
				pass
			else:
				out = out + line.strip() + " "

				if self.hit_game_end(line):
					break
		return out

	def pgn_meta_info(self, line):
		return line.strip() == "" or line.strip()[0] =='['

	def hit_game_end(self,line):
		if len(line.strip())>=3 and len(line.strip())<7:
			return line[-3:] in ['1-0','0-1']
		elif len(line.strip())>= 7:
			return line[-7:] in ['1-0','0-1','1/2-1/2']
		else:
			return False


	def read_single_pgn_game(self,filename):
		f = None
		bare_game = ""
		try:
			f = open(filename,'r') 
			bare_game = ""
			bare_game = self.basic_fileobject_reader(f)
			f.close()

		except IOError as e:
			print "IOError reading %s"%filename
			raise e
		return bare_game
		

	def pgn_generator(self, bare_game_str):
		k = 0
		nextk = 1

		while k < len(bare_game_str):
			# match empty character
			while nextk<len(bare_game_str)-1 and bare_game_str[nextk] not in [" ", '\n']:
				nextk+=1

			chunk_play = bare_game_str[k:nextk]

			# from here on: bare_game_str[nextk] == " "
			if '.' in chunk_play:
				chunk_play = chunk_play.split('.')[1]

			yield chunk_play

			# jump for next match
			if bare_game_str[nextk] in [" ", '\n']:
				
				if nextk > len(bare_game_str)-1:
					print "oh la la"
					break
				else:
					k = nextk+1
					nextk = k+1
			else:
				# should not go here
				break

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


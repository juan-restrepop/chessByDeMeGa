import os

class pgnBasicReader(object):

	def read_single_pgn_game(self,filename):
		f = None
		try:
			f = open(filename,'r') 
			for line in f.readlines():
				# read line by line?
				print line

			f.close()
		except IOError as e:

			print "io error reading %s"%filename
			raise e

if __name__=="__main__":
	import sys
	
	if len (sys.argv[0])>1:
	
		pgn_reader = pgnBasicReader()
		pgn_reader.read_single_pgn_game(sys.argv[1]) 
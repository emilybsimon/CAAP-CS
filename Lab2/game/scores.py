class Score(object):
	name = 'player'
	score = 0
	placement = 0 

	# initializes score and players name
	def __init__(self, name, score):
		self.name = name
		self.score = score

	# returns the name associated with score
	def get_name(self):
		return self.name

	# returns score of player
	def get_score(self):
		return self.score
	
	def set_score(self, newScore):
		self.score = newScore
		
	def set_name(self, newName):
		self.name = newName
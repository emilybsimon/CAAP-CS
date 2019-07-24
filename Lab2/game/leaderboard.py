# imports the score class to be used in the leaderboard.
from scores import Score

# leaderboard keeps track of top ten highest ranking players
class Leaderboard(object):
	size = 5
	board = []

	def __init__(self):
		for i in range(self.size):
			self.board.append(Score(str("player "+str(i)), 0))

	# prints the leaderboard
	def print_board(self):
		print("Leaderboard:")
		print()
		for entry in self.board:
			player = entry.get_name()
			score = entry.get_score()
			print(player+ ": ", score)

	# checks if given score should be in the leaderboard
	def update(self, score):
		i=0
		for status in self.board:
			if (score.get_score() >= status.get_score()):
				if i == self.size-1:
					return
				else:
					temp = range[i:size-1]
					self.board[i] = score
					self.board[i+1:size] = temp
					break
			i +=1
# inserts the score in the given position (assuming it's better or equal to the one in the given rank)
	# moving everything below down a rank
	# def insert(self, score, i):
	
sample = Leaderboard()
sample.print_board()
# imports multiple clases from the python library and some of our
# own modules.
from sys import exit
from random import randint
from map import Map
from leaderboard import Leaderboard
from scores import Score
from game_engine import Engine

# global variables to keep track of score, player, and leaderboard

moves = 0
name = ""
leaderboard = Leaderboard()

# what happens when the game is over
# takes in a boolean parameter
# should update leaderboard, global variables, and print leaderboard
def game_over(won):
	global name
	global moves
	score = Score(name, moves)
	if won:
            leaderboard.update(score)
	print ("\nGame Over.")
	name= ""
	moves = 0
	leaderboard.print_board()

# initializes/updates global variables and introduces the game.
# starts the Map and the engine.
# ends the game if needed.
def play_game():
	while True:
		global name 
		global moves 
		print ("This game is a challenge! To quit enter :q at any time. Good luck!") 
		name = input("\n Player name. > ") 
		if (name == ':q'):
			exit(1) 
		else:
			print ("Choose your difficulty level: 1-3. 1 is easiest, 3 is hardest.:")
			diff = input("\n Difficulty. > ")
			a_map = Map('central_corridor') # This calls the starting location.
			a_game = Engine(a_map, diff)
			moves = a_game.play()
			game_over(a_game.won())

play_game()

def test_game():
    test_playgame = game_over()
    test_playgame2 = play_game()
test_game()
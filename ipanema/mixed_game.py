from conversion import full_check	
from numbered_game import set_number_of_games
from infinite_game import set_infinite
from content import game_content
from select_game_size import select_game_size
import random

def mixed_game():
	game_type = select_game_size()

	def play(game_type):
		game_cont = game_content()

		print(game_cont)

		if game_type == True or game_type > 0:
			rand_ = random.randrange(0,2)
			print(f'random number switch {rand_}\n')
			if rand_ == 0:				# Name
				print(f'Question -- {game_cont[0]}')
				ans = input('What is the answer? \n')
				check_ans(ans, game_cont)
			elif rand_ == 1:		# Port
				print(f'Question -- {game_cont[1]}')
				ans = input('What is the answer? \n')
				check_ans(ans, game_cont)
			return play(game_type or game_type - 1)
		else:
			print(f'You have {abs(numbered)} games left, buck up or bon voyage!')

	play(game_type)


def check_ans(ans, key):
	full_check(ans, key[1])
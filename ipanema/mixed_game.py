from conversion import full_check	
from numbered_game import set_number_of_games
from infinite_game import set_infinite
from content import game_content
from select_game_size import select_game_size
import random

def mixed_game():
	select_game_size()

	print(infinite)
	print(numbered)

	def play(infinite, numbered):
		game_cont = game_content()

		if infinite == True or numbered > 0:
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
			return play(infinite, numbered - 1)
		else:
			print(f'You have {abs(numbered)} games left, buck up or bon voyage!')

	play(infinite, numbered)


def check_ans(ans, key):
	print('not done')
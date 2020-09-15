from conversion import full_check	
from numbered_game import set_number_of_games
from infinite_game import set_infinite
from content import game_content
import random

infinite = False
numbered = 0

def select_game_size():
	global infinite
	global numbered
	print('Now, select your games size:\n')
	print('Enter 1 for Infinite games')
	print('Enter 2 to select the number of games you want to play\n')
	selection = int(input('Which one?'))
	
	if selection == 1:
		print('\nInfinite was selected')
		infinite = True
	elif selection == 2:
		print('\nNumbered was selected')
		numbered = set_number_of_games()
	return 

def mixed_game():
	select_game_size()

	print(infinite)
	print(numbered)

	def play(infinite, numbered):
		game_cont = game_content()

		if infinite == True or numbered > 0:
			rand_ = random.randrange(0,2)
			print(f'random number switch {rand_}')
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
			print(f'You\'ve played all your games {abs(numbered)}, bon voyage!')

	play(infinite, numbered)


def check_ans(ans, key):
	print('not done')

	# if rand_ == 0:		# Name
	# 	full_check(ans, key[1])
	# elif rand_ == 1:	# Port
	# 	full_check(ans, key[0])
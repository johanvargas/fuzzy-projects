from conversion import full_check	
from numbered_game import set_number_of_games
from infinite_game import set_infinite

infinite = False
numbered = 0

def select_game_size():
	global infinite
	global numbered
	print('Now, select your games size:\n')
	print('Enter 1 for Infinite games')
	print('Enter 2 to select the number of games you want to play')
	selection = int(input('Which one?'))
	
	if selection == 1:
		print('Infinite was selected')
		infinite = True
	elif selection == 2:
		print('Numbered was selected')
		numbered = set_number_of_games()
	return 

def name_game(game_):
	select_game_size()

	print(infinite)
	print(numbered)

	if infinite == True or numbered > 0:
		print(f'initial num = {numbered}')
		print(f'Question -- {game_[0]}')
		print(f'num = {numbered}')
		ans = input('What is the answer? \n')
		check_ans(ans, game_)
		#print(f'Answer -- {game_[1]}')
	else:
		print('error')

def check_ans(ans, key):
	full_check(ans, key[1])


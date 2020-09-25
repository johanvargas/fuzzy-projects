from conversion import full_check	
from numbered_game import set_number_of_games
from infinite_game import set_infinite
from content import game_content
from select_game import select_game_size

infinite = False
numbered = 0

def name_game():
	select_game_size()

	print(infinite)
	print(numbered)

	def play(infinite, numbered):
		game_cont = game_content()

		if infinite == True or numbered > 0:
			print(f'initial num = {numbered}')
			print(f'Question -- {game_cont[0]}')
			print(f'num = {numbered}\n')
			ans = input('What is the answer? \n')
			check_ans(ans, game_cont)
			if infinite == True:
				play_again = str(input('play again?(y/n)'))
				if play_again == 'y':
					return play(infinite, numbered - 1)
		else:
			print(f'You\'ve played all your games {abs(numbered)}, bon voyage!')

	play(infinite, numbered)

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

def check_ans(ans, key):
	full_check(ans, key[1])

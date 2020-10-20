from conversion import full_check	
from numbered_game import set_number_of_games
from infinite_game import set_infinite
from content import game_content
from select_game_size import select_game_size

def port_game():
	game_type = select_game_size()
	print(game_type)

	def play(infinite, numbered):
		game_cont = game_content()

		if infinite == True or numbered > 0:
			print(f'initial num = {numbered}')
			print(f'Question -- {game_cont[1]}')
			print(f'num = {numbered}')
			ans = input('What is the answer? \n')
			check_ans(ans, game_cont)
			if infinite == True:
				play_again = str(input('play again?(y/n)'))
				if play_again == 'y':
					return play(infinite, numbered - 1)
		else:
			print(f'You\'ve played all your games {abs(numbered)}, bon voyage!')

	play(infinite, numbered)

def check_ans(ans, key):
	full_check(ans, key[0])

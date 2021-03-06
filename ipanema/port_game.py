from conversion import full_check	
from numbered_game import set_number_of_games
from infinite_game import set_infinite
from content import game_content
from select_game_size import select_game_size

def port_game():
	game_type = select_game_size()

	def play(game_type):
		# print('Game Type', game_type)

		if game_type[0] == 'Infinite' and game_type[1] == True:
			# print('Infinite Selected')
			
			port_game_module(game_type)
			q = input('Do you want to continue?\n(Enter to continue, anything else to exit)	')
			if not q:
				return play(game_type)
			else:
				game_type[1] = False 

		if game_type[0] == 'Numbered' and game_type[1] == True:
			num = set_number_of_games()
			# print('Numbered Selected')
			print('Number of games is ', num)
			while num > 0:
				port_game_module(game_type)
				num -= 1

	play(game_type)

def port_game_module(game_type):
	game_cont = game_content()
	# print('Game Answers', game_cont)
	print(f'What\'s the port that runs the service named {game_cont[1]}')
	ans = input('What is the answer?	\n')
	full_check(ans, game_cont[0])

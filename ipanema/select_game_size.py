from numbered_game import set_number_of_games

def select_game_size():
	infinite = False
	numbered = 0

	print('Now, select your games size:\n')
	print('Enter 1 for Infinite games')
	print('Enter 2 to select the number of games you want to play\n')
	selection = int(input('Which one?'))
	
	if selection == 1:
		print('\nInfinite was selected')
		infinite = True
		return infinite
	elif selection == 2:
		print('\nNumbered was selected')
		numbered = set_number_of_games()
		return numbered
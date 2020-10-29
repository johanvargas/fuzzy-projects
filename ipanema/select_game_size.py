def select_game_size():
	numbered = 0

	print('Now, select your games size:\n')
	print('Enter 1 for Infinite games')
	print('Enter 2 to select the number of games you want to play\n')
	selection = int(input('\v ^^ ^^^ Your choice Captian?\v ^^^ ^ '))
	
	if selection == 1:
		return ['Infinite', True] 
	elif selection == 2:
		return ['Numbered', True]
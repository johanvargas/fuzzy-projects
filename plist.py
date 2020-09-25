import sys
import random
import time
from name_game import name_game
from port_game import port_game
from mixed_game import mixed_game

def game_type():
	print('You have three options:\n')
	print('Name Game - where you name the port number (Enter 1)')
	print('Port Game - Where you number the name (Enter 2)')
	print('Mixed Game - Where you randomly get either one (Enter 3)\n')
	
	type_input = input('type?')
	
	return game_select(type_input)

def game_select(quest_type):
	print(f'\ntype : {quest_type}\n')

	def game_setup():
		# Sets type of game: name, port, mixed
		if int(quest_type) == 1:		# Name
			name_game()
		elif int(quest_type) == 2:		# Port
			port_game()
		elif int(quest_type) == 3:		# Mixed
			mixed_game()

	return game_setup()

def main():

	assert(sys.platform), sys.platform
	print('Welcome... You have docked at the PORT OF SAN IPANEMA!\n')
	print('Select a Game Type:\n')
	game_type()

if __name__ == '__main__':
	main()
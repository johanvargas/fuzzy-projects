"""

Ports of San IPanema
version 0.01
By Johan Alberto Vargas

"""
import sys
import random
import time
from name_game import name_game
from port_game import port_game
from mixed_game import mixed_game

def game_type():
	print('You have three options:\n')
	print('Name Game - Where you name the port number (Enter 1)')
	print('Port Game - Where you number the name (Enter 2)')
	print('Mixed Game - Where you randomly get either one (Enter 3)\n')
	
	type_input = int(input('What\'s your journey?'))
	
	return game_select(type_input)

def game_select(quest_type):

	def game_setup():
		# Sets type of game: name, port, mixed
		if quest_type == 1:		
		# Name
			name_game()
		elif quest_type == 2:		
		# Port
			port_game()
		elif quest_type == 3:		
		# Mixed
			mixed_game()

	return game_setup()

def main():
	print('\nWELCOME... You have docked at the PORT OF IPANEMA!\n')
	print('Select a Game Type:\n')
	game_type()

if __name__ == '__main__':
	main()
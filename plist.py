#!/usr/bin/env python3
import requests
import random
import time
from bs4 import BeautifulSoup
from conversion import full_check

def game_type():
	print('You have three options:\n')
	print('Name Game - where you name the port number (Enter 1)')
	print('Port Game - Where you number the name (Enter 2)')
	print('Mixed Game - Where you randomly get either one (Enter 3)\n')
	
	type_input = input('type?')
	

	return game_select(type_input, 'Infinite')

def game_select(quest_type, game_size):
	print(f'game size : {game_size}\nquest type : {quest_type}\n')

	# There needs to be some text cleaning here. Making sure the input is valid.

	def game_setup():
		# Sets the question and answer for the 'card'
		game_ = actual_game(quest_type)

		# Helper functions

		def check_ans(ans, key, quest_type):
			if int(quest_type) == 1:		# Name
				full_check(ans, key[1])
				#print(f'Answer -- {game_[1]}')
			elif int(quest_type) == 2:		# Port
				print(f'Question -- {game_[1]}')
				print(f'Answer -- {game_[0]}')
			elif int(quest_type) == 3:		# Mixed
				print('Mixed Game')
				rand_ = random.randrange(0,2)
				print(f'random number switch {rand_}')
				if rand_ == 0:		# Name
					print(f'Question -- {game_[0]}')
					print(f'Answer -- {game_[1]}')
				elif rand_ == 1:		# Port
					print(f'Question -- {game_[1]}')
					print(f'Answer -- {game_[0]}')

		# End of Helper functions

		# This def needs some cleaning up.
		# Sets type of game: name, port, mixed
		if int(quest_type) == 1:		# Name
			print(f'Question -- {game_[0]}')
			ans = input('What is the answer? \n')
			check_ans(ans, game_, quest_type)
			#print(f'Answer -- {game_[1]}')
		elif int(quest_type) == 2:		# Port
			print(f'Question -- {game_[1]}')
			print(f'Answer -- {game_[0]}')
		elif int(quest_type) == 3:		# Mixed
			print('Mixed Game')
			rand_ = random.randrange(0,2)
			print(f'random number switch {rand_}')
			if rand_ == 0:		# Name
				print(f'Question -- {game_[0]}')
				print(f'Answer -- {game_[1]}')
			elif rand_ == 1:		# Port
				print(f'Question -- {game_[1]}')
				print(f'Answer -- {game_[0]}')

	def actual_game(quest_type):
		page = requests.get('https://www.webopedia.com/quick_ref/portnumbers.asp')
		soup = BeautifulSoup(page.content, 'html.parser')
		spoonful = soup.find_all('td')
		list_it = list(spoonful)
		length = len(list_it)

		r = random.randrange(0, length)
		# print(f'game ready for {quest_type} : {r}')

		if r % 2 == 0 :
			print(list_it[r].text, list_it[r+1].text)
			return [list_it[r].text, list_it[r+1].text]
		else:
			return actual_game(quest_type)

	return game_setup()


def main():
	print('Welcome... You have docked at the PORT OF SAN IPANEMA!\n')
	print('Select a Game Type:\n')
	game_type()

if __name__ == '__main__':
	main()
#!/usr/bin/env python3
import requests
import random
import time
from bs4 import BeautifulSoup
# from conversion import full_check
from name_game import name_game

def game_type():
	print('You have three options:\n')
	print('Name Game - where you name the port number (Enter 1)')
	print('Port Game - Where you number the name (Enter 2)')
	print('Mixed Game - Where you randomly get either one (Enter 3)\n')
	
	type_input = input('type?')
	

	return game_select(type_input)

def game_select(quest_type):
	print(f'type : {quest_type}\n')

	def game_setup():
		# Sets the question and answer for the 'card'
		game_ = actual_game(quest_type)

		# This def needs some cleaning up.
		# Sets type of game: name, port, mixed
		if int(quest_type) == 1:		# Name
			name_game(game_)
		elif int(quest_type) == 2:		# Port
			print('port')
		elif int(quest_type) == 3:		# Mixed
			print('mixed')

	return game_setup()

def actual_game(quest_type):
	# Content for game

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

def main():
	print('Welcome... You have docked at the PORT OF SAN IPANEMA!\n')
	print('Select a Game Type:\n')
	game_type()

if __name__ == '__main__':
	main()
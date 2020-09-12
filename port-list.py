ddddddddd#!/usr/bin/env python3
import requests
import random
import time
from bs4 import BeautifulSoup

"""

Ports of San IPanema
version 0.01
By Johan Alberto Vargas

"""

def game_type():
	# The start of the game. Introduces rules and sets up params for play

	print('You have two options:')
	print('You can select and Infinity Game - Where it continuosly answer Questions until you quit (Enter 1)')
	print('Or you can select the number of Questions you want in a Session (Enter 2)')
	selekt = int(input('What is your decision? '))	
	
	# Inputs need some formatting to make sure the types are consistent.
	# <selekt> selects number of games, either infinte or numbered.
	# then prompts for selection of game type - number, name, mixed quest.
	
	print(f"Great, you selected {selekt}\n")
	print('-->Now what type of game do you want to play?')
	print('--->You have three options\n')
	print('----->Option 1 - A Number Quest, where you answer the name of the corresponding port.')
	print('-------->Option 2 - A Name Quest, where you answer with the port number to the corresponding name.')
	print('------------->Option 3 - A Mixed Quest, where either a Name or a Number Quest is thrown at your weak little mind')
	print('\n')

	quest_type = int(input('So, what say you? enter the number of your fate... \n'))

	print('\nSelecting game type...\n')
	if selekt == 1:
		print('Infinite Game was selected\n')
		sel1 = game_select(selekt, quest_type)	# Infinite Games
	elif selekt == 2:
		print('Numbered Game was selected\n')
		sel2 = game_select(selekt, quest_type)	# Numbered Games
	else:
		print('Naughty, not an option! Starting over...')
		return game_type()

def game_select(game_num, quest_type):
	# if game_num == 1:
	# 	game_inf(quest_type)
	# elif game_num == 2:
	# 	game_20(quest_type)
	# else:
	# 	print('Naughty, not an option! Starting over...')
	# 	return game_type()
	print('\ngame_select initiated ... this selects the game size\n')
	switcher = {
		1: game_inf(quest_type),
		2: game_20(quest_type)
	}

	return switcher.get(game_num, game_type())

def game_20(quest_type):
	print(f' game_20 selected, {quest_type}: quest type number ... this then moves to the_game to initiate actual game...\n')
	question_num = input('How many questions do you want to play? ')
	print(f'Great,{question_num} questions it is!\n')
	the_game(question_num, quest_type)


def game_inf(quest_type):
	print(f' game_20 selected, {quest_type}: quest type number ... this then moves to the_game to initiate actual game...\n')
	print('Ok, lets get started! Good Luck!')
	the_game(False, quest_type)


def the_game(number_of_questions, quest_type):

	print(f'\nthe_game ---> number of questions : {number_of_questions}, quest type ---> {quest_type}\n')

	# Content for game
	page = requests.get('https://www.webopedia.com/quick_ref/portnumbers.asp')
	soup = BeautifulSoup(page.content, 'html.parser')
	spoonful = soup.find_all('td')
	list_it = list(spoonful)
	length = len(list_it)

	def name_quest(number_of_questions, cool):

		# shifts the question_selection to odd; conversion to name quest.
		def make_odd():
			question_selector = random.randrange(0, length)
			if question_selector % 2 == 0:
				return make_odd()
			else:
				return int(question_selector)

		if number_of_questions == False:
			if cool == 'y':
				print('infinite name quest selected')
				index = make_odd()
				fact = list_it[index].text
				fact_answer = list_it[index - 1].text
				answer = input(f'what is the port number for the port named {fact}? ')
				print(f'the answer is {fact_answer}')
				check = input('play again? (y/n)')
				print(f' answer selected : {check}')
				return name_quest(False, check)
			else:
				exit()
		else:
			num = int(number_of_questions)
			print(f'number_of_questions is {number_of_questions}')
			print('numbered name quest selected')
			
			while num >= 0:
				index = make_odd()
				question_selector = random.randrange(0, length, 2)
				fact = list_it[index].text
				fact_answer = list_it[index - 1].text
				answer = input(f'what is the port name for port number {fact} ')
				print(f'the answer is {fact_answer}')
				num-=1
			else:
				exit()

	def number_quest(number_of_questions, cool):
		if number_of_questions == False:
			if cool == 'y':
				print('infinite number quest selected')
				question_selector = random.randrange(0, length, 2)
				fact = list_it[question_selector].text
				fact_answer = list_it[question_selector + 1].text
				answer = input(f'what is the port name for port number {fact} ')
				print(f'the answer is {fact_answer}')
				check = input('play again? (y/n)')
				print(f' answer selected : {check}')
				return number_quest(False, check)
			else:
				exit()
		else:
			num = int(number_of_questions)
			print(f'number_of_questions is {number_of_questions}')
			print('numbered number quest selected')
			while num >= 0:
				question_selector = random.randrange(0, length, 2)
				fact = list_it[question_selector].text
				fact_answer = list_it[question_selector + 1].text
				answer = input(f'what is the port name for port number {fact} ')
				print(f'the answer is {fact_answer}')
				num-=1
			else:
				exit()

		print('End of Number Quest')

	def mixed_quest(number_of_questions, cool):
		print('mixed gamed selected')
		print(f'number_of_questions : {number_of_questions}, cool : {cool}')
		high_low = random.randrange(0, 2)

		# switchy = {
		# 	0: name_quest(number_of_questions, cool),
		# 	1: number_quest(number_of_questions, cool)
		# }

		print(f'{high_low}')
		return 

	if quest_type == 1:
		number_quest(number_of_questions, 'y')
	elif quest_type == 2:
		name_quest(number_of_questions, 'y')
	elif quest_type == 3:
		mixed_quest(number_of_questions, 'y')

def main():
	print('Welcome... You have docked at the PORT OF SAN IPANEMA!\n')
	print('Select a Game Type:\n\n')
	game_type()

if __name__ == '__main__':
	main()
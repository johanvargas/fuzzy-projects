#!/usr/bin/env python3
import requests
import random
import time
from bs4 import BeautifulSoup
# import re

"""
PORTS of SAN IPANEMA

Things to add

Session view
	start a game session
	track right and wrong answers.
	points system
	reward system??

Game platform that compiles a system of learning for user.

User selects a topic.
	db created of 
		factoids
		flash cards
		quizes
		vid references
		pdf referecnces
		imgs
		resources 

It could learn your learning habits and feed info accordingly

Not in use as of now, 08132020

def selector(num):
	next = int(num)
	print(f'The number you selected is : {num}\n')
	ans = next
	return ans

Main Game

def find_the_pair():
	# 0, 1 initial pairing from list, list_it
	# then, even number is port number, p
	# odd port name, p + 1

"""


def game_type():
	print('You have two options:')
	print('You can select and Infinity Game - Where it continuosly answer Questions until you quit (Enter 1)')
	print('Or you can select the number of Questions you want in a Session (Enter 2)')
	selekt = int(input('What is you decision? ')) # This needs some formatting to make sure the types are consistant.
	print(f"Great, you selected {selekt}\n")
	print('Now what type of game do you want to play?')
	print('You have three options')
	print('Option 1 - A Number Quest, where you answer the name of the corresponding port.')
	print('Option 2 - A Name Quest, where you answer with the port number to the corresponding name.')
	print('Option 3 - A Mixed Quest, where either a Name or a Number Quest is thrown at your weak little mind')
	quest_type = int(input('So, what say you? enter the number of your fate... '))

	if selekt == 1:
		sel1 = game_select(1, quest_type)
	elif selekt == 2:
		sel2 = game_select(2, quest_type)
	else:
		print('Naughty, not an option! Starting over...')
		return game_type()

def game_select(game_num, quest_type):
	if game_num == 1:
		game_inf(quest_type)
	elif game_num == 2:
		game_20(quest_type)
	else:
		print('Naughty, not an option! Starting over...')
		return game_type()

def game_20(quest_type):
	question_num = input('How many questions do you want to play? ')
	print(f"Great,{question_num} questions it is!")
	the_game(question_num, quest_type)


def game_inf(quest_type):
	print('Ok, lets get started! Good Luck!')
	the_game(0, quest_type)


def the_game(number_of_questions, quest_type):
	# Pull port number resource

	page = requests.get('https://www.webopedia.com/quick_ref/portnumbers.asp')

	# print(page.status_code) # What is this for? ADD COMMENTS!
	# print(page.content)		# What is this for? ADD COMMENTS!

	soup = BeautifulSoup(page.content, 'html.parser')
	# soup_table = soup.table 	# What is this for? ADD COMMENTS!
	spoonful = soup.find_all('td')
	list_it = list(spoonful)
	length = len(list_it)

	print(number_of_questions, quest_type)

	def name_quest(number_of_questions, cool):
		if cool == 'y':
			def make_odd():
				question_selector = random.randrange(0, length)
				if question_selector % 2 == 0:
					return make_odd()
				else:
					return int(question_selector)

			index = make_odd()

			fact = list_it[index].text
			fact_answer = list_it[index - 1].text
			answer = input(f'what is the port number for the port named {fact}? ')
			print(f'the answer is {fact_answer}')
			check = input('play again? (y/n)')
			return name_quest(number_of_questions, check)
		else:
			return

	def number_quest(number_of_questions, cool):
		if cool == 'y':
			question_selector = random.randrange(0, length, 2)
			fact = list_it[question_selector].text
			fact_answer = list_it[question_selector + 1].text
			answer = input(f'what is the port name for port number {fact} ')
			print(f'the answer is {fact_answer}')
			check = input('play again? (y/n)')
			return number_quest(number_of_questions, check)
		else:
			return


	def mixed_quest(number_of_questions):
		pass

	if quest_type == 1:
		number_quest(number_of_questions, 'y')
	elif quest_type == 2:
		name_quest(number_of_questions, 'y')
	elif quest_type == 3:
		mixed_quest()

def main():
	print('Welcome... You have docked at the PORT OF SAN IPANEMA!\n')
	print('Select a Game Type:\n\n')
	game_type()

# 	if True:

# 		print('Ok.. lass uns spielen..')
# 		# time.sleep(2)
# 		print('The game consists of answering the correct name or port based on the info given\n')
# 		print('If you don\'t know or want to move to the next question, type idk')
# 		q_port = list_it[r]
# 		print(f'The port is : {q_port.text}')

# 		question = input('What is the corresponding service associated with this port? \n')
# 		answer = question

# 		if answer == list_it[r + 1].text:
# 			print('Sehr gut!')
# 			return find_the_pair()
# 		elif answer == 'idk':
# 			return find_the_pair()
# 		else:
# 			print('Tut mir leid, das is nicht die richtige Antwort!\n')
# 			print(f'{list_it[r + 1].text.upper()} ist das Antwort.\n\n')

# 		prompter = input('willst du nochmal spielen? \nType ja to play again\nOr press ENTER to exit\n')
# 		if prompter == 'ja':
# 			return find_the_pair()
# 		else:
# 			pass

# 		pass

if __name__ == '__main__':
	main()




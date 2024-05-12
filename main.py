#!/usr/bin/env python3
import requests
import random
import time
from bs4 import BeautifulSoup
# import re

page = requests.get('https://www.webopedia.com/quick_ref/portnumbers.asp')

# print(page.status_code)
# print(page.content)

soup = BeautifulSoup(page.content, 'html.parser')
# soup_table = soup.table
spoonful = soup.find_all('td')

list_it = list(spoonful)

length = len(list_it)

def selector(num):
	next = int(num)
	print(f'The number you selected is : {num}\n')
	ans = next
	return ans

def find_the_pair():
	# even port number, p
	# odd port name, p + 1

	r = random.randrange(0, length, 2)

	if True:

		print('Ok.. lass uns spielen..')
		# time.sleep(2)
		print('The game consists of answering the correct name or port based on the info given\n')
		q_port = list_it[r]
		print(f'The port is : {q_port.text}')

		question = input('What is the corresponding service associated with this port? \n')
		answer = question

		if answer == list_it[r + 1].text:
			print('Sehr gut!')
			return find_the_pair()
		else:
			print('Tut mir leid, das is nicht die richtige Antwort!\n')
			print(f'{list_it[r + 1].text.upper()} ist das Antwort.\n\n')

		prompter = input('willst du nochmal spielen? \nType ja to play again\nOr press ENTER to exit\n')
		if prompter == 'ja':
			return find_the_pair()
		else:
			pass

		return 


game = find_the_pair()

print(game)


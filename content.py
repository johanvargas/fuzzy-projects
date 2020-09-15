import requests
from bs4 import BeautifulSoup
import random

def game_content():
	# Content for game

	page = requests.get('https://www.webopedia.com/quick_ref/portnumbers.asp')
	soup = BeautifulSoup(page.content, 'html.parser')
	spoonful = soup.find_all('td')
	list_it = list(spoonful)
	length = len(list_it)

	r = random.randrange(0, length)

	if r % 2 == 0 :
		print(list_it[r].text, list_it[r+1].text)
		return [list_it[r].text, list_it[r+1].text]
	else:
		return game_content()
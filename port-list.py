#!/usr/bin/env python3
import requests
from bs4 import BeautifulSoup

print('libraries are ok. move on.')

page = requests.get('https://www.webopedia.com/quick_ref/portnumbers.asp')

# print(page.status_code)
# print(page.content)

soup = BeautifulSoup(page.content, 'html.parser')

soup_table = soup.table

spoonful = soup.find_all('td')

list_it = list(spoonful)

length = len(list_it)

for i in range(0, length, 2):
	print(list_it[i].text, list_it[i + 1].text)


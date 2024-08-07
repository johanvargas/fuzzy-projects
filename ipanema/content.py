import requests
from bs4 import BeautifulSoup
import random
import sys

def game_content():
    # Content for game
    # Needs a network connection error msg
    # the webopedia changed their website, so now this link doesn't work

    page = requests.get('https://www.webopedia.com/quick_ref/portnumbers.asp')
    if page.status_code != '200':
        print("error: exited with status : ", page.status_code)
        sys.exit('We are done here, sorry')
    # Parse html
    soup = BeautifulSoup(page.content, 'html.parser')
    spoonful = soup.find_all('td')
    list_it = list(spoonful)
    length = len(list_it)

    r = random.randrange(0, length)

    # Use modulus to get the right order of question/answer pair.
    # Which sounds like it should get parsed in a dict or obj
    if r % 2 == 0 :
            # print(list_it[r].text, list_it[r+1].text)
            return [list_it[r].text, list_it[r+1].text]
    else:
            return game_content()

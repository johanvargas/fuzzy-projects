#!/usr/bin/python3
# Scrap images from URL
# more importantly it needs to follow links and find the base url for image and
# download that.

import subprocess, sys, requests
from bs4 import BeautifulSoup
from requests.exceptions import HTTPError

# url = "https://www.google.com"
# url ="https://fapello.com/sakurawaifu/"
# https://youtube.com

# user url input
# need a url verifier
url = input("Enter URL: ")
verified_url = url if len(url) < 0 else "https://www.youtube.com"

# collecting response data
content = None # http file
link_source = []

def parse_url(soup):
    # print(soup.prettify())
    links = soup.find_all('a')
    # print(links)
    for l in links:
        link_source.append(l)
        #print( "image link: " + l.get('src'))

    #print(type(soup))
    print("Number of links found: " + str(len(link_source)))
    
    for l in link_source:
        print(f"link is : {l}")
    #print(soup.get_text())

try:
    response = requests.get(verified_url)
    print("HTTP Response: " + str(response.status_code))
    content = response.content

    # create bs4 obj
    soup = BeautifulSoup(content, 'html.parser')

    # parse data
    parse_url(soup)

except HTTPError as httper:
    print(httper)
except Exception as err:
    print(err)
else:
    print("\nLink collection completed!")

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

url = input("Enter URL: ")
content = None # http file
link_source = []
response = requests.get(url)

try:
    response = requests.get(url)
    print("HTTP Response: " + str(response.status_code))
    content = response.content
    soup = BeautifulSoup(content, 'html.parser')
    # print(soup.prettify())
    links = soup.find_all('a')
    # print(links)
    for l in links:
        link_source.append(l)
        #print( "image link: " + l.get('src'))
except HTTPError as httper:
    print(httper)
except Exception as err:
    print(err)
else:
    print("\nLink collection completed!")

print(type(soup))
print(len(link_source))
#print(soup.get_text())

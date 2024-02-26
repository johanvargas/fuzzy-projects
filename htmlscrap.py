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
verified_url = url if len(url) < 0 else "https://fapello.com/sakurawaifu/"

# collecting response data
link_source = []
img_source = []

def parse_url(soup):
    # print(soup.prettify())
    links_a = soup.find_all('a')
    links_img= soup.find_all('img')
    for l in links_a:
        link_source.append(l)

    for l in links_img:
        img_source.append(l.get('src'))

    print(f"{str(len(link_source))} links were found")
    
    if len(img_source) == 0:
        print("No images were found on this page")
    else:
        for src in img_source:
            print("Image source: " + src)

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
    print("\nScrap Finished!!")

#!/usr/bin/python3
# Scrap images from URL
# more importantly it needs to follow links and find the base url for image and
# download that.

import subprocess, sys, requests, random, os
from bs4 import BeautifulSoup
from requests.exceptions import HTTPError
from urllib.request import urlretrieve

# user url input
# need a url verifier
url = input("Enter URL: ")
verified_url = url if len(url) > 0 else "https://fapello.com/sakurawaifu/"

# collecting response data
link_source = []
img_source = []

def download_img(url):
    path = "/tmp/"
    try:
        res = requests.get(url)
        img = open(f"{os.path.join(path, str(random.randrange(1000000)))}.jpg" ,'wb')
        img.write(res.content)
        img.close()
    except Exception as err:
        print(f"Oops! Something went wrong while trying to download image {err}")

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
            download_img(src)
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

#!/usr/bin/python3

import subprocess, sys, requests, random, os
from bs4 import BeautifulSoup
from requests.exceptions import HTTPError
from urllib.request import urlretrieve

# ascii esc key colors
WHITE="\033[1;37m"
YELLOW="\033[0;31m"
RED="\033[0;33m"
GREEN="\033[0;32m"
RESET="\033[0m"

# collecting response data

# image handling
img_source = []
def download_img(url):
    path = "/tmp/"
    try:
        res = requests.get(url)
        img = open(f"{os.path.join(path, str(random.randrange(1000000)))}.jpg" ,'wb')
        img.write(res.content)
        img.close()
    except Exception as err:
        print(f"\033[0;32m Oops! Something went wrong while trying to download image {err}")

def parse_url_for_images(soup):
    links_img= soup.find_all('img')

    for l in links_img:
        img_source.append(l.get('src'))
    
    if len(img_source) == 0:
        print("No images were found on this page")
    else:
        for src in img_source:
            #download_img(src)
            print(f"{WHITE}Image source:{RESET} " + src)

# generic handling
def parse_url_with(soup, depth=2):
   links = soup.find_all('a')
   print(f"{WHITE}link {links[0]}{RESET}")
    
   if depth < 1:
       print("no links, here is where an image will be downloaded.")
       return
   
   for link in links:
       print("for loop")
       class_list = link.get('class')
       follow_link = link.get('href') 
       print(f"{follow_link}")
       if isinstance(class_list, list) and class_list[0] != 'js-sidebar-open' and class_list[0] != 'logo' and class_list[0] != 'h6':
           print(f"\t{link.get('href')}")
           print(f"\t{class_list}")
           url_follow = http_client(follow_link)
           parse_url_with(url_follow, depth - 1)

def hyperlink_check(soup):
    links = soup.find_all('a')

    for link in links:
        print(f"link: {link}")
        for child in link:
            print(f"\tchild: {child}")

def http_client(url):
    try:
        response = requests.get(verified_url)
        print("HTTP Response: " + str(response.status_code))
        content = response.content
    except HTTPError as httperr:
        print(httperr)
    except Exception as err:
        print(err)
    else:
        # create bs4 obj
        soup = BeautifulSoup(content, 'html.parser')
        
    return soup

if __name__ == '__main__':
    #should throw error if str len > 0
    
    url = input("Enter the URL: ")
    verified_url = url if len(url) > 17 else "\33[0;32mNo URL\033[0m"
    soup = http_client(verified_url)
        
    # parse data
    #parse_url_with(soup)
    hyperlink_check(soup)

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
verified_url = url if len(url) > 0 else "https://www.instagram.com"

print(verified_url)

# get resource from url

response = requests.get(verified_url)
content = response.content

print("HTTPS Response: " + str(response.status_code))

# response.raise_for_status()
print(f" Headers : {response.headers}\n")
print(f" Redirect history : {response.history}\n")
print(f" Content : {response.content}")

soup = BeautifulSoup(content, "html.parser")
soup_links = soup.find_all('a')

for link in soup_links:
    print(link)

# incomplete: this needs to be a tool to dissect html responses.

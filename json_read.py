import json
import requests

response = requests.get('https://jsonplaceholder.typicode.com/users/')

if response.text:
    print('the url returned a response.')
else:
    print('nothing here.')

users = json.loads(response.text)

print(users)

for thing in users:
    print(thing)

#with open() as write_f:
#    json.dump()

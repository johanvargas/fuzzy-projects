import requests 
from requests.auth import HTTPBasicAuth
from requests.adapters import HTTPAdapter
from requests.exceptions import ConnectionError
from getpass import getpass, getuser
# random note - f strings are from python 3.6+

## At this point it does
# it prints the headers and the full text of the reponse, the html etc...

#r = requests.get('http://www.instagram.com/', auth=HTTPBasicAuth('getmegyoza', getpass()))

session_adapter = HTTPAdapter(max_retries=1)

savoy_url = 'http://www.savoyparkr.com/'
insta_url = 'http://www.instagram.com/accounts/login'

print(getuser())

with requests.Session() as session:
#    session.auth = ('getmegyoza', getpass(prompt="getm*** password: ")) 
#    session.mount(savoy_url, session_adapter)   # here to try and mitigate 429 response
    
    try:
        s = session.get(insta_url)
#        print(s.headers)
        print(s.text)
    except ConnectionError as ce:
        print(ce)

########################
## Junk and Extra Code ## 
########################

#print(response.status_code)
#print(response.headers)
# status of sent request
#print("Status Code: ", r.status_code)

# headers of response
#h = r.headers
#if r.status_code == requests.codes.ok:
#    print(dir(requests))
#    print(h['content-type'])
#    for k in h:
#        print(k," : ",  h[k])
#else:
#    print("error: response headers not found")

# request headers
#rh = r.request.headers

#print("\n",rh)
# full text response
#print(r.text)


import requests 

r = requests.get('http://www.savoyparkr.com')

# status of sent request
print("Status Code: ", r.status_code)

# headers of response
h = r.headers
if r.status_code == requests.codes.ok:
    print(dir(requests))
    print(h['content-type'])
    for k in h:
        print(k," : ",  h[k])
else:
    print("error: response headers not found")

# request headers
rh = r.request.headers

print("\n",rh)
# full text response
#print(r.text)


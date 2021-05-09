import json

with open("/Users/johanvargas/Downloads/spinsta/saved/saved_collections-2.json") as write_f:
    json_file = json.load( write_f )
#    print(json_file)

    r = json.dumps(json_file, indent=2)
    print(r)

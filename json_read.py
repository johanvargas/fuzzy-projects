import json

JSON_A = "/Users/johanvargas/Downloads/spinsta/saved/saved_collections-2.json"

def worker(path):
    with open(path) as write_f:
        json_file = json.load( write_f )
    #    print(json_file)

        r = json.dumps(json_file, indent=2)
    #    print(r)

        test = r[0]
        test2 = r[2:125]
        test3 = r[126:250]
        print(test)
        print("\n")
        print(test2)
        print("\n")
        print(test3)

    return "worker2 done"

def worker2(path):
    with open(path, "r") as write_f:
        #json_ = json.dumps(write_f)
        #print(json_)
        print(type(write_f))
        print(write_f)
    return "worker2 done"

def worker3(path):
    json_ = json.loads(open(path).read())
#    print(json_)
#    print(type(json_))
    #value = json_
    #print(value)
    for thing in json_:
#        print(f"This is one thing --> {thing} : {json_[thing]}\n")
#        print(type(json_[thing]))
        values = json_[thing]
        for t in values:
#            print(type(t))
#            print(t)
            for b in t:
                print(type(t), " ", b[0:25])
                if b == "string_map_data":
                    print(type(b))
    return "worker3 done"

#worker_a = worker(JSON_A)
#worker_b = worker2(JSON_A)
worker_c = worker3(JSON_A)

worker_c

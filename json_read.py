from sys import platform
import json
import sys

print(platform)

try:
    print(dict(platform))
except Exception:
    print("error encountered")
if platform == 'darwin':
    MPATH = "/Users/johanvargas/Downloads/saved/saved_collections.json"
else:
    MPATH = "/Users/johanvargas/Downloads/saved/saved_collections-2.json"

JSON_ = json.loads(open(MPATH).read())

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
                #print(type(t), " ", b)
                #print(t.items())
                #print(t['string_map_data'])

                obj_ = t['string_map_data']
#                print(type(obj_))
#                print(obj_.keys())

                for key in obj_:
 #                   print(obj_[key])
                    obj_main = obj_[key]

#                    print(type(obj_main))
                    print(obj_main['value'])

    return "worker3 done"

def worker4(dic, sn):
    print(f"wrkr {sn}")
    if type(dic) == dict:
      #  print(dic.keys())
        for key in dic:
            sn += 1
            print(key, " ", type(dic[key]))
            return worker4(dic[key], sn)
        #return worker4(dic[])
    elif type(dic) == list:
        list_mover = 0
        for key in dic:
            sn += 1
            list_mover += 1
            print(key, " ", type(dic[list_mover]))
            
            if list_mover == len(dic):
                return worker4(dic, sn)

            return worker4(dic[list_mover], sn)

        return worker4(dic)
    else:
        print(f'worker4 stack_number = {sn} finished')
        return 

#    if dic != dict:
#        return "done"
#    else:
#        for obj in dic:
#            print(dict[obj])
#    print("#" * 125)
    return key

def worker5(dic, sn=1):
    print(f"iteration {sn}")
    next_dic = ""
    if type(dic) == dict:
        for key in dic:
            next_dic = dic[key]
            print(next_dic[3:10], "\n")
            print(type(dic), type(next_dic))
            sn += 1
            if type(next_dic) == list:
                print("uh oh, this is a list")
                print(len(next_dic))

                #for t in next_dic
                for t in next_dic:
                    print("this is a list item", t)
            return worker5(next_dic, sn)

    print(type(next_dic), next_dic)
    return worker5(next_dic, sn)
    
def worker6(json, sn=1):
    print(f"iteration {sn}")
    myjson = json
    
    if type(myjson) == dict:
        print("this is a dict [json]")
        myjson = json.popitem()
        sn+=1
        return worker6(myjson, sn)

    if type(myjson) == tuple or type(myjson) == list:
        print(f"theda is a {type(myjson)}")
        for t in myjson:
            print("type from t = ", type(t))
            if type(t) == list or type(t) == tuple:
                myjson = t[0]
                sn+=1
                return worker6(myjson, sn)
            elif type(t) == dict:
                myjson = t
                return worker6(myjson)
    if sn == 20:
        print("done")
        return
    sn+=1
    return worker6(myjson, sn)

def worker7(json):
    k = json['saved_saved_collections']
    for item in k:
        k2 = item['string_map_data'].get('Shared By')
        try:
            print(k2['value'] )
        except TypeError:
            print('exception_skip')

#    myjson = json.popitem()
#    print("type of myjson = ", type(myjson))
#    print("myjson array 0 = ", myjson[0])
#    print(type(myjson[0]), type(myjson[1]))
#    print(myjson[0],"\n", "myjson 1 0 = ", myjson[1][0])
#    print(json)

   # print(json, type(json))
   # print(type(myjson[1], ))

#worker_a = worker(MPATH)
#worker_b = worker2(MPATH)
#worker_c = worker3(MPATH)
#worker_d = worker4(JSON_, 1)
#worker_e = worker5(JSON_)
#worker_f = worker6(JSON_)
worker_g = worker7(JSON_)
worker_g

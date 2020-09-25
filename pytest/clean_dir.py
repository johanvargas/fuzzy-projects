import sys
import os
import math
##
## SYS MODULE
##
## size of storge drive??
##s = sys.maxsize
##print(s)
##
## sys path
##p = sys.path
##print(p)
##
## sys version
##v = sys.version
##print(v)
##
## OS MODULE
##
## name of os
##o = os.name
##print(o)
##
## lists files in dir
##d = os.listdir('.')
##print(d)
##
## gets the times??
##t = os.times()
##print(t)
##
## generator function that walks the dir tree.
##w = os.walk('.')
##
## look thru the dir and list all the files
## This script looks like it could use map() or something.
## This works so be careful running it. I will delete accordingly.
## Also, generators anyone?
##
##for root, dirs, files in os.walk('.'):
##    # print("root-->{}\ndirs-->{}\nfiles-->{}".format(root, dirs, files))
##    print(f'{files}')
##    for f in files:
##        # a = f.split('.')
##        print(len(f))
##        # This needs to be upgraded. 
##        if len(f) < 10:
##            os.remove(f)
##        else:
##            pass
##
## MATH MODULE
##
## log(x, 10)
## this will be very useful in roman numeral.py
##lg = math.log10(1000)
##print(f'log10 of 1000 = {lg}')
##
## map functions
##l = ['BMW', 'MERCEDES', 'VOLVO', 'SUBARU']
##def funk(element):
##    return element + '.com'
##
##map_ = map(funk, l)
##print(list(map_))
##
##
## Simple lambda implementation
##map2 = map(lambda x: x + '.com/search', l)
##print(list(map2))

l = ['BMW', 'MERCEDES', 'VOLVO', 'SUBARU', 'TELSA', 'TOYOTA', 'NISSAN', 'ROLLS-ROYCE', 'RANGE ROVER']

def get_files(path):
    for root, dirs, files in os.walk(path):
        return files
m = map(lambda x : x.split('.'), get_files('.'))
map_list = list(m)
for t in map_list:
    print(map_list[0][0])


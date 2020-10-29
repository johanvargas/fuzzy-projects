import sys
import os
import math

# System and OS modules. Some basic methods.

# SYS MODULE

# size of storge drive??
s = sys.maxsize
# print(s)

# sys path
p = sys.path
# print(p)

# sys version
v = sys.version
# print(v)

# OS MODULE

# name of os
o = os.name
# print(o)

# lists files in dir
d = os.listdir('.')
# print(d)

# gets the time??
t = os.times()
# print(t)

# generator function that walks the dir tree.
w = os.walk('.')

# look thru the dir and list all the files
# Incomplete.. completing in .pytest/ 
for root, dirs, files in w:
    # print("root-->{}\ndirs-->{}\nfiles-->{}".format(root, dirs, files))
    # print('{}'.format(files))
    for f in files:
        a = f.split('.')
        # print(type(f))
        print(f)

## MATH MODULE

# log(x, 10)
# this will be very useful in roman numeral.py
lg = math.log10(1000)
# print(lg)

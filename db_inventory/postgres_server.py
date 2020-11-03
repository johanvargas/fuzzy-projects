import sys
from add_data import add_data

'''
Next steps is to create users and group for specific tasks 

user_a to only view data
	group for viewing only?

user_b to add, delete data
	group or these processes.

Still finding methods of 'cleaning' data before inserting into db. 

'''

name = (sys.argv[1]),
description = (sys.argv[2]),
price = (sys.argv[3]),
images = (sys.argv[4]),
status = (sys.argv[5]),

data = name, description, price, images, status
print(data)
add_data(data)
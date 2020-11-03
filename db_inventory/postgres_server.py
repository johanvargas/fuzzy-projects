import sys
from add_data import add_data

name = sys.argv[0]
description = sys.argv[1]
price = sys.argv[2]
images = sys.argv[3]
status = sys.argv[4]

data = f'{name}, {description}, {price}, {images}, {status}'
print(data)
# add_data(data)
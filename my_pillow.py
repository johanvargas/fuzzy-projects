import collections
import os
import math
import array
import random
from PIL import Image

'''

Brute-forcey way of checking if two image.histograms are equal.

'''
def rand():
	r = random.randint(1, 100)
	return r

def getImage(dir):
	return Image.open(dir)

im1 = getImage('media/Spawn.jpg')
im2 = getImage('media/s2.jpg')

# opens image in preview
# im1.show()
# im2.show()

# returns a list of values, length = 758 
# histo1 = im1.histogram()
# histo2 = im2.histogram()


# (r, b, g) dump
# s = im2.getdata()

#############

histo1 = im1.histogram()
histo2 = im2.histogram()


def get_average(histogram):
	total = 0;
	for num in histogram:
		total += num;

	return math.floor(total/len(histogram))

def compare(*args):
	for arg in args:
		avrg = get_average(arg)
		print(avrg)

# returning NoneType
colors1 = im1.getcolors()
colors2 = im2.getcolors()

print(f'average of spawn is {compare(histo1, histo2)}')
print(f'average of batman is {get_average(histo2)}')


im1.close()
im2.close()
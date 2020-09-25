import collections

from PIL import Image

'''

Brute-forcey way of checking if two image.histograms are equal.

'''



im1 = Image.open('6tg/98324030_254079302371602_7221435594702621230_n.jpg')
im2 = Image.open('6tg/97340215_2960412877376299_6489420792522072687_n.jpg')
im3 = Image.open('6tg/97340215_2960412877376299_6489420792522072687_n.jpg')

# opens image in preview
# im1.show()
# im2.show()

# returns a list of values, length = 758 
# histo1 = im1.histogram()
# histo2 = im2.histogram()

# returning NoneType
# histo1 = im1.getcolors()
# histo2 = im2.getcolors()

# (r, b, g) dump
# s = im2.getdata()

#############

histo1 = im1.histogram()
histo2 = im2.histogram()
histo3 = im3.histogram()


if collections.Counter(histo2) == collections.Counter(histo2):
	print('they are the same')
else:
	print('they are NOT the same')
import collections
from PIL import Image

'''

Brute-forcey way of checking if two image histograms are equal, 
that is, if they are the same image. 

######

References and extra crap
^^^^^^^^^^^^^^^^^^^^^^^^
opens image in preview
im1.show()
im2.show()

returns a list of values, length = 758 
histo1 = im1.histogram()
histo2 = im2.histogram()

returning NoneType
histo1 = im1.getcolors()
histo2 = im2.getcolors()

(r, b, g) dump
s = im2.getdata()



def open_image(image):
	return Image.open(image)

image.histogram()

'''

image1 = 'MeatMurder'
image2 = 'Prince_Around'
image3 = 'cosmic_thing'

list_test = [4, 6 ,7, 4,'12', 5, 4]
ans = []

def compare_items(l):
	# if collections.Counter(docket) == collections.Counter(image):
	while len(l) > 0:
		for n in range(1, len(l)):
			print(l, l[n])
			if l[0] == l[n]:
				print(l[0], l[n])
				ans.append(f'Found an equal at {l[0]}')
			else:
				pass
		l.remove(l[0])
		print('\n')
		return compare_items(l)
	return ans



def compare(*args):
	l = []
	for e in args:
		img_location = f'images/{e}.jpg'
		open_img = Image.open(img_location)
		histo = open_img.histogram()
		l.append(histo)

	return l


_set = compare(image1, image2, image3)

comp = compare_items(list_test)
print(comp)
# print(_set)
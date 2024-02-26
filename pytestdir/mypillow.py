import os, sys, collections
from PIL import Image
from support import check_image_dir, get_images, CWD, CURRENT_DIR, IMG_DIR_NAME

'''

Brute-forcey way of checking if two image histograms are equal, 
that is, if they are the same image. 

check_image_dir --> checks if not it creates the dir and populates with a
couple of images for testing. The rest is histo...grams.

'''
# setup support content
check_image_dir()

def get_histograms():
	os.chdir(IMG_DIR_NAME)
	print(os.getcwd())
	
	image_list = os.listdir()
	print(image_list)

	l = []
	for e in image_list:
		open_img = Image.open(e)
		histo = open_img.histogram()
		t = (e, histo)
		l.append(t)

	return l

def compare_histograms(img_list):
	# print('\n')
	for i, j in img_list:
		# print(i)
		for b, c in img_list:
			# print(i, b)
			if collections.Counter(j) == collections.Counter(c) and i != b:
				print(f'{i} and {b} are equal')
		img_list.remove(img_list[0])
		return compare_histograms(img_list)

# TESTS

histograms = get_histograms()
compare = compare_histograms(histograms)
print(compare)

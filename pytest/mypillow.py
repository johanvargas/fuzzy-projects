import os, sys, collections
from PIL import Image
from support import check_image_dir, get_images, CWD, CURRENT_DIR, IMG_DIR_NAME

'''

Brute-forcey way of checking if two image histograms are equal, 
that is, if they are the same image. 

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
	l = [] 
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

'''

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

	# while len(img_list) > 0:f
	# 	for image in img_list:
	# 		print(image[0])
	# 		for i in range(len(img_list) - 1):
	# 			print (image[0], image[i][0])
	# if collections.Counter(image_1) == collections.Counter(image_2):
	# 	t = tuple(image[], image[])
	# 	print('ok, we are in the money')
	# else:
	# 	print('they are NOT the same')

# list_test = [4, 6 ,7, 4,'12', 5, 4]
# ans = []

# def compare_items(l):
# 	while len(l) > 0:
# 		for n in range(1, len(l)):
# 			print(l, l[n])
# 			if l[0] == l[n]:
# 				print(l[0], l[n])
# 				ans.append(f'Found an equal at {l[0]}')
# 			else:
# 				pass
# 		l.remove(l[0])
# 		print('\n')
# 		return compare_items(l)
# 	return ans

'''
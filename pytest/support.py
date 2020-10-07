# https://www.simplifiedpython.net/python-download-file/
import os, sys
import requests

CWD 		= os.getcwd()
CURRENT_DIR = os.listdir(CWD)
DIR_NAME 	= 'images'

images = {
'MeatMurder': 
'https://img.discogs.com/tMPrxCuA1sjPxIt6JM3YYbXAkY4=/fit-in/\
600x608/filters:strip_icc():format(jpeg):mode_rgb():quality(90)/\
discogs-images/R-429324-1230852244.jpeg.jpg',

'Prince_Around': 
'https://img.discogs.com/3cfZG95e405oWBJLL-1lIJwb5jk=/\
fit-in/600x483/filters:strip_icc():format(jpeg):mode_rgb():quality(90)/\
discogs-images/R-1954507-1260983269.jpeg.jpg',

'cosmic_thing' : 
'https://img.discogs.com/gmgpFW8AhJ8FRbb9n_b7-vh_BpA=/\
fit-in/600x599/filters:strip_icc():format(jpeg):mode_rgb():quality(90)/\
discogs-images/R-951365-1236876316.jpeg.jpg'
}

# create images/
def make_dir():
	# creates dir with root as owner, should be changed.
	os.mkdir('images')

# download file from internet and add to images/
def populate_dir():
	population = os.getcwd()
	print(population)
	new_dir = os.chdir('images')
	new_pop = os.getcwd()
	print(new_pop)
	pop_size = len(os.listdir())

	if pop_size == 0:
		# request url and cleanup 
		for item in images:
			r = requests.get(images[item])
			filename = images[item].split('/')[-1]
			with open(filename, 'wb') as output_file:
				output_file.write(r.content)

			# rename jpg for proper use in mypillow.py
			proper_name = item + '.jpg'
			os.rename(filename, proper_name)

			print('download complete.')
	else:
		print(os.listdir()) 
		pass



	# image_loc = f'{cwd}/{image[0]}.jpg'

	# renamed_image = os.rename('MeatMurder.jpg', 'mm.jpg')
	# print(image_loc)

# check to see if images/ exists, if not create
def check_image_dir():
	dir_present = False
	img_present = False

	def check_dir_size():
		# new_dir = os.chdir('images')
		pop_size = len(os.listdir())
		return pop_size

	for item in CURRENT_DIR:
		if item != DIR_NAME:
			pass
		else:
			print('images/ already exists!')
			dir_present = True

	if dir_present == False:
		print('no images directory found, creating one...')
		make_dir()
		populate_dir()

	if dir_present == True:
		print('images directory exists, your good to go.')

	return

# returns <class 'dict_item'>, a tuple per dict item?
def get_images():
	my_images = images.items()
	return my_images

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
	os.mkdir('images', 755)

# download file from internet and add to images/
def populate_dir():
	population = os.getcwd()
	new_dir = os.chdir('images')
	new_pop = os.getcwd()
	pop_size = len(os.listdir())
	print(pop_size)

	# requests get method on url
	# r = requests.get(url)

	# clean up url, lose everything but filename
	# filename = url.split('/')[-1]

	# with open(filename, 'wb') as output_file:
	# 	output_file.write(r.content)

	# print('download complete.')

	# image_loc = f'{cwd}/{image[0]}.jpg'

	# renamed_image = os.rename('MeatMurder.jpg', 'mm.jpg')
	# print(image_loc)

# check to see if images/ exists, if not create
def check_image_dir():
	present = False

	for item in CURRENT_DIR:
		if item != DIR_NAME:
			pass
		else:
			print('images/ already exists!')
			present = True
			# check to see if images/ is filled with correct images,
			# if not, download to directory


	if present == False:
		make_dir()

	if present == True:
		populate_dir()

	return


# TESTS

check_image_dir()
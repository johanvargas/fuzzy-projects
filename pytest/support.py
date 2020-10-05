# https://www.simplifiedpython.net/python-download-file/
import os, sys
import requests

CWD 		= os.getcwd()
CURRENT_DIR = os.listdir(CWD)
DIR_NAME 	= 'images'

images = {
'MeatMurder': 'https://img.discogs.com/tMPrxCuA1sjPxIt6JM3YYbXAkY4=/fit-in/\
600x608/filters:strip_icc():format(jpeg):mode_rgb():quality(90)/\
discogs-images/R-429324-1230852244.jpeg.jpg',
'Prince_Around': '' ,
'cosmic_thing' : ''
}

# create images/
def make_dir():
	# creates dir with root as owner, should be changed.
	os.mkdir('images', 755)

# download file from internet and add to images/
def populate_dir():


# check to see if images/ exists, if not create
def check_image_dir():
	present = False

	for item in CURRENT_DIR:
		if item != DIR_NAME:
			pass
		else:
			print(type(item), item)
			present = True
			# check to see if images/ is filled with correct images,
			# if not, download to directory


	if present == False:
		make_dir()
		populate_dir()

	return

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

# TESTS

check_image_dir()
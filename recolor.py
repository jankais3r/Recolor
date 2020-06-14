import PIL
import sys
import json
import time
import ntpath
import os.path
from PIL import Image
from ast import literal_eval

try:
	from_image = sys.argv[1]
	to_image = sys.argv[2]
	transform_image = sys.argv[3]
except:
	print('Argument(s) missing.')
	print('Run the script like this: python3 recolor.py image1.png image2.png image3.png')
	quit()

def map():
	print('Generating a map file:')
	
	if os.path.isfile('map_' + ntpath.basename(from_image) + 'to' + ntpath.basename(to_image) + '.txt'):
		print('	Map file already exists, moving on.')
		return
	
	raw_img = Image.open(from_image).load()
	rendered_img = Image.open(to_image).load()
	img_dict = {}
	for i in range(4096):
		for j in range(4096):
			pixel_val = raw_img[i, j]
			img_dict[tuple(pixel_val)] = (i, j)
	print('	Finished loading the input image.')
	
	result = {}
	for i in range(4096):
		for j in range(4096):
			pixel_val = rendered_img[i, j]
			if tuple(pixel_val) in img_dict:
				result[i, j] = img_dict[tuple(pixel_val)]
	print('	Finished generating the map file.')
	with open('map_' + ntpath.basename(from_image) + 'to' + ntpath.basename(to_image) + '.txt', 'w') as out:
		out.write(str(result))
	print('	Map file saved.')

def load():
	print('Transforming the image:')
	raw_img = Image.open(transform_image).load()
	img_dict = {}
	for i in range(4096):
		for j in range(4096):
			pixel_val = raw_img[i, j]
			img_dict[(i, j)] = tuple(pixel_val)
	print('	Finished loading the input image.')
	
	with open('map_' + ntpath.basename(from_image) + 'to' + ntpath.basename(to_image) + '.txt', 'r') as out:
		map_loaded = out.read()
		map_loaded = map_loaded.replace('(', '"').replace(')', '"')
		map_dictionary = json.loads(map_loaded)
		print('	Finished loading the map file.')
	
	image = Image.new('RGB', (4096, 4096))
	imagex = image.load()
	print('	Rendering the final image (3-5 minutes).')
	for i in range(4096):
		for j in range(4096):
			key = literal_eval('(' + map_dictionary[str(i) + ', ' + str(j)] + ')')
			imagex[i, j] = img_dict[key]
	
	image.save(ntpath.basename(from_image) + 'to' + ntpath.basename(to_image) + '_' + ntpath.basename(transform_image), 'PNG')
	print('	Image file saved.')

start = time.time()
map()
load()
print('Done. Took '+str(round(time.time() - start, 2)) + ' s.')
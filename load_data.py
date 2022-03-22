# Author(s):	Shaun Derstine
# Date: 	mm/dd/yyyy
# Desc: 	This file describes a function that loads images from a file into a
#		numpy array

import numpy as np
from os import scandir
from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array
from keras.preprocessing.image import array_to_img
from PIL import Image

def as_numpy(path_to_dir, print_debug):
	path_to_base_dir = path_to_dir # provide absolute path to prevent possible errors

	# Pseudocode:
	# use os.scandir to list base directory
	# loop through each subdirectory (class)
	# load image with keras load_img
	# convert to np ary with img_to_array
	# save to list

	num_loaded = 0 # number of images successfully loaded and converted
	num_errors = 0 # number of images where some error occurred preventing them from being properly loaded/converted
	images_as_numpy_arrays = [] # Initialize empty list to hold images once converted to Numpy arrays

	for sub_dir in scandir(path_to_base_dir): # each 'sub_dir' corresponds to a class
		if sub_dir.is_dir(): # needed to ignore hidden files
			for elem in scandir(sub_dir): # loop through each image in class
					# try to load image from file and save it as a numpy array then append it to list
					# if it fails for any reason, record error
					try:
						img = load_img(elem) # load image using Keras API
						img_numpy_array = img_to_array(img) # convert loaded image into Numpy array
						images_as_numpy_arrays.append(img_numpy_array) # add converted image to list
						num_loaded += 1
					except:
						num_errors += 1
			# end inner for loop
	# end outer for loop

	# this step might be unnecessary
	# finally, convert list to Numpy array
	# converted_images = np.array(images_as_numpy_arrays, dtype=object)

	# debug printout
	if print_debug:
		print("Image loading completed...")
		print("Loaded %d images" % num_loaded)
		print("Unable to load %d images" % num_errors)
	
	return images_as_numpy_arrays
# end as_numpy()

# Given a list of images as Numpy arrays (images) return list with all images modified to (size)
def resize(images, size):
	# Loop through each image in list
	for img in images:
		# Convert to PIL image type
		img_as_pil = array_to_img(img)
		img_as_pil = img_as_pil.resize(size)
# end resize()

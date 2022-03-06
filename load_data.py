# Author(s):	Shaun Derstine
# Date: 	__/__/____
# Desc: 	This file describes a function that loads images from a file into a
#		numpy array

import os
from sys import argv
from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array

def as_numpy():
	# have user pass path to base directory as a CLA (command-line argument)
	path_to_base_dir = argv[1] # relative to location of this script

	# Pseudocode:
	# use os.scandir to list base directory
	# loop through each subdirectory (class)
	# load image with keras load_img
	# convert to np ary with img_to_array
	# save to list/numpy array

	for sub_dir in os.scandir(path_to_base_dir): # each 'sub_dir' corresponds to a class
		for elem in os.scandir(sub_dir): # loop through each image in class
				# try to load image from file and save it as a numpy array
				# if it fails for any reason, print error message
				try:
					img = load_img(elem)
					img_numpy_array = img_to_array(img)
				except:
					print("Error loading image...")
		# end inner for loop
	# end outer for loop

# Author(s):	Shaun Derstine
# Date: 	mm/dd/yyyy
# Desc: 	This file describes a function that loads images from a file into a
#		numpy array

from os import scandir
#from sys import argv
from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array

def as_numpy(path_to_dir):
	path_to_base_dir = path_to_dir # provide absolute path to prevent possible errors

	# Pseudocode:
	# use os.scandir to list base directory
	# loop through each subdirectory (class)
	# load image with keras load_img
	# convert to np ary with img_to_array
	# save to list/numpy array

	num_loaded = 0 # number of images successfully loaded and converted
	num_errors = 0 # number of images where some error occurred preventing them from being properly loaded/converted

	for sub_dir in scandir(path_to_base_dir): # each 'sub_dir' corresponds to a class
		if sub_dir.is_dir(): # needed to ignore hidden files
			for elem in scandir(sub_dir): # loop through each image in class
					# try to load image from file and save it as a numpy array
					# if it fails for any reason, record error
					try:
						img = load_img(elem)
						img_numpy_array = img_to_array(img)
						num_loaded += 1
					except:
						num_errors += 1
			# end inner for loop
	# end outer for loop

	# debug printout
	print("Image loading completed...")
	print("Loaded %d images" % num_loaded)
	print("Unable to load %d images" % num_errors)
# end as_numpy()
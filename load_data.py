# Author(s):	Shaun Derstine
# Date: 	mm/dd/yyyy
# Desc: 	This file describes a function that loads images from a file into a
#		numpy array

from os import scandir
from sys import argv
from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array

def as_numpy(path):
	# have user pass path to base directory as a CLA (command-line argument)
	path_to_base_dir = path # relative to location of this script

	# Pseudocode:
	# use os.scandir to list base directory
	# loop through each subdirectory (class)
	# load image with keras load_img
	# convert to np ary with img_to_array
	# save to list/numpy array

	for sub_dir in scandir(path_to_base_dir): # each 'sub_dir' corresponds to a class
		if sub_dir.is_dir(): # needed to ignore hidden files
			for elem in scandir(sub_dir): # loop through each image in class
					# try to load image from file and save it as a numpy array
					# if it fails for any reason, print error message
					try:
						img = load_img(elem)
						img_numpy_array = img_to_array(img)
					except:
						print("Error loading image...")
			# end inner for loop
	print(img_numpy_array)
	# end outer for loop
	print("Images loaded successfully...")
# end as_numpy()

def main():
	path = "./PetImages/"
	as_numpy(path)
# end main()

if __name__=="__main__":
	main()

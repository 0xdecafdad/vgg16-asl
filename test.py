# this file is for testing various functions
from load_data import as_numpy
from tensorflow import keras
from keras.applications.vgg16 import preprocess_input

def main():
    #as_numpy("~/Documents/workspace/vgg16-asl/PetImages/")
    data = as_numpy("./PetImages/", True) # had to add location relative to file

    for elem in data:
        elem = preprocess_input(elem)

    return 0
# end main()

if __name__=="__main__":
    main()
# this file is for testing various functions
from load_data import as_numpy
from load_data import resize
from tensorflow import keras
from keras.applications.vgg16 import preprocess_input
import matplotlib.pyplot as plt

def main():
    # Load images as Numpy arrays
    data = as_numpy("./PetImages/", True)

    # Preprocess each image
    for elem in data:
        elem = preprocess_input(elem)
    
    # Resize each image according to VGG16 constraints
    resize(data, (224,224))

    return 0
# end main()

if __name__=="__main__":
    main()
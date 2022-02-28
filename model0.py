#!/Users/shaun/miniforge3/envs/tensorflow/bin/python

import numpy as np
import tensorflow as tf
from tensorflow import keras

# Data loading and pre-processing
# Training set
train_ds = tf.keras.utils.image_dataset_from_directory(
	"./PetImages",
	batch_size=32,
	image_size=(224,224),
	seed=1337,
	validation_split=.2,
	subset="training",
)

# Validation set
val_ds = tf.keras.utils.image_dataset_from_directory(
	"./PetImages",
	batch_size=32,
	image_size=(224,224),
	seed=1337,
	validation_split=.2,
	subset="validation",
)

# Visualize data

# Building model

# Training model

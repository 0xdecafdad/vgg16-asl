#!/Users/shaun/miniforge3/envs/tensorflow/bin/python

import numpy as np
import tensorflow as tf
from tensorflow import keras

# Data loading
## Load data in as tf.data.Dataset type
### Training set
train_ds = tf.keras.utils.image_dataset_from_directory(
	"./PetImages",
	batch_size=32,
	image_size=(224,224),
	seed=1337,
	validation_split=.2,
	subset="training",
)

### Validation set
val_ds = tf.keras.utils.image_dataset_from_directory(
	"./PetImages",
	batch_size=32,
	image_size=(224,224),
	seed=1337,
	validation_split=.2,
	subset="validation",
)

# Data preprocessing
## Convert tf.data.Dataset to numpy
## Necessary to pass to vgg16.preprocess_inputs()
#train_ds_numpy = train_ds.as_numpy_iterator()

### Preprocess data for VGG16
#train_ds_prep = tf.keras.applications.vgg16.preprocess_input(
#	train_ds_numpy
#)

#val_ds_prep = tf.keras.applications.vgg16.preprocess_input(
#	val_ds_numpy
#) 

### Note: prefetch data!

# Building model
model = tf.keras.applications.VGG16(
	include_top=True,
	weights=None,
	classes=2,
	classifier_activation="softmax",
)

## Print model
model.summary()

# Training model

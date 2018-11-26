# -*- coding: utf-8 -*-
"""
Created on Fri Nov 16 12:19:23 2018

@author: qiany
"""

import numpy as np
import keras
import matplotlib.pyplot as plt
import random

#import data
from keras.datasets import mnist
(train_images, train_labels),(test_images,test_labels) = mnist.load_data()

#decide model
from keras import layers
from keras import models

model = models.Sequential()

#three convolutional layers
model.add(layers.Conv2D(32,(3,3),activation='relu',input_shape =(28,28,1)))
model.add(layers.MaxPooling2D(2,2))
model.add(layers.Conv2D(32,(3,3),activation='relu'))
model.add(layers.MaxPooling2D(2,2))
model.add(layers.Conv2D(64,(3,3),activation='relu'))

#model.summary()

#convert 3D to 1D
model.add(layers.Flatten())
#fully-connected layer
model.add(layers.Dense(64,activation='relu'))
model.add(layers.Dense(10,activation='softmax'))

#reshape data,scalling into [0,1]
train_images = train_images.reshape((60000,28,28,1))
train_images = train_images.astype('float32')/255
test_images = test_images.reshape((10000,28,28,1))
test_images = test_images.astype('float32')/255

#categorically encode the labels
from keras.utils import to_categorical
#Converts a class vector (integers) to binary class matrix
train_labels = to_categorical(train_labels)
test_labels = to_categorical(test_labels)

#Before training a model, you need to configure the learning process,
model.compile(optimizer='rmsprop',
              loss='categorical_crossentropy',
              metrics=['accuracy'])
# For a multi-class classification problem

#training use fit
model.fit(train_images,train_labels,epochs=5, batch_size=128)

#evaluate
test_loss, test_acc = model.evaluate(test_images,test_labels)
print(test_acc)
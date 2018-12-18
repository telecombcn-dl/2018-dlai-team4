# -*- coding: utf-8 -*-
"""CNN

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1eqZE2md_MkwbpPLum0aCG0P6oQgTMU0b

# Import data from github repository

Import the files from github
"""

!git clone https://github.com/telecombcn-dl/2018-dlai-team4.git
import os
os.chdir("2018-dlai-team4")

"""Run this code to use existing sub-datase existing on the github repository"""

# decide model
model = models.Sequential()

# three convolutional layers
model.add(layers.Conv2D(32, (3, 3), activation='relu',
                        batch_input_shape=(64, 40, 430, 1)))
model.add(layers.MaxPooling2D(2, 2))
model.add(layers.Conv2D(32, (3, 3), activation='relu'))
model.add(layers.MaxPooling2D(2, 2))
model.add(layers.Conv2D(64, (3, 3), activation='relu'))

# CNN to RNN
model.add(layers.Reshape(target_shape=(6, 104*64)))
model.add(layers.Dense(64, activation='relu'))

model.summary()

# RNN layer
model.add(layers.LSTM(64, return_sequences=True, stateful=True,
                      batch_input_shape=(64, 6, 64)))

# convert 3D to 1D
model.add(layers.Flatten())


# fully-connected layer
model.add(layers.Dense(64, activation='relu'))
model.add(layers.Dropout(0.5))
model.add(layers.Dense(5, activation='softmax'))

size_of_output=100                #square image so size_of_output*size_of_output
folder_to_use="optimised_for_accuracy"

from import_picture import import_processed_pict_from


(x_train, y_train), (x_val, y_val), (x_test, y_test),name_list=import_processed_pict_from(folder_to_use,size_of_output,RGB=True,reshape=True)
#Here we just perform the needed reshaping (so that all values are in the [0,1] interval), we switch the labels to categorical and perform random shuffle of the input data.
import numpy as np
x_train=np.asarray(x_train)
x_test=np.asarray(x_test)
x_val=np.asarray(x_val)
if not RGB_output: 
  x_train=x_train.reshape(len(x_train),size_of_output,size_of_output,1)
  x_test=x_test.reshape(len(x_test),size_of_output,size_of_output,1)
  x_val=x_val.reshape(len(x_val),size_of_output,size_of_output,1)

#Conversion of the labels to categoricals
from keras.utils import to_categorical
y_train = to_categorical(y_train)
y_val = to_categorical(y_val)
y_test = to_categorical(y_test)

#Introducing randomization in the input data
ind = np.arange(len(x_train))
np.random.shuffle(ind)
x_train = x_train[ind]
y_train = y_train[ind]

"""Run this section to create a new folder (sub-database) online (do not run the previous cell)"""

treshold= 130 #only the people with more than treshold picture will be kept
number_of_pict_to_keep=10 #number of pict keep per person 

!pip install xlrd

from only_keep_good_files import create_new_parse


create_new_parse(treshold, number_of_pict_to_keep,all_picture_per_person=False,everyone=False)



from import_picture import import_processed_pict_from

size_of_output=100                #square image so size_of_output*size_of_output
folder_to_use="filtered_pict_"+str(treshold)+"_"+str(number_of_pict_to_keep)

(x_train, y_train), (x_val, y_val), (x_test, y_test),name_list=import_processed_pict_from(folder_to_use,size_of_output)

import numpy as np
x_train=np.asarray(x_train)
x_test=np.asarray(x_test)
x_val=np.asarray(x_val)
x_train=x_train.reshape(len(x_train),size_of_output,size_of_output,1)
x_test=x_test.reshape(len(x_test),size_of_output,size_of_output,1)
x_val=x_val.reshape(len(x_val),size_of_output,size_of_output,1)

"""# **CNN with data augmentation**"""

import keras.backend as K

#We defined the precion and recall functions by ourselves as the ones from keras have some issues
def precision(y_true, y_pred):
    '''Calculates the precision, a metric for multi-label classification of
    how many selected items are relevant.
    '''
    true_positives = K.sum(K.round(K.clip(y_true * y_pred, 0, 1)))
    predicted_positives = K.sum(K.round(K.clip(y_pred, 0, 1)))
    precision = true_positives / (predicted_positives + K.epsilon())
    return precision


def recall(y_true, y_pred):
    '''Calculates the recall, a metric for multi-label classification of
    how many relevant items are selected.
    '''
    true_positives = K.sum(K.round(K.clip(y_true * y_pred, 0, 1)))
    possible_positives = K.sum(K.round(K.clip(y_true, 0, 1)))
    recall = true_positives / (possible_positives + K.epsilon())
    return recall

from keras import layers
from keras import models
from keras import regularizers



output_size=len(y_train[1])
print("output size automatisation : "+ str(output_size))
input_size=x_train[1].shape
print("input size automatisation : "+ str(input_size))

model = models.Sequential()
model.add(layers.Conv2D(32, (3, 3), activation='relu',kernel_regularizer = regularizers.l2(0.001), input_shape=input_size))
model.add(layers.Conv2D(32, (3, 3), kernel_regularizer = regularizers.l2(0.001),activation='relu'))  
model.add(layers.Conv2D(32, (3, 3), kernel_regularizer = regularizers.l2(0.001),activation='relu')) 
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(64, (3, 3),kernel_regularizer = regularizers.l2(0.001), activation='relu'))
model.add(layers.Conv2D(64, (3, 3),kernel_regularizer = regularizers.l2(0.001), activation='relu'))   
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(128, (3, 3), kernel_regularizer = regularizers.l2(0.001),activation='relu')) 
model.add(layers.Conv2D(128, (3, 3), kernel_regularizer = regularizers.l2(0.001),activation='relu')) 
model.add(layers.Flatten())
model.add(layers.Dropout(0.5))    
model.add(layers.Dense(output_size, kernel_regularizer = regularizers.l2(0.001),activation='softmax'))  

  

from keras import optimizers
from keras.optimizers import SGD
#a lot of epochs but we are using early stopping. With our settings we never actually reach such value
epoc = 500

#we did not manage to test the network with other optimizers (apart from some initial tests with an sgd(0.1) just to see that it actually had convergence issues)
opt = optimizers.SGD(lr=0.01, decay=1e-6, momentum=0.9, nesterov=True)  

model.compile(optimizer=opt,
            loss='categorical_crossentropy',
            metrics=['accuracy',precision,recall])

model.summary()

"""Apply early stopping"""

from keras.callbacks import EarlyStopping, ModelCheckpoint


#We chose accuracy as the early stopping criterion. Of course also the loss was an option. 
callback = [EarlyStopping(monitor='val_acc', patience=20),
             ModelCheckpoint(filepath='best_model.h5', monitor='val_acc', save_best_only=True)]

"""Data augmentation"""

#The kind of augmentations we perform depend on the dataset (it does not make much sense to employ vertical_flip for example).
#All parameters (commented or not) have been tested. On the right we say whether they are useful and in that case, for which values.
from keras.preprocessing.image import ImageDataGenerator
datagen = ImageDataGenerator(
    rotation_range = 15,       #useful (smaller than 20 seems better)
    width_shift_range = 0.1,   #useful for small values
    #height_shift_range = 0.1, #not useful
    #shear_range = 0.1,        #not useful
    zoom_range = 0.2,         #useful
    horizontal_flip = True,   #useful
    #vertical_flip = True
    #fill_mode = 'nearest'
    )

"""Training without data augmentation"""

#This part was used to perform the training without data augmentation (in order to see the difference in performance)

#history = model.fit(x_train, y_train,batch_size = 128,   
#                    epochs=epoc,
#                    shuffle = True, 
#                    validation_data = (x_val,y_val),
#                    callbacks = callback)

"""Training with data augmentation"""

#The batch size and the steps per epoch have been tuned so that we use 4 times more data. 
history = model.fit_generator(datagen.flow(x_train, y_train,batch_size = 128,shuffle = True),  
                    epochs=epoc,
                    shuffle = True, 
                    steps_per_epoch =  len(x_train)/32,  
                    validation_data = (x_val,y_val),
                    callbacks = callback,
                    validation_steps = 50)

#Plots for accuracy and loss on training and validation set
import matplotlib.pyplot as plt

acc = history.history['acc']
val_acc = history.history['val_acc']
loss = history.history['loss']
val_loss = history.history['val_loss']

epochs = range(1, len(acc) + 1)


plt.plot(epochs, acc, 'bo', label='Training accuracy')
plt.plot(epochs, val_acc, 'b', label='Validation accuracy')
plt.title('Training and validation accuracy')
plt.xlabel('Epochs')
plt.ylabel('Accuracy')
plt.legend()

plt.show()

plt.plot(epochs, loss, 'bo', label='Training loss')
plt.plot(epochs, val_loss, 'b', label='Validation loss')
plt.title('Training and validation loss')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.legend()

plt.show()

"""Load the best weights for the model and compute test accuracy, precision and recall."""

#Since we are using early stopping we need to load the weights for the best case.
model.load_weights('best_model.h5')
print(model.metrics_names)
test_loss, test_acc, test_precision , test_recall= model.evaluate(x_test, y_test)
print("Accuracy = " + str(test_acc))
print("Precision = " + str(test_precision))
print("Recall = " + str(test_recall))

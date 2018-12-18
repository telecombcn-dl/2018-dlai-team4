
#Original file is located at
#https://colab.research.google.com/drive/1w07uOcZ-kumujcxsTmI5A5_UhWGaGC8n

import os
import numpy as np
from import_picture import import_processed_pict_from
from keras import models
from keras import layers
from keras import optimizers
from keras.utils import to_categorical
from keras.applications import VGG19
from keras.callbacks import EarlyStopping, ModelCheckpoint
from keras.preprocessing.image import ImageDataGenerator

# Import data from github

size_of_output=100                   #square image so size_of_output*size_of_output
folder_to_use="optimised_for_speed"
RGB_output=True
run_preprocessing = True

(x_train, y_train), (x_val, y_val), (x_test, y_test),name_list=import_processed_pict_from(folder_to_use)

x_train=np.asarray(x_train)
x_test=np.asarray(x_test)
x_val=np.asarray(x_val)
if not RGB_output: 
  x_train=x_train.reshape(len(x_train),size_of_output,size_of_output,1)
  x_test=x_test.reshape(len(x_test),size_of_output,size_of_output,1)
  x_val=x_val.reshape(len(x_val),size_of_output,size_of_output,1)

y_train = to_categorical(y_train)
y_val = to_categorical(y_val)
y_test = to_categorical(y_test)

ind = np.arange(len(x_train))
np.random.shuffle(ind)
x_train = x_train[ind]
y_train = y_train[ind]

########################################
#Transfer Learning - Feature extraction#
########################################

#Use VGG19 as pretrain network.

conv_base = VGG19(weights='imagenet',
                  include_top=False,
                  input_shape=(100, 100, 3))

# resize the training, validation and test data to fit the output of pre-trained network.

datagen = ImageDataGenerator()
batch_size = 16

def extract_features(x, y, sample_count):
    features = np.zeros(shape=(sample_count, 3, 3, 512))
    labels = np.zeros(shape=(sample_count,62))
    generator = datagen.flow(x,y, batch_size=batch_size)

    i = 0
    for inputs_batch, labels_batch in generator:
        features_batch = conv_base.predict(inputs_batch)
        features[i * batch_size : (i + 1) * batch_size] = features_batch   
        labels[i * batch_size : (i + 1) * batch_size] = labels_batch
        i += 1
        if i * batch_size >= sample_count:

            break
            
    return features, labels 

train_features, train_labels = extract_features(x_train, y_train, len(y_train))
validation_features, validation_labels = extract_features(x_val, y_val, len(y_val))
test_features, test_labels = extract_features(x_test, y_test, len(y_test))

# Flatten the features
train_features = np.reshape(train_features, (len(y_train), 3 * 3 * 512))
validation_features = np.reshape(validation_features, (len(y_val), 3 * 3 * 512))
test_features = np.reshape(test_features, (len(y_val), 3 * 3 * 512))

# use early stoping

callback = [EarlyStopping(monitor='val_acc', patience=15),
             ModelCheckpoint(filepath='best_model.h5', monitor='val_acc', save_best_only=True)]

# Add Dense layers and train the model

model = models.Sequential()
model.add(layers.Dense(512, activation='relu', input_dim=3 * 3 * 512))
model.add(layers.Dense(256))
model.add(layers.Dropout(0.5))
model.add(layers.Dense(62, activation='softmax'))

model.compile(optimizer=optimizers.RMSprop(lr=2e-5),
              loss='categorical_crossentropy',
              metrics=['acc'])

history = model.fit(train_features, train_labels,
                    epochs=250,
                    batch_size=16,
                    validation_data=(validation_features, validation_labels),
                    callbacks = callback)

model.load_weights('best_model.h5')

# Test the model
test_loss, test_acc = model.evaluate(test_features, test_labels)
print("Accuracy = " + str(test_acc))

###################################
# Transfer Learning - Fine Tuning #
###################################

# Unfreeze the 5th Block

conv_base.trainable = True

set_trainable = False

for layer in conv_base.layers:
    if layer.name == 'block5_conv1':
        set_trainable = True
    if set_trainable:
        layer.trainable = True
    else:
        layer.trainable = False

# Define the Dense layers

model = models.Sequential()
model.add(conv_base)
model.add(layers.Flatten())
model.add(layers.Dense(512, activation='relu'))
model.add(layers.Dense(256, activation='relu'))
model.add(layers.Dropout(0.5))
model.add(layers.Dense(62, activation='softmax'))

model.summary()

# Add data augmentation

datagen = ImageDataGenerator(
    rotation_range = 15,       #useful (smaller than 20 seems better)
    width_shift_range = 0.1,   #useful for small values
    zoom_range = 0.2,         #useful
    horizontal_flip = True,   #useful
    )

# Early stopping

callback = [EarlyStopping(monitor='val_acc', patience=15),
             ModelCheckpoint(filepath='best_model.h5', monitor='val_acc', save_best_only=True)]

# Build and train the network

model.compile(optimizer=optimizers.RMSprop(lr=2e-5),
              loss='categorical_crossentropy',
              metrics=['acc'])

history = model.fit_generator(datagen.flow(x_train, y_train ,batch_size = 16,shuffle = True),  #batch size was 32 
                    epochs=100,
                    shuffle = True, 
                    steps_per_epoch =  len(x_train)/32,  # steps were /32
                    validation_data = (x_val, y_val),
                    validation_steps=50,
                    callbacks = callback
                    )

model.load_weights('best_model.h5')

# test 
test_loss, test_acc = model.evaluate(x_test, y_test)
print(test_acc)

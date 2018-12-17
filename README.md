# Introduction 

The capabilities of the human may be insufficient in terms of understanding and comprehending events under some situations like limited memory. At this point, face recognition systems come out as a good tool to overwhelm these weak things of the human. We aren’t strange to the systems and we are so interacting with these type systems in daily life. We can face the systems in the surveillance, tracking, control etcetera.   Alright, why are the systems so important? Because, there are non-contact, detection from long distance, record and archive in the recognition process. 

To form the system model, we are using convolutional neural network structure that is so useful to solve the image processing problem. 



%to do and remove text bellow 

WE NEED TO DELETE THE "test.py" FILE BEFORE DELIVERING THE PROJECT
AND THE "few_pict_for_test" FOLDER 

# Database 

We need sample images to form system structure that has high accuracy rate. For that, Labeled Face in the Wild (LFW) database that is presented by MIT is being used in the network. The database presents us images that are collected from celebrity people on the web. Totally, the database includes image in different number for each person and totally, there are 13233 images for 5740 people. 

The database link: http://vis-www.cs.umass.edu/lfw/




x photos for y person with different number per person same size , color 

link 

if possible curve with the number of people depending on the number of picture or an array with the first person 

# Pre-processing 

Before using the picture in our system we implemented some improvment on the data to increase the final accuracy and the computing speed of our system. 

## Size and reshape

We first reduce the size of the image by only detecting the face using the Haar cascade method. This system allow us to remove all the unused background. And we reshape the imput image as uniform size 100*100 pixels.


# Network structure

We propose two methods on Neural Network. In the first appoach, we creat our own Convolutional Neural Network and compare the performance before and after Data Augmentation. In the other appoach, we use the Transfer Learning method. We first implement the Feature Extration and then we use also Fine Tuning to improve the performance.

## Convolutional Neural Network

> This is a blockquote following a header.
>
> When something is important enough, you do it even if the odds are not in your favor.


## Transfer Learning
In this section, we use the weights pretrained in VGG19 to train the network. Codes are in file transfer_learning.py .

### Feature Extraction
We use the weights in the pretrained VGG19 and feed them to the Dense layer we decide.
Here we don't use the Data augmentation. And we reach the accuracy of 52.4%. 

### Fine Tuning
Based on the structure of Feature Extraction, we unfreeze the last block of VGG19 Network and we propose Data Augmentataion.

# Results
For traning the Network, we use 20 images per class and totally 62 classes. In the CNN, before Data Augmentation we have the result of accuracy 48.8%. After Data Augmentation, the performance improves to 72.6%.
With the appoach of Transfer Learning the accuracy reaches 52.4% after Feature Extractions and increases to 70.6% after Fine Tuning.
Finally with the best weight we have obtain accuracy 85.1% for the unbalanced number of imput iamges.

# Conclusions
## Pre-processing
Create sub-database with a reduced number of people and a balanced number of pictures.
Remove all the useless information of the image and reshape for uniform input.

## Deep Neural Network
Regularizations like Early stopping and Dropout layer prevent overfitting.
Dataset Augmentation improve the network performance.
We tried to implement Transfer Learning like Features Extraction and Fine-Tuning, but we did not manage to improve the performance.

# Reference
[1]. Keras documentation.  https://keras.io/

[2].Face Detection using Haar Cascades. https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_objdetect/py_face_detection/py_face_detection.html

[3]. Ian Goodfellow, Deep Learning.  http://www.deeplearningbook.org

[4]. Data base http://vis-www.cs.umass.edu/lfw/

[5]. Biometrics class in UPC

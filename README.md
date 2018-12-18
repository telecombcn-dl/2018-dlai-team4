# Introduction 

The capabilities of humans may be insufficient in terms of understanding and comprehending really complex events. Face recognition systems are as a good tool to overcome such limitations. We interact with such systems on a daily as in surveillance, tracking, control etcetera. Why are these systems so important? Because they have high accuracy, do not require contact and are able to perform detection from high distances.

We are employing a convolutional neural network structure due to its usefulness for image processing.

# Database

The database we are using is Labeled Face in the Wild (LFW) database, presented by MIT. The database presents us images that are collected from celebrities on the web. In practice, the database presents a different amount of images from person to person; in total we are working with 13233 images for 5740 people.
All the picture are yet processed in order to uniform the dimension of the images and the orientation of the faces.

Link to the database: http://vis-www.cs.umass.edu/lfw/


# Files explanation

## Image folders 

### "all_pict" 

Folder containing all the pictures from the database, never used for train the network but needed to create new sub-folder.

### "optimised_for_accuracy"

This folder is the optimal sub-database we found for obtaining the highest accuracy. 
The sub-database is obtained by keeping all the pictures for people who have more than 20 pictures. 
This sub-database contains 62 classes and more than 3000 samples in total. 


### "optimised_for_speed"

This folder is the optimal sub-database we found for obtaining a good accuracy and have a reasonable training time. 
This sub-database is obtained by keeping the same classes but for all classes, we keep 20 pictures. We have a total of 1240 
pictures in this sub-database.

## Pre-processing script 

### "ordered_names.xlsx"

Files containing the number of pictures associated with all the people in decreasing order. This file is used during the
creation of sub-dataset

### "haarcascade_frontalface_default.xml"

This file is used to extract the face from the pictures. 

### "import_picture.py"

This script is called before all network to processed all the raw pictures from a specific dataset to adapt them to for the network.

The function define in this file is : 

import_processed_pict_from(path_to_look, size, RGB = True, reshape=True, plot_pict=False)

"path_to_look" : database used for the system

"size" : define the normalized size of the image after face extraction. Recommended under 100 to avoid extrapolation. 

"RGB" : use to determine if the picture sent to the network is colored (True) or black & white (False)

"reshape" : if it's set to "False" , the faces are not extracted and the original 250x250 pixels image is used

"plot_pict" : allow us to see the result of the first image reshaped if set to "True"


### "only_keep_good_files.py"

This script contain the function which create new sub-database : 

create_new_parse(threshold, number_of_pict, all_picture_per_person=False, everyone=False) 

"threshold" : minimal number of picture a person need to have to be selected 

"number_of_pict" : number of picture we keep by person. If "number_of_pict" is superior to the number of picture available,
the maximal available picture number is used

"all_picture_per_person" : this parameter allows to overwrite the "number_of_pict" parameter an for each person we keep 
all the picture

"everyone" : this parameter allow to overwrite the "threshold" parameter. In this case all the available person will be kept. 


## Networks

### "main.py"

This file contains the main network we used. Using this network and the "optimised_for_accuracy" sub-database.
We can reach a test accuracy equal to 85%

### "transfer_learning.py"

This file contains the network we implemented using transfer learning from "VGG19" network. 



# More information 

## github page 

You can find more explanation about our project on our github page : 

https://telecombcn-dl.github.io/2018-dlai-team4/

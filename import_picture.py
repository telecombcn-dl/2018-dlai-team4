import os
import cv2
import numpy

def reshape():
    array=[]
    return array

def input_from(path_to_look):
    split_train = 0.6
    split_val= split_train + 0.2
    X_train = []
    X_val=[]
    X_test = []
    y_train = []
    y_val=[]
    y_test = []
    name_list=[]
    folder_list=os.listdir(path_to_look)
    for folder in folder_list:
        files_path = path_to_look + "/"+folder
        image_list = os.listdir(files_path)
        X = []
        y = []
        name_list.append(folder)
        for image_path in image_list:
            image = cv2.imread(path_to_look + "/"+folder+"/"+image_path)

            #if we want to reshape the pict to only keep the face
            #gray = reshape(image)

            #if we just want to use the picture as grey level array
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            gray = numpy.array(gray)


            X.append(gray)
            y.append(len(name_list))
        X_train.extend(X[:int(split_train * len(X))])
        X_val.extend(X[int(split_train * len(X)):int(split_val * len(X))])
        X_test.extend(X[int(split_val * len(X)):])
        y_train.extend(y[:int(split_train * len(y))])
        y_val.extend(y[int(split_train * len(y)):int(split_val * len(y))])
        y_test.extend(y[int(split_val * len(y)):])
    return (X_train, y_train), (X_val, y_val), (X_test, y_test),name_list



files_path=os.path.dirname(__file__)+"\\few_pict_for_test"
(X_train, y_train), (X_val, y_val), (X_test, y_test),name_list=input_from(files_path)
print(X_train[2][150][150])
print(y_train)
print(name_list)

(train_images, train_labels),(test_images,test_labels) =(X_train, y_train), (X_test, y_test)






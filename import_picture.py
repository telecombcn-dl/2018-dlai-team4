import os
from face_detection import reshape
import cv2
import numpy


def import_processed_pict_from(path_to_look):
    #path_to_look=os.path.dirname(__file__) +"/"+path_to_look
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
    i=0
    for num_person,folder in enumerate(folder_list):
        print(num_person)
        files_path = path_to_look + "/"+folder
        image_list = os.listdir(files_path)
        X = []
        y = []
        name_list.append(folder)
        for image_name in image_list:
            image_path=path_to_look + "/"+folder+"/"+image_name

            #if we want to reshape the pict to only keep the face
            gray,img= reshape(image_path)
            # if(i<10):
            #     cv2.imshow('img', img)
            #     cv2.waitKey(0)
            #     cv2.destroyAllWindows()
            #     i+=1

            #if we just want to use the picture as grey level array
            #image = cv2.imread(image_path)
            #gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            #gray = numpy.array(gray)


            X.append(gray)
            label=numpy.zeros(len(folder_list))
            label[num_person]=1;
            y.append(label)
        X_train.extend(X[:int(split_train * len(X))])
        X_val.extend(X[int(split_train * len(X)):int(split_val * len(X))])
        X_test.extend(X[int(split_val * len(X)):])
        y_train.extend(y[:int(split_train * len(y))])
        y_val.extend(y[int(split_train * len(y)):int(split_val * len(y))])
        y_test.extend(y[int(split_val * len(y)):])
    return (X_train, y_train), (X_val, y_val), (X_test, y_test),name_list



# files_path=os.path.dirname(__file__)+"\\filtered_pict_20"
# (X_train, y_train), (X_val, y_val), (X_test, y_test),name_list=input_from(files_path)
#print(name_list)

#print(train_images)
#print(len(train_images))
# max=(0,0)
# for i in range (len(train_images)):
#     print(train_images[i].shape)
#     if(train_images[i].shape>max):
#         max=train_images[i].shape
# print(max)





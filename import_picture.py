# Related libraries are being called.
import os
import cv2


def extract_face(path, size, RGB):
    global roi_gray
    global roi_color
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

    img = cv2.imread(path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.1, 5)
    for (x, y, w, h) in faces:
        roi_gray = gray[y:y + h, x:x + w]
        roi_gray = cv2.resize(roi_gray, dsize=(size, size), interpolation=cv2.INTER_CUBIC)
        roi_color = img[y:y + h, x:x + w]
        roi_color = cv2.resize(roi_color, dsize=(size, size), interpolation=cv2.INTER_CUBIC)

    if RGB:
        return roi_color
    else:
        return roi_gray


def import_processed_pict_from(path_to_look, size=100, RGB = True, reshape=True, plot_pict=False):
    # Arranging percentage of train, validation and test data
    split_train = 0.6
    split_val = split_train + 0.2

    # Creating empty array to put picture with respect to three parts 
    x_train = []
    x_val = []
    x_test = []
    y_train = []
    y_val = []
    y_test = []

    name_list = []
    folder_list = os.listdir(path_to_look)
    i = 0

    # For each person we read all the picture then we split in different tensor (train, validation & test)
    for num_person, folder in enumerate(folder_list):
        print(str(num_person) + " : " + folder)
        files_path = path_to_look + "/" + folder
        image_list = os.listdir(files_path)
        X = []
        y = []
        
        # The name of the celebrity is added to the list of possible output
        name_list.append(folder)

        # the pictures of each person is reshaped (only face) and extracted as float matrix
        for image_name in image_list:
            image_path = path_to_look + "/"+folder+"/"+image_name

            # if we want to reshape the pict to only keep the face
            # RGB 1 - colored scale   RGB 0- gray scale
            if reshape:
                output = extract_face(image_path, size, RGB)
            else :
                output = cv2.imread(image_path)
                if not RGB:
                    output = cv2.cvtColor(output, cv2.COLOR_BGR2GRAY)

            if plot_pict:
                plot_pict = False
                cv2.imshow('img', output)
                cv2.waitKey(0)
                cv2.destroyAllWindows()


            # picture values are being scaled between 0-1
            output = output/255

            X.append(output)
            # Add the label to the output tensor
            label = num_person
            y.append(label)

        # For each person, pictures is being separated related parts
        x_train.extend(X[:int(split_train * len(X))])
        x_val.extend(X[int(split_train * len(X)):int(split_val * len(X))])
        x_test.extend(X[int(split_val * len(X)):])
        y_train.extend(y[:int(split_train * len(y))])
        y_val.extend(y[int(split_train * len(y)):int(split_val * len(y))])
        y_test.extend(y[int(split_val * len(y)):])
        
    return (x_train, y_train), (x_val, y_val), (x_test, y_test), name_list





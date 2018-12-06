import random

# If we hold all pictures under just a file
# in this case, we need to choose data as validation, training and testing.
# Thanks to this code, we can do it by using random function. 

def picture_selection(picture_size):

    # Determining disturbution ratios of data
    train_size=picture_size*0.6
    validation_size=picture_size*0.2
    test_size=picture_size*0.2

    # Creating array to hold related picture index 
    train_pic_index=[]
    validation_pic_index=[]
    test_pic_index=[]

    list_index=range(0,picture_size)

    #print len(list_index)
    #print list_index
    #print train_size-len(train_pic_index)


    for i in range(0,int(train_size)):  

        # For training part
        index=random.choice(list_index)
        train_pic_index.append(index)
        list_index.remove(index)

        # For validation part
        if(len(validation_pic_index)!=validation_size):  # testing whether related limit value is reached
            index=random.choice(list_index)              # Chosing an index number from index set
            validation_pic_index.append(index)           # Adding related array
            list_index.remove(index)                     # removing index number from index set

        # For text part
        if(len(test_pic_index)!=test_size):
            index=random.choice(list_index)
            test_pic_index.append(index)
            list_index.remove(index)

    return train_pic_index,validation_pic_index,test_pic_index

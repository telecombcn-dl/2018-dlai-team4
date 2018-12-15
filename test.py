from only_keep_good_files import create_new_parse
from import_picture import import_processed_pict_from
import os

threshold_list = [100, 53, 43, 39, 35, 32, 29, 26, 24, 21, 20]
num_pict = 20

for threshold in threshold_list:
    create_new_parse(threshold, num_pict, False, False)
#import_processed_pict_from(os.getcwd() + "/filtered_pict_20", 100, True)
# from face_detection import reshape
# import os
# import cv2
#
# output=reshape(os.getcwd()+"/all_pict/Aaron_Eckhart/Aaron_Eckhart_0001.jpg",100,False)
# cv2.imshow('img',output)
# cv2.waitKey(0)
# cv2.destroyAllWindows()




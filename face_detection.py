# -*- coding: utf-8 -*-
"""
Created on Fri Nov 30 14:41:27 2018

@author: qiany
"""

import cv2
#import sys
import numpy as np

def reshape(path,size,RGB) :
    global roi_gray
    global roi_color
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    #eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
    
    img = cv2.imread(path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    faces = face_cascade.detectMultiScale(gray, 1.1, 5)
    for (x,y,w,h) in faces:
        roi_gray = gray[y:y+h, x:x+w]
        roi_gray=cv2.resize(roi_gray, dsize=(size, size), interpolation=cv2.INTER_CUBIC)
        roi_color = img[y:y+h, x:x+w]
        roi_color = cv2.resize(roi_color, dsize=(size, size), interpolation=cv2.INTER_CUBIC)
        # eyes = eye_cascade.detectMultiScale(roi_gray)
        #for (ex,ey,ew,eh) in eyes:
        #    cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
    
    #cv2.imshow('img',roi_gray)
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()
    if RGB :
        return roi_color
    else :
        return roi_gray


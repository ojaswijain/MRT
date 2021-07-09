# -*- coding: utf-8 -*-
"""
Created on Wed Jul  7 10:52:54 2021

@author: ojasw
"""
#works with the anaconda environment, faces issues on Colab
import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0)
back_sub = cv.createBackgroundSubtractorMOG2(history=500, 
        varThreshold=25)
 
kernel = np.ones((5,5),np.uint8)
 
while(True):
        ret, frame = cap.read()
        fore = back_sub.apply(frame)
        fore = cv.morphologyEx(fore, cv.MORPH_CLOSE, kernel)
        _, fore = cv.threshold(fore,127,255,cv.THRESH_BINARY)
 
        bb = fore
        contourSet, hierarchy = cv.findContours(bb,cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE)[:]
        areas = [cv.contourArea(c) for c in contourSet]

        if len(areas) < 1:
            cv.imshow('Frame',frame)
            if cv.waitKey(1) & 0xFF == ord('x'):
                break
            continue
 
        else:
            max_index = np.argmax(areas)
 
        contour = contourSet[max_index]
        x,y,w,h = cv.boundingRect(contour)
        cv.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
         
        cv.imshow('Frame',frame)
 
        if cv.waitKey(1) & 0xFF == ord('x'):
            break
 
cap.release()
cv.destroyAllWindows()
 

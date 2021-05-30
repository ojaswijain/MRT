# -*- coding: utf-8 -*-
"""
Created on Thu May 13 23:54:21 2021

@author: ojasw
"""

import cv2 as cv
import sys
img = cv.imread(sys.argv[1])
if img is None:
    sys.exit("Could not read the image.")
img = cv.resize(img, (480,340))
for x in range (0,480,1):
    for y in range(0,340,1):
        color = img[y,x]
        if color[0]<70 and color[1]<70 and color[2]<70:
            img[y,x]=[0,0,0]
        else:
            img[y,x]=[255,255,255]
cv.imshow("Display window", img)
k = cv.waitKey(0)
if k == ord("s"):
    cv.imwrite("QR.png", img)

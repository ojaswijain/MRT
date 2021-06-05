# -*- coding: utf-8 -*-
"""
Created on Sat Jun  5 21:17:34 2021

@author: ojasw
"""

import cv2 as cv
import sys
import matplotlib.pyplot as plt

img = cv.imread(sys.argv[0])
img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
gray = cv.cvtColor(img, cv.COLOR_RGB2GRAY)
#using the inbuilt binary function instead of homemade algo
_, binary = cv.threshold(gray, 100, 100, cv.THRESH_BINARY_INV)
plt.imshow(binary, cmap="gray")
plt.show()
contours, hierarchy = cv.findContours(binary, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
img = cv.drawContours(img, contours, -1, (0, 255, 0), 1)
plt.imshow(img)
plt.show()

# -*- coding: utf-8 -*-
"""
Created on Mon May 31 01:53:12 2021

@author: ojasw
"""

import sys
import cv2 as cv
def main(argv):
    
    window_name = ('Sobel')
    scale = 1
    delta = 0
    ddepth = cv.CV_16S
   
    src = cv.imread(argv[0], cv.IMREAD_COLOR)
    src = cv.GaussianBlur(src, (3, 3), 100)
    gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)  
    grad_x = cv.Sobel(gray, ddepth, 1, 0, ksize=3, scale=scale, delta=delta, borderType=cv.BORDER_DEFAULT)
    grad_y = cv.Sobel(gray, ddepth, 0, 1, ksize=3, scale=scale, delta=delta, borderType=cv.BORDER_DEFAULT)
    
    
    abs_grad_x = cv.convertScaleAbs(grad_x)
    abs_grad_y = cv.convertScaleAbs(grad_y)
    
    
    grad = cv.addWeighted(abs_grad_x, 0.5, abs_grad_y, 0.5, 0)
    
    
    cv.imshow(window_name, grad)
    cv.waitKey(0)
    
    return 0
if __name__ == "__main__":
    main(sys.argv[1:])
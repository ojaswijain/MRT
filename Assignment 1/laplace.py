# -*- coding: utf-8 -*-
"""
Created on Sat Jun  5 23:59:01 2021

@author: ojasw
"""

import sys
import cv2 as cv
def main(argv):
    ddepth = cv.CV_16S
    kernel_size = 3
    window_name = "Laplace"
    img = "cat.jpg"
    src = cv.imread(img, cv.IMREAD_COLOR)
    src = cv.GaussianBlur(src, (3, 3), 0)
    gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
    cv.namedWindow(window_name, cv.WINDOW_AUTOSIZE)
    dst = cv.Laplacian(gray, ddepth, ksize=kernel_size)
    # [laplacian]
    # [convert]
    # converting back to uint8
    abs_dst = cv.convertScaleAbs(dst)
    cv.imshow(window_name, abs_dst)
    cv.waitKey(0)
    return 0
if __name__ == "__main__":
    main(sys.argv[1:])
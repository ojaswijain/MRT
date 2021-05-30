import cv2 as cv
import sys
MAX_KERNEL_LENGTH = 31
dst = None
window_name = 'Gaussian'
src=cv.imread(sys.argv[1])
for i in range(1, MAX_KERNEL_LENGTH, 2):
        dst = cv.GaussianBlur(src, (i, i), 5)
cv.imshow(window_name,dst)
k = cv.waitKey(0)
if k == ord("s"):
    cv.imwrite("v.jpg", dst)

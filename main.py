import cv2 as cv
import numpy as np


img = cv.imread('original.png',0)
equ = cv.equalizeHist(img)
res = np.hstack((img, equ))
cv.imwrite('converted.png',res)


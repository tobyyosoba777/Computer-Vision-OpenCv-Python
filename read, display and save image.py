# -*- coding: utf-8 -*-
"""
Created on Tue Jul 19 10:07:05 2022

@author: TOBBY
"""

import cv2
import sys

img = cv2.imread("images/car.jpg")
if img is None:
    sys.exit("not found")

cv2.imshow("image", img)
key = cv2.waitKey(0)
if key == ord('s'):
    cv2.imwrite("images/caro.png", img)
elif key == ord('q'):
    cv2.destroyAllWindows()
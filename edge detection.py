# -*- coding: utf-8 -*-
"""
Created on Sun Nov 20 16:10:38 2022

@author: TOBBY
"""

"""
Humans, after seeing a rough sketch, can easily recognize many object types and their poses.
That is why edges play an important role in the life of humans as well as in the applications of computer vision.
 OpenCV provides very simple and useful function called Canny()for detecting the edges.
"""

import cv2
#numpy is a python library used for fast computation of arrays and in preprocessing multidimensional arrays
import numpy as np

img = cv2.imread("images/car2.png")

#now detect the edges
edges = cv2.Canny(img, 200, 300)

cv2.imwrite("images/edges_car.jpg", edges)

cv2.imshow("edges", cv2.imread("images/edges_car.jpg"))


#displays the original image
cv2.imshow("original image", img)


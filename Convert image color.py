#import the required library

import cv2
#reading the image
img = cv2.imread("images/car2.png")
#if we display this image using imshow() function, then we can see that this image is in BGR format
#Now, use cvtColor() function to convert this image to grayscale

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow('gray_car', gray)


cv2.imshow("original image", img)
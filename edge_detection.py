import cv2 
import numpy as np 

img=cv2.imread('image.jpg')
grayscale=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow('Gray',grayscale)
#Laplacian
lap=cv2.Laplacian(grayscale,cv2.CV_64F)
lap=np.uint8(np.absolute(lap))
cv2.imshow('edged',lap)


cv2.waitKey()

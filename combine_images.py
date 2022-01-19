import cv2
import numpy as np 
img=cv2.imread('image.jpg')
print(img.shape)
img1=cv2.imread('image1.jpg')

img1_resized=cv2.resize(img1,(2560,1920))
print(img1_resized.shape)
imgmerge=np.hstack((img,img1_resized))
imgmerge=cv2.resize(imgmerge,(500,400))

cv2.imshow("MergedImage",imgmerge)
cv2.waitKey()


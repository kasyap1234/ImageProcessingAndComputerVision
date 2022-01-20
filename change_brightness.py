import cv2
import numpy as np 
img=cv2.imread('image1.jpg')

# now introducing a factor by which the brightness is controlled either postive or negative . 
n=int(input(""))
matrix=np.ones(img.shape,dtype="uint8")*n
print("do you want to brighten you image or darken it ?")
print("enter 1 if you want to brighten the image and 0 if you want to darken it ")

factor=int(input(""))


if factor==1: 
    img_new=cv2.add(img,matrix)
    cv2.imshow('modified',img_new)
    cv2.waitKey()
elif factor==0: 
    img_new=cv2.subtract(img,matrix)
    cv2.imshow("modified",img_new)
    cv2.waitKey()
    





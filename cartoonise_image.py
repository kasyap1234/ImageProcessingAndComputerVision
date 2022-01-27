import cv2 
import numpy as np 
img=cv2.imread("person.jpg")
grayscale=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
grayscale=cv2.medianBlur(grayscale,9)
edge=cv2.adaptiveThreshold(grayscale,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,9,9)
colored=cv2.bilateralFilter(img,9,250,250)
cartoonise=cv2.bitwise_and(colored,colored,mask=edge)
cv2.imshow("original image",img)
cv2.imshow("edges",edge)
cv2.imshow("CARTOONISED",cartoonise)
cv2.waitKey(0)
cv2.destroyAllWindows()

import cv2
import cvzone 
from cvzone.SelfiSegmentationModule import SelfiSegmentation
import os 
cap=cv2.VideoCapture(0)
modifier=SelfiSegmentation()

while True: 
    success,img=cap.read()
    output=modifier.removeBG(img)

    cv2.imshow('Image',img)
    

    cv2.waitKey(1)
    cv2.destroyAllWindows


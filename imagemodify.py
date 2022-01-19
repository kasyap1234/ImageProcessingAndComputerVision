import cv2
img=cv2.imread('image.jpg')


imgresize=cv2.resize(img,(720,480))
imgcanny=cv2.Canny(imgresize,70,100)

cv2.imshow("lines",imgcanny)
cv2.waitKey(0)


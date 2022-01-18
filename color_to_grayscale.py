import cv2
img1=cv2.imread('/home/kasyap/Downloads/image.jpg',0)
cv2.imshow("converted image",img1)
cv2.waitKey(0) 
k=input("enter s to save the grayscale image ")

if k=="s": 
    cv2.imwrite("/home/kasyap/Downloads/output.jpg",img1)
    cv2.destroyAllWindows()


print('converted and stored the grayscale image')



import cv2

# reads image from the computer ; 

img1=cv2.imread('/home/kasyap/Downloads/image.jpg')
# resizing the image . 
img1=cv2.resize(img1,(1280,700))
# displaying the image . 
cv2.imshow("coloured image",img1)
#function to prevent the popup image from closing . 
cv2.waitKey()
cv2.destroyAllWindows()




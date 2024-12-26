import cv2
import numpy as np 

img = cv2.resize(cv2.imread("love.jpg"),(260,360))
# Convert the image to grayscale
new=cv2.cvtColor(src=img, code=cv2.COLOR_BGR2GRAY, dst=None, dstCn=None)
# Convert the image to BGR
bgr=cv2.cvtColor(src=new,code=cv2.COLOR_GRAY2BGR,dst=None,dstCn=None)
# # Convert the image to HSV
# HSV=cv2.cvtColor(new,cv2.COLOR_GRAY2HSV)
# Convert the image to RGB
rgb=cv2.cvtColor(new,cv2.COLOR_GRAY2RGB,dst=None,dstCn=None)

cv2.imshow("original",new)
cv2.imshow("bgr",bgr)
# cv2.imshow("hsv",new)
cv2.imshow("rgb",rgb)
cv2.waitKey(0)
cv2.destroyAllWindows()
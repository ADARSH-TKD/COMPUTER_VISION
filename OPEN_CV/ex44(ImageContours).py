import cv2
import numpy as np

a= cv2.imread("chorme.png")


img=cv2.cvtColor(a,cv2.COLOR_BGR2GRAY)
r,th=cv2.threshold(img,240,255,cv2.THRESH_BINARY)

#image contours
contours, hierarchy = cv2.findContours(image=th, mode=cv2.RETR_TREE, method=cv2.RETR_TREE, contours=None, hierarchy=None, offset=None)

new_img= cv2.drawContours(image=a, contours=contours, contourIdx=-1, color=(0,255,0), thickness=2)

#desply image 
# h=np.hstack((img,th,new_img))
cv2.imshow("image contouring",new_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
import cv2
import matplotlib.pyplot as plt 
import numpy as np

img =cv2.imread("thor.jpg")
hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

demo=cv2.imread("demo.jpg")
hsv_demo=cv2.cvtColor(demo,cv2.COLOR_BGR2HSV)

hist=cv2.calcHist([hsv_demo],[0,1],None,[180,256],[0,180,0,256])
mask=cv2.calcBackProject([hsv],[0,1],hist,[0,180,0,256],1)

ker =cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))
mask=cv2.filter2D(mask,-1,ker)

_,th=cv2.threshold(mask,20,255,cv2.THRESH_BINARY)

mask =cv2.merge((mask,mask,mask))

res =cv2.bitwise_or(img,mask)


cv2.imshow("Sample",res )
cv2.imshow("Original Image",img)
cv2.imshow("Mask",mask)
cv2.waitKey(0)
cv2.detroyAllWindows()
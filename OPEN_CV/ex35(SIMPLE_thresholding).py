import cv2
import numpy as np 

img=cv2.resize(cv2.imread("coin.jpg",0),(280,280))#read the image

_,th1=cv2.threshold(src=img, thresh=90, maxval=255, type=cv2.THRESH_BINARY)#convert the image to binary

_,th2=cv2.threshold(src=img, thresh=90, maxval=255, type=cv2.THRESH_BINARY_INV)#convert the image to binary invert

_,th3=cv2.threshold(img,200,255,cv2.THRESH_TRUNC)#convert the image to trunc

_,th4=cv2.threshold(img,70,255,cv2.THRESH_TOZERO)#convert the image to tozero

_,th5=cv2.threshold(img,170,255,cv2.THRESH_TOZERO_INV)#convert the image to tozero invert


# text
cv2.putText(img,"ORIGINAL",(10,20),19,0.6,(0,255,0),2)

h1=np.hstack((img,th1,th2))
h2=np.hstack((th3,th4,th5))
v=np.vstack((h1,h2))

cv2.imshow("threshold",v)
cv2.waitKey(0)
cv2.destroyAllWindows()
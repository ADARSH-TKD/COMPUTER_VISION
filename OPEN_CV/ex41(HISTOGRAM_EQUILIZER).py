import cv2
import numpy as np 
import matplotlib.pyplot as plt 

img =cv2.imread("hp.jpeg")#read the image
img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)#convert the image to grayscale
crop=img[9:212,19:321]#crop the image

# Histogram of the image
h=cv2.calcHist([crop],[0],None,[256],[0,256])

# equalize the histogram
eq=cv2.equalizeHist(crop)
q=cv2.calcHist([eq],[0],None,[256],[0,256])


plt.subplot(2,1,1)
plt.title("Histogram_equilaizer of the image",color="blue")
plt.plot(q)


plt.subplot(2,1,2)
plt.title("Normal histogram of image",color="red")
plt.plot(h)
plt.show()


hs=cv2.resize(np.hstack((crop,eq)),(1300,800))

cv2.imshow("histrogram equlizer",hs)
cv2.waitKey(0)
cv2.destroyAllWindows()
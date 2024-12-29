import cv2
import matplotlib.pyplot as plt 
import numpy as np

img= cv2.imread("potrate.jpg")

r,g,b=cv2.split(img)

h=cv2.calcHist([r],[0],None,[256],[0,256])
h2=cv2.calcHist([g],[0],None,[256],[0,256])
h3=cv2.calcHist([b],[0],None,[256],[0,256])

plt.figure(figsize=(5, 5), facecolor="white", edgecolor="green")
plt.subplot(3,1,1)
plt.plot(h2,label="image1",color="blue")
plt.subplot(3,1,2)
plt.plot(h,label="image2",color="green")
plt.subplot(3,1,3)
plt.plot(h3,label="image3",color="red")
plt.show()

h=np.hstack((r,g,b))
cv2.putText(h,"RED",(50,50),4,1,(0,0,255),2)
cv2.putText(h,"GREEN",(500,50),4,1,(0,0,255),2)
cv2.putText(h,"BLUE",(1000,50),4,1,(0,0,255),2)
cv2.imshow("image1",h)

cv2.waitKey(0)
cv2.destroyAllWindows()
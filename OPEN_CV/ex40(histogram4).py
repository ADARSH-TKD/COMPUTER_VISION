import cv2
import numpy as np 
import matplotlib.pyplot as plt 

img= cv2.imread("car.jpg")
b,g,r=cv2.split(img)

plt.figure(figsize=(5,5))

plt.hist(g.ravel(),256,[0,256],color='green')
plt.hist(r.ravel(),256,[0,256],color='red')
plt.hist(b.ravel(),256,[0,256],color='blue')
plt.show()


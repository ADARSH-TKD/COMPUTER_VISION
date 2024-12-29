import cv2
import numpy as np 
 
img=cv2.imread("ave.jpg")#read the image
img2=cv2.imread("ave3.jpg")#read the image

gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)#convert the image to gray scale
gray2=cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)#convert the image to gray scale

# w,h=gray2.shpape[::-1] #get the width and height of the image but advance 
w,h=gray2.shape[::-1] #get the width and height of the image but advance

res = cv2.matchTemplate(image=gray, templ=gray2, method=cv2.TM_CCOEFF_NORMED)#apply template matching
thr =0.95 #set the threshold

l=np.where(res>=thr)#get the location of the image
for i in zip(*l[::-1]):#loop through the location
    cv2.rectangle(img,i,(i[0]+w,i[1]+h),(0,255,0),2)#draw the rectangle


print(l)



cv2.imshow("image2",res)
cv2.imshow("image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
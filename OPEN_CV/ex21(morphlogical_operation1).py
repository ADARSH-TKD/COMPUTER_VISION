import cv2
import numpy as np 
img =cv2.resize(cv2.imread("img_mp.png"),(230,140))
img2 =cv2.resize(cv2.imread("img_mo.png"),(230,140))
img3=cv2.resize(cv2.imread("mp.png"),(230,140))

k= np.ones((8,8),np.uint8)
print(k)
print(img)
# opening
open=cv2.morphologyEx(src=img, op=cv2.MORPH_OPEN, kernel=k, iterations=1)
# closing
close=cv2.morphologyEx(img2,cv2.MORPH_CLOSE,k,1)
#gradient
gradent=cv2.morphologyEx(img3,cv2.MORPH_GRADIENT,k,1)
# top hat
top=cv2.morphologyEx(img3,cv2.MORPH_TOPHAT,k,1)
# blackhat
blackhat=cv2.morphologyEx(img3,cv2.MORPH_BLACKHAT,k,1)
# hitmiss
hitmiss=cv2.morphologyEx(img3,cv2.MORPH_HITMISS,k,1)



H=np.hstack([img,open,])
h2=np.hstack([img2,close])
h3=np.hstack([img3,gradent])
h4=np.hstack([img3,top])
h5=np.hstack([img3,blackhat])
h6=np.hstack([img3,hitmiss])
v=np.vstack([H,h2,h3])
v2=np.vstack([h4,h5,h6])
x=np.hstack([v,v2])
# cv2.putText(v,"Original",(10,20),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,255,0),1)
# cv2.putText(v,"openinng",(190,20),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,255,0),1)
# cv2.putText(v,"Original",(10,170),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,255,0),1)
# cv2.putText(v,"closeing",(190,170),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,255,0),1)
# cv2.putText(v,"Original",(10,320),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,255,0),1)
# cv2.putText(v,"gradent",(190,320),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,255,0),1)
# cv2.putText(v,"Original",(10,450),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,255,0),1)
# cv2.putText(v,"Top_Hat",(190,450),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,255,0),1)


cv2.imshow("img",x)
cv2.waitKey(0)
cv2.destroyAllWindows()
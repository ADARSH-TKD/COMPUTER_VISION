import cv2
import numpy as np

img=cv2.imread(r"C:\Users\adarsh\Downloads\New folder\ADARSH.jpg")
# Resize the image
rs=cv2.resize(img,(400,600))


# Display the shape of the image
print(rs.shape) 

# Rotate the image
w=rs.shape[0] #height
h=rs.shape[1] #width
m=cv2.getRotationMatrix2D(center=(h//2,w//2),angle=90,scale=1)
print(m) # Display the rotation matrix
new_img=cv2.warpAffine(rs,m,(h,w))


cv2.imshow("image",np.hstack([rs,new_img]))
cv2.waitKey(0)
cv2.destroyAllWindows()
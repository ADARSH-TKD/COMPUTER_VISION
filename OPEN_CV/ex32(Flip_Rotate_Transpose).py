import cv2
img =cv2.resize(cv2.imread("AK.jpg"),200,380)
# flip(src,flipCode)
# 0=Vertical, 1=Horizontal, -1=Both
img=cv2.flip(scr=img,flipcode=0) # x-axis
img=cv2.flip(img,1) # y-axis
img=cv2.flip(img,-1) # both

# Rotate
# Rotate(src,angle,center,scale)
# center=(x,y) scale=1.0
img=cv2.rotate(src=img,rotateCode=cv2.ROTATE_90_CLOCKWISE)

# Transpose
# Transpose(src)
img=cv2.transpose(src=img)



cv2.imshow("window",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
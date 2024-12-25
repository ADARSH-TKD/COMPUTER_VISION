import cv2
# Read the image
a= cv2.imread(r"C:\Users\adarsh\Downloads\New folder\ADARSH.jpg")
# Resize the image
# r=cv2.resize(a,(400,600))
r1=cv2.resize(a,(400,600))
# Draw a circle
# cv2.circle(img=r, center=(200, 200), radius=100, color=(0, 255,0), thickness=1, lineType=4, shift=0)
# cv2.circle(r,(200,150),50,(0,0,255),-1,4,0)
# Draw an ellipse
cv2.putText(img=r1, text="ADARSH", org=(245, 159), fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=0.3, color=(0, 255, 0), thickness=1, lineType=4, bottomLeftOrigin=False)

cv2.ellipse(img=r1, center=(198, 153), axes=(50, 70), angle=-2, startAngle=10, endAngle=360, color=(0, 255, 0), thickness=1, lineType=16, shift=0)

# cv2.imshow("imagge",r)
cv2.imshow("ellipse",r1) 
cv2.waitKey(0)
cv2.destroyAllWindows() 
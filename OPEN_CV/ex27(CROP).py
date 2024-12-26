import cv2
img=cv2.resize(cv2.imread("car.jpg"),(400,400))
# crope[height,width]
#{startY:endY,startX:endX}
# {height,width}=[y1:y2,x1:x2]
crop=img[170:260,150:310]


cv2.imshow("origanal",img)
cv2.imshow("crop",crop)

cv2.waitKey(0)
cv2.destroyAllWindows()
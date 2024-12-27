import cv2
 
img= cv2.imread("potrate.jpg")
crop=img[11:236,197:337]
img[11:236,337:477]=crop
img[11:236,57:197]=crop

cv2.imshow("window",img)
cv2.imwrite("potrate1.jpg",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
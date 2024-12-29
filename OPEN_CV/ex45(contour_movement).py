import cv2
import numpy as np

# Load and preprocess the image
i = cv2.resize(cv2.imread("shape.png"), (500, 500))
img = cv2.cvtColor(i, cv2.COLOR_BGR2GRAY)
_, th = cv2.threshold(img, 200, 255, cv2.THRESH_BINARY)

# Find contours
cnt, h = cv2.findContours(th, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)



ar=[]
# Iterate through each contour
for c in cnt:
    m = cv2.moments(c)
    
    # Calculate centroid only if area is non-zero
    # if m["m00"] != 0:
    x = int(m["m10"] / m["m00"])
    y = int(m["m01"] / m["m00"])
        
    # Draw the contour and centroid
    cv2.drawContours(i, cnt, -1, (0, 0, 0), 2)
    cv2.circle(i, (x, y), 5, (0, 0, 0), -1)
    
    #finding the area of the contour
    area = cv2.contourArea(c)
    ar.append(area)

print(ar)
# Display the image
cv2.imshow("Image with Contours", i)
cv2.waitKey(0)
cv2.destroyAllWindows()
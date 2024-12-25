import cv2

a = cv2.imread(r"C:\Users\adarsh\Downloads\New folder\ADARSH.jpg")
r = cv2.resize(a, (400, 600))

# Draw a line 
cv2.line(img=r, pt1=(200, 100), pt2=(300, 400), color=(0, 255, 0), thickness=4, lineType=4, shift=0)

# Draw a rectangle
cv2.rectangle(img=r, pt1=(145, 100), pt2=(250, 235), color=(0, 255, 0), thickness=4, lineType=4, shift=0)

# Add text to the image
cv2.putText(img=r, text="ADARSH", org=(145, 90), fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=0.7, color=(200, 0, 0), thickness=2, lineType=4, bottomLeftOrigin=False)


# Display the image
cv2.imshow("image", r)
cv2.waitKey(0)
cv2.destroyAllWindows()
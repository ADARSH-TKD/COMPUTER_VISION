import cv2
import numpy as np

# Load and resize the image
image_path = r"C:\Users\adarsh\Downloads\New folder\ADARSH.jpg"
img = cv2.imread(image_path)

    # Resize the image
img = cv2.resize(img, (400, 600))

    # Apply Canny edge detection
new_img = cv2.Canny(image=img, threshold1=400, threshold2=300 , edges=None, apertureSize=3, L2gradient=False)

    # Display the combined image
cv2.imshow("image", new_img)


cv2.waitKey(0)
cv2.destroyAllWindows()

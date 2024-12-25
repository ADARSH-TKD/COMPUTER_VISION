import cv2
import numpy as np

# Load the image
a = cv2.imread(r"C:\Users\adarsh\Downloads\New folder\ADARSH.jpg")

# Check if the image is loaded successfully
if a is None:
    print("Image not found. Please check the path.")
else:
    # Resize the image
    r = cv2.resize(a, (400, 600))

    # Define points for the polyline
    points = np.array([[100, 100], [150, 400], [200, 500], [250, 300]])

    # Draw the polyline on the image
    cv2.polylines(img=r, pts=[points], isClosed=False, color=(0, 255, 0), thickness=4, lineType=4)

    # Display the image
    cv2.imshow("image", r)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

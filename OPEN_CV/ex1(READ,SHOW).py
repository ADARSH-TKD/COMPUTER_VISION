import cv2
# a = cv2.imread("love.jpg")  # Reads the image
# cv2.imshow("Image", a)      # Displays the image with a window title
# cv2.waitKey(0)              # Waits for a key press indefinitely
# cv2.destroyAllWindows()     # Closes all OpenCV windows

#  CLOSING-ONE-BY-ONE 
# # Load and display the first image
# a = cv2.imread("love.jpg")  
# cv2.imshow("Image", a)

# # Load and display the second image
# b = cv2.imread("car.jpg")
# cv2.imshow("image2", b)

# # Wait for a key press
# cv2.waitKey(0)

# # Close only the first window
# cv2.destroyWindow("Image")

# # Optionally, wait again before closing the second window
# cv2.waitKey(0)
# cv2.destroyWindow("image2")

# MORE -EFFICIENT-WAY
# # Load images
# images = {
#     "Image": cv2.imread("love.jpg"),
#     "Image2": cv2.imread("car.jpg")
# }

# # Display all images in separate windows 
# for name, img in images.items():
#     cv2.imshow(name, img)

# # Wait for a key press
# cv2.waitKey(0)

# # Close all windows
# cv2.destroyAllWindow()

# MORE -EFFICIENT-WAY CLOSE ONE BY ONE 
import cv2

# Load images
images = {
    "Image2": cv2.imread("car.jpg"),
    "Image1": cv2.imread("love.jpg")
}

# Display all images in separate windows
for name, img in images.items():
    cv2.imshow(name, img)

# Close windows one by one
for name in images.keys():  # Correct method is keys()
    cv2.waitKey(0)  # Wait for a key press
    cv2.destroyWindow(name)  # Close the current window

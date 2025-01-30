# import cv2

# # Read the base image
# base_img = cv2.imread("love.jpg")

# # Read the overlay image
# overlay_img = cv2.imread("car.jpg")

# # Resize the overlay image to fit within the base image
# overlay_img_resized = cv2.resize(overlay_img, (200, 300))

# # Define the position where the overlay image will be placed
# x_offset = 50
# y_offset = 50

# # Get the region of interest (ROI) from the base image
# rows, cols, channels = overlay_img_resized.shape
# roi = base_img[y_offset:y_offset+rows, x_offset:x_offset+cols]

# # Create a mask of the overlay image and its inverse mask
# overlay_gray = cv2.cvtColor(overlay_img_resized, cv2.COLOR_BGR2GRAY)
# ret, mask = cv2.threshold(overlay_gray, 1, 255, cv2.THRESH_BINARY)
# mask_inv = cv2.bitwise_not(mask)

# # Black-out the area of the overlay image in the ROI
# base_img_bg = cv2.bitwise_and(roi, roi, mask=mask_inv)

# # Take only the region of the overlay image
# overlay_img_fg = cv2.bitwise_and(overlay_img_resized, overlay_img_resized, mask=mask)

# # Put the overlay image in the ROI and modify the base image
# dst = cv2.add(base_img_bg, overlay_img_fg)
# base_img[y_offset:y_offset+rows, x_offset:x_offset+cols] = dst

# # Display the result
# cv2.imshow("Overlay Image", base_img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
import cv2
import numpy as np

# Load the image
img = cv2.imread(r"C:\Users\adarsh\Downloads\New folder\ADARSH.jpg")

# Resize the image
rs = cv2.resize(img, (400, 600))

# Create a mask for the ellipse
mask = np.zeros_like(rs, dtype=np.uint8)

# Draw the ellipse on the mask
cv2.ellipse(mask, center=(200, 160), axes=(50, 100), angle=-2,
            startAngle=0, endAngle=360, color=(255, 255, 255),
            thickness=-1, lineType=4)

# Apply Gaussian blur to the entire image
blurred = cv2.GaussianBlur(rs, (15, 15), 0)

# Combine the blurred and original image using the mask
result = np.where(mask == 255, blurred, rs)

# Display the result
cv2.imshow("Blurred Ellipse", result)
cv2.waitKey(0)
cv2.destroyAllWindows()

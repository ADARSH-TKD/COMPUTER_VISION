import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the images
img1 = cv2.imread("p1.jpg")
img2 = cv2.imread("p2.jpg")
img3 = cv2.imread("p3.jpg")

# Check if the images are loaded properly
if img1 is None or img2 is None or img3 is None:
    print("Error: One or more images could not be loaded.")
else:
    # Calculate histograms for the images
    h1 = cv2.calcHist([img1], [0], None, [256], [0, 256])
    h2 = cv2.calcHist([img2], [0], None, [256], [0, 256])
    h3 = cv2.calcHist([img3], [0], None, [256], [0, 256])

    # Plot histograms
    plt.figure(figsize=(5, 5), facecolor="black", edgecolor="green")
    plt.subplot(3, 1, 1)
    plt.title("Image 1", color="white")
    plt.plot(h1, label="Image 1", color="blue")
    plt.xlabel("Pixel Intensity", color="white")
    plt.ylabel("Frequency", color="white")
    plt.tick_params(axis='x', colors='white')
    plt.tick_params(axis='y', colors='white')

    plt.subplot(3, 1, 2)
    plt.title("Image 2", color="white")
    plt.plot(h2, label="Image 2", color="green")
    plt.xlabel("Pixel Intensity", color="white")
    plt.ylabel("Frequency", color="white")
    plt.tick_params(axis='x', colors='white')
    plt.tick_params(axis='y', colors='white')

    plt.subplot(3, 1, 3)
    plt.title("Image 3", color="white")
    plt.plot(h3, label="Image 3", color="red")
    plt.xlabel("Pixel Intensity", color="white")
    plt.ylabel("Frequency", color="white")
    plt.tick_params(axis='x', colors='white')
    plt.tick_params(axis='y', colors='white')

    plt.tight_layout()
    plt.show()

    # Concatenate and display the images horizontally
    h = cv2.resize(np.hstack((img1, img2, img3)), (1000, 300))

    cv2.imshow("Concatenated Images", h)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

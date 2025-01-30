import cv2
import numpy as np 

def nothing(x):
    pass

# Create a window for the trackbars
cv2.namedWindow("Trackbars")

cv2.createTrackbar("th", "Trackbars", 0, 255, nothing)  # Lower Blue
# Add trackbars for HSV lower and upper bounds
cv2.createTrackbar("LB", "Trackbars", 0, 255, nothing)  # Lower Blue
cv2.createTrackbar("LG", "Trackbars", 0, 255, nothing)  # Lower Green
cv2.createTrackbar("LR", "Trackbars", 0, 255, nothing)  # Lower Red

cv2.createTrackbar("HB", "Trackbars", 255, 255, nothing)  # Upper Blue
cv2.createTrackbar("HG", "Trackbars", 255, 255, nothing)  # Upper Green
cv2.createTrackbar("HR", "Trackbars", 255, 255, nothing)  # Upper Red

# Open video capture
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if ret:
        
        th = cv2.getTrackbarPos("th", "Trackbars")
        # Get the current positions of the trackbars
        LB = cv2.getTrackbarPos("LB", "Trackbars")
        LG = cv2.getTrackbarPos("LG", "Trackbars")
        LR = cv2.getTrackbarPos("LR", "Trackbars")

        HB = cv2.getTrackbarPos("HB", "Trackbars")
        HG = cv2.getTrackbarPos("HG", "Trackbars")
        HR = cv2.getTrackbarPos("HR", "Trackbars")

        #resize the frame
        
        
        # Create lower and upper bounds for the mask
        lower = np.array([LB, LG, LR])
        upper = np.array([HB, HG, HR])

        # Flip the frame for a mirrored effect
        frame = cv2.flip(frame, 1)
        frame= cv2.resize(frame,(400,400))
        frame=frame[100:300,100:300]
        # Convert the frame to HSV
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # Create a mask based on the HSV bounds
        mask = cv2.inRange(hsv, lower, upper)

        # Apply the mask to the original frame
        res = cv2.bitwise_and(frame, frame, mask=mask)
        
        # Invert the masked result and apply binary thresholding
        fr = cv2.bitwise_not(res)
        gray = cv2.cvtColor(fr, cv2.COLOR_BGR2GRAY)  # Convert to grayscale     for thresholding
        _, thi = cv2.threshold(gray, th, 255, cv2.THRESH_BINARY)

        # Find contours
        cnt, _ = cv2.findContours(thi, cv2.RETR_TREE, cv2. CHAIN_APPROX_SIMPLE)

        # Draw contours on the original frame
        cv2.drawContours(frame, cnt, -1, (0, 255, 0), 2)
        for c in cnt:
            # m = cv2.moments(c)
            # if m["m00"] != 0:
            #     x = int(m["m10"] / m["m00"])
            #     y = int(m["m01"] / m["m00"])
                # cv2.circle(frame, (x, y), 5, (0, 0, 0), -1)
    
            area = cv2.contourArea(c)
            if area > 100:  # Ignore small contours
                epsilon = 0.001 * cv2.arcLength(c, True)
                approx = cv2.approxPolyDP(c, epsilon, True)
                hull = cv2.convexHull(approx)
                bx, by, bw, bh = cv2.boundingRect(hull)
                cv2.rectangle(frame, (bx, by), (bx + bw, by + bh), (0, 0, 255), 2)

        
        
        # Display the resulting frames
        cv2.imshow("Threshold", thi)
        cv2.imshow("Result", res)
        cv2.imshow("Mask", mask)
        cv2.imshow("Original with Contours", frame)
    
       
        # Break the loop when the space bar is pressed
        if cv2.waitKey(25) & 0xFF == ord(' '):
            break
    else:
        break

# Release resources
cap.release()
cv2.destroyAllWindows()

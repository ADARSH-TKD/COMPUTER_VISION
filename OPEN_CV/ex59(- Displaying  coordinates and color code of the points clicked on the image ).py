import cv2

def click_b(event, x, y, flags, param):
    global r  # Use the resized image
    if event == cv2.EVENT_LBUTTONDOWN:
        S = f"{x},{y}"  # Corrected format string (lowercase 'f')
        cv2.putText(r, S, (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 0, 0), 2)
        cv2.imshow("original", r)  # Update the displayed image
    elif event == cv2.EVENT_RBUTTONDOWN:
        b = img[y,x,0]
        g = img[y,x,1]
        r = img[y,x,2]
        s = f"{b},{g},{r}"
        cv2.putText(img,s,(x,y),cv2.FONT_HERSHEY_PLAIN,0.5,(0,0,0))
        cv2.imshow("original",img)
    
    
img = cv2.imread("BALL.jpg")
r = cv2.resize(img, (800, 500))  # Resize the image

cv2.imshow("original", r)  # Create the window first
cv2.setMouseCallback("original", click_b)  # Set the mouse callback function

cv2.waitKey(0)
cv2.destroyAllWindows()

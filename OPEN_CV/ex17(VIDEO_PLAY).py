import cv2

cap = cv2.VideoCapture("video.mp4")
while cap.isOpened():
    ret, frame = cap.read()
    if ret == True:
        cv2.imshow("frame", frame)
        if cv2.waitKey(5) & 0xFF == ord('p'):  # Stop if 'p' key is pressed
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()

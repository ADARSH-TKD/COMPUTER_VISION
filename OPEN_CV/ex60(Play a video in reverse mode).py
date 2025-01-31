import cv2
cap = cv2.VideoCapture("Ball Bouncing_2.mp4")
l = []
c = 1
while cap.isOpened():
    ret,frame = cap.read()
    if ret == True:
        cv2.imshow("video",frame)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
    else:
        break
cap.release()
cv2.destroyAllWindows()

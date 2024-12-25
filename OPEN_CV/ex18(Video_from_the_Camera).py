import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if ret == True:
        cv2.imshow("frame", frame)
        if cv2.waitKey(25) & 0xFF == ord(' '):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()
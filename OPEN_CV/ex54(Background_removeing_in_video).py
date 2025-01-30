import cv2

cap = cv2.VideoCapture("videoplayback.mp4")  # Load the video file

algo1 = cv2.createBackgroundSubtractorMOG2(detectShadows= True)
algo2 = cv2.createBackgroundSubtractorKNN(detectShadows= True)


while True:
    ret,frame = cap.read()  # Read the frame
    if ret == True:
        r1 = algo1.apply(frame)
        r2 = algo2.apply(frame)
        cv2.imshow("MOG2", r1)
        cv2.imshow("KNN", r2)
        cv2.imshow("Original", frame)
        if cv2.waitKey(40) & 0xFF == ord("q"):
            break
    else:
        break


cap.release()
cv2.destroyAllWindows()
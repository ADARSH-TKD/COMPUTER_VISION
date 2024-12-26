import cv2
cap= cv2.VideoCapture("video.mp4")
sub_m=cv2.createBackgroundSubtractorMOG2()
while True:
    ret,frame=cap.read()
    if ret==True: 
        new_frame=sub_m.apply(frame)
        cv2.imshow("frame",new_frame)
        if cv2.waitKey(25) & 0xFF==ord(' '):
            break
    else:
            break
        
cap.release()
cv2.destroyAllWindows()
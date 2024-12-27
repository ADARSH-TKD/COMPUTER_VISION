import cv2
cap= cv2.VideoCapture(0)
# sub=cv2.createBackgroundSubtractorMOG2()
f= cv2.VideoWriter_fourcc(*"XVID")
out= cv2.VideoWriter(filename="adarsh.mp4", fourcc=f, fps=40.0, frameSize=(640,480), isColor=True)
while True:
    ret,frame =cap.read()
    if ret == True:
        frame=cv2.flip(frame,1)
        # a=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY) # 0
        # new= sub.apply(frame) # 0,1
        out.write(frame)
        cv2.imshow("WINDOW",frame)
        if cv2.waitKey(30) & 0xFF == ord("p"):
            break
    else:
        break
    
cap.release()
cv2.destroyAllWindows()
        
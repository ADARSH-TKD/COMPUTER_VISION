import cv2

# Open the video file twice
cap1 = cv2.VideoCapture("video.mp4")
cap2 = cv2.VideoCapture("video.mp4")

while cap1.isOpened() and cap2.isOpened():
    # Read frames from the first video (fast playback)
    ret1, frame1 = cap1.read()
    # Read frames from the second video (slow playback)
    ret2, frame2 = cap2.read()

    if ret1:
        cv2.imshow("Video 1 (Fast)", frame1)
    if ret2:
        cv2.imshow("Video 2 (Slow)", frame2)

    # Control the speed of playback
    key = cv2.waitKey(1)  # Faster video
    if key == ord('q'):  # Break on 'q'
        break

    # Slower video delay (additional delay for the second video)
    if ret2 and key == -1:
        cv2.waitKey(20)

# Release the video capture objects and close the windows
cap1.release()
cap2.release()
cv2.destroyAllWindows()

import cv2

# open camera
cap = cv2.VideoCapture('/dev/video0', cv2.CAP_V4L)

# set dimensions
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 2560)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1440)

while True:
    # take frame
    ret, frame = cap.read()

    # check if the frame is valid
    if not ret:
        print("Error reading frame.")
        break

    # display the frame in a window
    cv2.imshow('Video Feed', frame)

    # exit the loop on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# release camera and close window
cap.release()
cv2.destroyAllWindows()

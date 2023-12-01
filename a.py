import cv2

# Open a video capture object (0 indicates the default camera)
cap = cv2.VideoCapture(0)

# Check if the camera opened successfully
if not cap.isOpened():
    print("Error: Couldn't open the camera.")
    exit()

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # If the frame is read correctly, ret will be True
    if ret:
        # Display the frame
        cv2.imshow('Video Feed', frame)

        # Break the loop if 'q' key is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        print("Error: Couldn't read a frame.")
        break

# Release the capture object and close all windows
cap.release()
cv2.destroyAllWindows()

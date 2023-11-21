import cv2

# Use the correct video device
camera = cv2.VideoCapture('/dev/video2')

while True:
    success, frame = camera.read()

    if not success:
        print("Failed to capture frame")
        break

    cv2.imshow('Camera Feed', frame)

    # Break the loop if 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close the window
camera.release()
cv2.destroyAllWindows()

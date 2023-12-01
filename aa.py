import cv2
import threading

def capture_frames(cap):
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error reading frame.")
            break
        cv2.imshow('Video Feed', frame)
        if cv2.waitKey(1) == ord('q'):
            break

# Open camera
cap = cv2.VideoCapture('/dev/video0', cv2.CAP_V4L)

# Set dimensions and frame rate
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
cap.set(cv2.CAP_PROP_FPS, 30)

# Start a separate thread for capturing frames
capture_thread = threading.Thread(target=capture_frames, args=(cap,))
capture_thread.start()

# Wait for the capture thread to finish
capture_thread.join()

# Release resources
cap.release()
cv2.destroyAllWindows()

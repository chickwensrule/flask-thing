from flask import Flask, render_template, Response
import cv2
import threading

app = Flask(__name__)
camera = cv2.VideoCapture("/dev/video0", cv2.CAP_V4L)  # Use the default camera (you may need to adjust this)

def capture_frames():
    while True:
        success, frame = camera.read()
        if not success:
            break
        else:
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    return Response(capture_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

def flask_thread():
    app.run(debug=False)

if __name__ == '__main__':
    # Start a separate thread for Flask app
    flask_thread = threading.Thread(target=flask_thread)
    flask_thread.start()

    # Start a separate thread for capturing frames
    capture_thread = threading.Thread(target=capture_frames)
    capture_thread.start()

    # Wait for both threads to finish
    flask_thread.join()
    capture_thread.join()

    # Release resources
    camera.release()
    cv2.destroyAllWindows()

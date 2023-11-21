app = Flask(__name__)
camera = cv2.VideoCapture("/dev/video1")

print("Camera opened:", camera.isOpened())  # Add this line

# ... rest of the code

if __name__ == '__main__':
    app.run(debug=True)

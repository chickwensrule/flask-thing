ffmpeg -f v4l2 -i /dev/video0 -vcodec libx264 -preset ultrafast -tune zerolatency -an -f mpegts udp://0.0.0.0:8080

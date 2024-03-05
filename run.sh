#ffmpeg -f v4l2 -i /dev/video0 -vcodec libx264 -preset ultrafast -tune zerolatency -an -f mpegts udp://0.0.0.0:8080

ffmpeg -s 1024x786 -i /dev/video0 -preset ultrafast -tune zerolatency -codec libx264 -f mpegts udp://192.168.1.2:8080

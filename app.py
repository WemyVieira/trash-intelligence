import cv2
camera = cv2.VideoCapture('rtsp://192.168.0.2:8080/video/h264')
while True:
    conectado, frame = camera.read()
    print(conectado)
    cv2.imshow('teste', frame)
    if cv2.waitKey(1) == ord('q'):
        break

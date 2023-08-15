# computer vision - cv

import cv2

cap=cv2.VideoCapture(0)

while True:
    __. frame=cap.read()
    cv2.imshow('output',frame)
    if cv2.waitkey(10)==ord('q'):
        break

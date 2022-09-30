import numpy as np
import cv2

cap = cv2.VideoCapture('Resources/elon.mp4')
while True:
    success, img = cap.read()
    crop_img = img[100:200,200:500]
    cv2.imshow('Output', crop_img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
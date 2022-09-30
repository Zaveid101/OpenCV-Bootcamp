import numpy as np
import cv2

haarcascade = "Resources/haarcascade_frontalface_default.xml"
img = cv2.imread("Resources/lena.png")

imgcascade = cv2.CascadeClassifier(haarcascade)
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgfaces = imgcascade.detectMultiScale(img_gray, 1.1, 4)
for (x,y,w,h) in imgfaces:
        cv2.rectangle(img ,(x,y), (x+w,y+h), (0,255,0), 2)

cv2.imshow("image",img)
cv2.waitKey(0)

cap = cv2.VideoCapture('Resources/elon.mp4')
while True:
    success, video = cap.read()
    print(video.shape)

    videocascade = cv2.CascadeClassifier(haarcascade)
    video_gray = cv2.cvtColor(video, cv2.COLOR_BGR2GRAY)

    videofaces = videocascade.detectMultiScale(video_gray, 1.1, 4)

    for (x,y,w,h) in videofaces:
        cv2.rectangle(video ,(x,y), (x+w,y+h), (0,255,0), 2)

    cv2.imshow("video",video)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
import numpy as np
import cv2

img = np.zeros((512, 512, 3), np.uint8)
print(img.shape)
img[:] = 255,255,255 #BGR 0,0,0
cv2.circle(img, (128,128), 50, (255,255,0), cv2.FILLED)
cv2.circle(img, (384,128), 50, (255,255,0), cv2.FILLED)
cv2.line(img, (78,78), (178,178), (0,255,0), 3)
cv2.line(img, (78,178), (178,78), (0,255,0), 3)
cv2.line(img, (334,78), (434,178), (0,255,0), 3)
cv2.line(img, (334,178), (434,78), (0,255,0), 3)
cv2.rectangle(img, (78,78), (178, 178), (0,0,255), 3)
cv2.rectangle(img, (334,78), (434, 178), (0,0,255), 3)
#center,axis xy,clockwise/anticlockwise,start angle,end angle,colour,thickness
cv2.ellipse(img,(256,256),(100,50),0,0,180,(255,0,0),cv2.FILLED)
cv2.imshow('Image', img)
cv2.waitKey(0)
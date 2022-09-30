import numpy as np
import cv2

img1= cv2.imread("Resources/lambo.png")

resized_img1 = cv2.resize(img1, (300, 200))
cv2.imshow('Resized_Output', resized_img1)
cv2.waitKey(0)

img2= cv2.imread("Resources/robot.png")
resized_img2 = cv2.resize(img2, (300, 200))
cv2.imshow('Resized_Output', resized_img2)
cv2.waitKey(0)

img_hor = np.hstack((resized_img1, resized_img2))
img_var = np.vstack((resized_img1, resized_img2))

cv2.imshow("Horizontal", img_hor)
cv2.imshow("Vertical", img_var)
cv2.waitKey(0)
import numpy as np
import cv2

width , height = 512, 512

img = cv2.imread("Resources/docs.jpg")
pts1 = np.float32([[720,24],[1110,15],[746,540],[1225,536]])
pts2 = np.float32([[0,0], [width, 0], [0,height], [width, height]])

metrix = cv2.getPerspectiveTransform(pts1, pts2)
img_out = cv2.warpPerspective(img, metrix, (width, height))

cv2.imshow('docs', img)
cv2.imshow('vert_docs', img_out)

cv2.waitKey(0)
import cv2
import numpy as np
cap = cv2.VideoCapture('output.avi')
frameCount = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
frameWidth = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frameHeight = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
print(frameCount,frameWidth,frameHeight)
buf = np.empty((frameCount, frameHeight, frameWidth, 3), np.dtype('uint8'))
fc = 0
ret = True
while (fc < frameCount  and ret):
    ret, buf[fc] = cap.read()
    fc += 1
cap.release()
cv2.namedWindow('ultimo frame')
cv2.imshow('ultimo frame', buf[fc-1])
cv2.waitKey(0)

import numpy as np
from PIL import ImageGrab
import cv2

SCREEN_SIZE = (1920, 1080)

fourcc = cv2.VideoWriter_fourcc(*"XVID")
# 20 frames por segungo
out = cv2.VideoWriter("output.avi", fourcc, 20, (SCREEN_SIZE))
n = 0
while(True):
    n += 1
    imagen =  ImageGrab.grab()
    printscreen_numpy =   np.array(imagen.getdata(),dtype='uint8')\
            .reshape((imagen.size[1], imagen.size[0], 3)) 
    print(imagen.size[1], imagen.size[0])
    # cv2.imshow('window',printscreen_numpy)
    frame = cv2.cvtColor(printscreen_numpy, cv2.COLOR_BGR2RGB)
    # write the frame
    out.write(frame)
    c = cv2.waitKey(1)

    print(c)
    if c == 27:
        cv2.destroyAllWindows()
        break
print(n)
cv2.destroyAllWindows()
out.release()    
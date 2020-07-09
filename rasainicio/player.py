import cv2
cap = cv2.VideoCapture("D:/jviejo/Downloads/video_tarragona.mp4")

altura = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
anchura = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
fps = cap.get(cv2.cv2.CAP_PROP_FPS)



cv2.namedWindow('video', cv2.WINDOW_NORMAL)
cv2.resizeWindow('video',(700, int(700 * 1080 / 1920)))

while (cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        imS = cv2.resize(frame, (640, 480))  
        cv2.imshow("video", imS)
        k = cv2.waitKey(25)
        if k == ord('q'):
            break   
    else:
      break

cap.release()
cv2.destroyAllWindows()
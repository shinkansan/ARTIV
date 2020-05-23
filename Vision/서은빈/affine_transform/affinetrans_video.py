import cv2
import numpy as np

#img = cv2.imread('./test.png')

cap = cv2.VideoCapture('5_14_12_37.avi')

while(cap.isOpened()):
    ret, img = cap.read()
    img = img[:][200:600]

    pts1 = np.float32([[836,223],[482,397],[1032,223],[1312,397]])

    pts2 = np.float32([[10,10],[10,1000],[1000,10],[1000,1000]])

    
    cv2.circle(img, (504,1003), 20, (255,0,0),-1)
    cv2.circle(img, (243,1524), 20, (0,255,0),-1)
    cv2.circle(img, (1000,1000), 20, (0,0,255),-1)
    cv2.circle(img, (1280,1685), 20, (0,0,0),-1)

    M = cv2.getPerspectiveTransform(pts1, pts2)

    dst = cv2.warpPerspective(img, M, (1100,1100))

  
    cv2.imshow('original', img)
    cv2.imshow('affine',dst)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

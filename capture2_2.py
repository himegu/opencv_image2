import numpy as np
import cv2

def myfunc(i):
    global dst
    ret, dst=cv2.threshold(frame_g, i, 255, cv2.THRESH_BINARY)
    

cv2.namedWindow('title') 

cv2.createTrackbar('value', # name of value
                   'title', # win name
                   0, # min
                   255, # max
                   myfunc) # callback func


cap = cv2.VideoCapture(1)
cap.set(3,1280)
cap.set(4,800)
cap.set(5,15)


while(True):

    ret, frame = cap.read()
    if not ret: continue

    frame_g=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    v = cv2.getTrackbarPos('value',  # get the value
                           'title')  # of the win

    ## do something by using v
    myfunc(v)

    cv2.imshow('title', dst)# show in the win

    k = cv2.waitKey(1)
    if k == ord('q') or k == 27:
        break



cap.release()
cv2.destroyAllWindows()
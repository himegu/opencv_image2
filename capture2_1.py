import numpy as np
import cv2

def myfunc(x):
    global output
    
    output = cv2.bilateralFilter(frame,15,x,x)


cv2.namedWindow('title') # create win with win name

cv2.createTrackbar('value', # name of value
                   'title', # win name
                   0, # min
                   100, # max
                   myfunc) # callback func


cap = cv2.VideoCapture(1)
cap.set(3,1280)
cap.set(4,800)
cap.set(5,15)


while(True):

    ret, frame = cap.read()
    if not ret: continue

    #img_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
  
    v = cv2.getTrackbarPos('value',  # get the value
                           'title')  # of the win

    ## do something by using v
    myfunc(v)

    cv2.imshow('title', output)  # show in the win

    k = cv2.waitKey(1)
    if k == ord('q') or k == 27:
        break



cap.release()
cv2.destroyAllWindows()

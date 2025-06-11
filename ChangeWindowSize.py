import numpy as np
import cv2

scaling_factorx = 1
scaling_factory = 1

cap = cv2.VideoCapture(0)
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()  # ret = 1 if the video is captured; frame is the image
    
    # set frame size (e.g. 640x480; 320x240; 960x720), larger is slower    
    #ret = cap.set(cv2.CAP_PROP_FRAME_WIDTH,320)
    #ret = cap.set(cv2.CAP_PROP_FRAME_HEIGHT,240)
    frame=cv2.resize(frame,None,fx=scaling_factorx,fy=scaling_factory,interpolation=cv2.INTER_AREA)
    
    # Our operations on the frame come here    
    img = frame
    
    # Display the resulting image
    cv2.imshow('Smaller Window',img)
    if cv2.waitKey(1) & 0xFF == ord('q'):  # press q to quit
        break
        
# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
import numpy as np
import cv2

# create a VideoCapture object
cap = cv2.VideoCapture('eggs.avi')

# get the dimensions of the frame
# you can also read the first frame to get these
w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))  # width of the frame
h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)) # height of the frame

fourcc = cv2.VideoWriter_fourcc(*'XVID') # choose codec


# create VideoWriter object w by h, 30 frames per second
out = cv2.VideoWriter('eggs-reverse.avi',fourcc, 30.0, (w,h))
buffer=[]

while True:
    ret, I = cap.read()




    buffer.append(I)
    if ret == False: # end of video (or error)
        break

cap.release()

    # write the current frame I
    #out.write(I)

buffer.reverse()

for J in buffer:
    out.write(J)

out.release()

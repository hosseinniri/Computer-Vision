import numpy as np
import cv2

I = cv2.imread('coins.jpg')
G = cv2.cvtColor(I,cv2.COLOR_BGR2GRAY)
G = cv2.GaussianBlur(G, (5,5), 0);

canny_high_threshold = 160
min_votes = 35 # minimum no. of votes to be considered as a circle
min_centre_distance = 40
resolution = 1 # resolution of parameters (centre, radius) relative to image resolution

circles = cv2.HoughCircles(G,cv2.HOUGH_GRADIENT,resolution,min_centre_distance,
                           param1=canny_high_threshold,
                           param2=min_votes,minRadius=0,maxRadius=100)

for c in circles[0, :]:
    x = c[0]  # x coordinate of the centre
    y = c[1]  # y coordinate of the centre
    r = c[2]  # radius

    # draw the circle
    cv2.circle(I, (x, y), r, (180, 0, 0), 2)

n = circles.shape[1]
font = cv2.QT_FONT_NORMAL
cv2.putText(I,'There are %d coins!'%n,(400,40), font, 1,(255,0,0),2)

cv2.imshow("I",I)
cv2.waitKey(0)


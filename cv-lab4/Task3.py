#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 07:40:56 2020

@author: hossein
"""
import numpy as np
import cv2

I = cv2.imread('isfahan.jpg').astype(np.float64) / 255;



m = 13; # we will create an m by m filter

Jg=cv2.GaussianBlur(I,(m,m),0)

cv2.imshow('original',I)
cv2.waitKey()

cv2.imshow('blurred Gaussian',Jg)
cv2.waitKey()

cv2.destroyAllWindows()


#!/usr/bin/python3

import cv2
import numpy as np

cam = cv2.VideoCapture(0)
ret,frame = cam.read()

cv2.imshow('named',frame)
cv2.waitKey()

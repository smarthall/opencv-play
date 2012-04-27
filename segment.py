#!/usr/bin/python

import cv

cv.NamedWindow('a_window', cv.CV_WINDOW_AUTOSIZE)

capture = cv.CaptureFromCAM(-1)
cv.SetCaptureProperty(capture, cv.CV_CAP_PROP_FRAME_WIDTH, 320)
cv.SetCaptureProperty(capture, cv.CV_CAP_PROP_FRAME_HEIGHT, 240)

stor = cv.CreateMemStorage();

image = cv.QueryFrame(capture)
img = cv.CreateImage (cv.GetSize (image), 8, 3)
grey = cv.CreateImage (cv.GetSize (image), 8, 1)
eig = cv.CreateImage (cv.GetSize (image), 32, 1)
temp = cv.CreateImage (cv.GetSize (image), 32, 1)

count = 0
while count < 20000:
  image = cv.QueryFrame(capture)
  cv.PyrSegmentation(image, img, stor, 4, 255, 30)
  #for (x, y) in cv.GoodFeaturesToTrack(grey, eig, temp, 200, 0.01, 1.0, useHarris = True):
  #  cv.Circle(image, (int(x), int(y)), 3, (0, 255, 0), -1, 8, 0)
  cv.ShowImage('a_window', img)
  cv.WaitKey(2)
  #print count
  count += 1



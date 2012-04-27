#!/usr/bin/python

import cv

cv.NamedWindow('a_window', cv.CV_WINDOW_AUTOSIZE)

capture = cv.CaptureFromCAM(-1)
cv.SetCaptureProperty(capture, cv.CV_CAP_PROP_FRAME_WIDTH, 640)
cv.SetCaptureProperty(capture, cv.CV_CAP_PROP_FRAME_HEIGHT, 480)

image = cv.QueryFrame(capture)
grey = cv.CreateImage (cv.GetSize (image), 8, 1)
eig = cv.CreateImage (cv.GetSize (image), 32, 1)
temp = cv.CreateImage (cv.GetSize (image), 32, 1)

count = 0
while count < 20000:
  image = cv.QueryFrame(capture)
  cv.CvtColor(image, grey, cv.CV_BGR2GRAY)
  for (x, y) in cv.GoodFeaturesToTrack(grey, eig, temp, 200, 0.01, 1.0, useHarris = True):
    cv.Circle(image, (int(x), int(y)), 3, (0, 255, 0), -1, 8, 0)
  cv.ShowImage('a_window', image)
  cv.WaitKey(2)
  count += 1



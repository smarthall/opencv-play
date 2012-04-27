#!/usr/bin/python

import cv

cv.NamedWindow('a_window', cv.CV_WINDOW_AUTOSIZE)
capture = cv.CaptureFromCAM(0)
cv.SetCaptureProperty(capture, cv.CV_CAP_PROP_FRAME_WIDTH, 640)
cv.SetCaptureProperty(capture, cv.CV_CAP_PROP_FRAME_HEIGHT, 480)

#image = cv.LoadImage('pic.png', cv.CV_LOAD_IMAGE_COLOR)

font = cv.InitFont(cv.CV_FONT_HERSHEY_SIMPLEX, 1, 1, 0, 3, 8)
x = 5
y = 20
count = 0
while count < 250:
  image = cv.QueryFrame(capture)
  cv.PutText(image, "Hello World!!!", (x, y), font, 255)
  cv.ShowImage('a_window', image)
  cv.WaitKey(2)
  count += 1



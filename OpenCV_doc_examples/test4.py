# This example shows the use of OpenCV's trackbar functionalities. A
# window's color can be modified by using three RGB sliders and one
# ON/OFF slider.

import cv2
import numpy as np


def nothing(x):
    pass

# Create a black image, a window
img = np.zeros((300, 523, 3), np.uint8)
cv2.namedWindow('display')

# Create trackbars for color change
cv2.createTrackbar('R', 'display', 0, 255, nothing)
cv2.createTrackbar('G', 'display', 0, 255, nothing)
cv2.createTrackbar('B', 'display', 0, 255, nothing)

# Create switch for ON/OFF functionality
switch = '0 : OFF \n1 : ON'
cv2.createTrackbar(switch, 'display', 0, 1, nothing)

while 1:
    cv2.imshow('display', img)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break

    # Get current position of four trackbars
    r = cv2.getTrackbarPos('R', 'display')
    g = cv2.getTrackbarPos('G', 'display')
    b = cv2.getTrackbarPos('B', 'display')
    s = cv2.getTrackbarPos(switch, 'display')

    if s == 0:
        img[:] = 0
    else:
        img[:] = [b, g, r]

cv2.destroyAllWindows()

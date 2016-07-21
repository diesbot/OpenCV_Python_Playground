# This example uses cv drawing methods to demonstrate image
# modification.
# Also it makes use of the displaying method that was created in test1.

import numpy as np
import cv2
import test1

# colors
blue = (255, 0, 0)
green = (0, 255, 0)
red = (0, 0, 255)

# Create black image
img = np.zeros((512, 512, 3), np.uint8)

# Draw a diagonal blue line with thisckness of 5 px
img = cv2.line(img, (0, 0), (511, 511), blue, 5)
# Draw a green rectangle
img = cv2.rectangle(img, (384, 0), (510, 128), green, 3)
# Draw a red circle
img = cv2.circle(img, (447, 63), 63, red, -1)

# Display the image
test1.displayImage('display', img)

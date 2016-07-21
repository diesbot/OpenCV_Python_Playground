# In this example a program was created in which you can draw circles 
# and rectangles onto a black ground.
# It makes use of OpenCV's Callback functions.

import cv2
import numpy as np

# colors
blue = (255, 0, 0)
green = (0, 255, 0)
red = (0, 0, 255)

# states
drawing = False  # True if mouse is pressed
mode = True  # if True, draw rectangle. Press 'm' to toggle to curve
ix, iy = -1, -1


def main():

    global mode

    # Mouse callback function
    def draw_circle(event, x, y, flags, param):

        global ix, iy, drawing, mode

        if event == cv2.EVENT_LBUTTONDOWN:
            drawing = True
            ix, iy = x, y

        elif event == cv2.EVENT_MOUSEMOVE:
            if drawing:
                if mode:
                    cv2.rectangle(img, (ix, iy), (x, y), green, -1)
                else:
                    cv2.circle(img, (x, y), 5, red, -1)
        elif event == cv2.EVENT_LBUTTONUP:
            drawing = False
            if mode:
                cv2.rectangle(img, (ix, iy), (x, y), green, -1)
            else:
                cv2.circle(img, (x, y), 5, red, -1)

    img = np.zeros((512, 512, 3), dtype=np.uint8)

    cv2.namedWindow('display')
    cv2.setMouseCallback('display', draw_circle)

    while(True):
        cv2.imshow('display', img)
        k = cv2.waitKey(1) & 0xFF
        if k == ord('m'):
            mode = not mode
        elif k == 27:
            break

    cv2.destroyWindow('display')


if __name__ == '__main__':
    main()

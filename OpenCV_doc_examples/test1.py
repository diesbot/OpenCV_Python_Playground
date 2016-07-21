# This example introduces the basic methods for image reading and
# displaying via OpenCV and/or matplotlib.

import cv2
import matplotlib.pyplot as plt


# Displays an image in a normalized, scalable window
def displayImage(windowname, img):
    cv2.namedWindow(windowname, cv2.WINDOW_AUTOSIZE)
    cv2.imshow('display', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def main():
    # Load a color image in grayscale
    img = cv2.imread('images/sonnenblume.jpg', 0)
    displayImage('display', img)

    plt.imshow(img, cmap='gray', interpolation='none')
    plt.xticks([]), plt.yticks([])
    plt.show()


if __name__ == '__main__':
    main()

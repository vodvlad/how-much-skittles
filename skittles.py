import matplotlib.pyplot as plt
import numpy as np
from skimage.morphology import area_opening
import cv2.cv2 as cv2
from skimage import exposure
from skimage.measure import label
import sys, os
from os import path

def viewImage(image):
    cv2.namedWindow('Display', cv2.WINDOW_NORMAL)
    cv2.imshow('Display', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def main(argv):
    list = []
    for filename in os.listdir(argv[1]):
        if filename[filename.rfind(".") + 1:] in ['jpg', 'jpeg', 'png']:
                list.append(filename)

    for i in range(len(list)):
        full_name = path.basename(list[i])

        image = cv2.imread(argv[1] + '/' + full_name)
        viewImage(image)

        image_e = exposure.adjust_gamma(image, 2)
        hsv_img = cv2.cvtColor(image_e, cv2.COLOR_BGR2HSV)

        o_low = np.array([94, 27, 17])
        o_high = np.array([132, 255, 255])
        mask = cv2.inRange(hsv_img, o_low, o_high)
        viewImage(mask)

        cl = area_opening(mask, area_threshold=80)
        viewImage(cl)

        labels = label(cl)
        plt.imshow(labels)
        plt.show()
        print(labels.max())

if __name__ == "__main__":
    main(sys.argv)

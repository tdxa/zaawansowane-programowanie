import cv2
import numpy as np
import imutils
from imutils.object_detection import non_max_suppression

class Detector:
    def __init__(self):
        pass

    def load_img(self, path: str):
        img = cv2.imread(path)
        self._image = img
        self._width = img.shape[1]

    def show_image(self):
        cv2.imshow("Detection", self._image)

    def image_detect(self, path: str):
        self.load_img(path)
        self.show_image()
        cv2.waitKey()

    def video_detect(self):
        pass
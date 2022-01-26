from src.detector import Detector
from src.utils import photos_list

if __name__ == '__main__':
    detector = Detector()

    for photo in photos_list:
        detector.check_image(photo, 'HOG')

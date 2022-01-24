from src.detector import Detector

if __name__ == '__main__':
    detector = Detector()

    detector.check_image('images/people-2.jpg', 'HOG')

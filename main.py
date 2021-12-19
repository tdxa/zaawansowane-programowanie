import cv2
import matplotlib.pyplot as plt
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r"C:\\Program Files\\Tesseract-OCR\\tesseract.exe"


def main():
    img = cv2.imread('cooper.jpg')
    print(type(img))
    print(img)
    print(img.shape)

    img_convert = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    cv2.imshow('image', img_convert)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    plt.imshow(img)
    plt.show()


def get_image(path: str):
    return cv2.imread(path)


def prepare_image(path: str):
    img = cv2.cvtColor(get_image(path), cv2.COLOR_BGR2GRAY)
    return cv2.adaptiveThreshold(cv2.medianBlur(img, 3), 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 2)


def read_text(path):
    return pytesseract.image_to_string(prepare_image(path))


def print_text(images: list[str]):
    for img in images:
        print(".......................", read_text(img), sep='\n')


print_text(['text1.png', 'text3.png', 'text4.png'])

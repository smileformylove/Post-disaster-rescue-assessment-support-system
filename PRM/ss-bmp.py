import cv2 as cv
import numpy as np


def is_red(arr):
    newarr = list(map(int, arr))
    if newarr[2] > (newarr[0] + newarr[1]):
        return True
    elif newarr[2] > 200 and newarr[1] > 200:
        return True
    else:
        return False


def jpgtobmp(file):
    img = cv.imread(file)
    mask = np.ones(img.shape[:2], dtype=np.uint8)
    mask = 255 * mask
    for i in range(mask.shape[0]):
        for j in range(mask.shape[1]):
            if is_red(img[i, j]):
                mask[i, j] = 0
    # ret, thresh = cv.threshold(mask, 100, 255, cv.THRESH_BINARY)
    cv.imwrite(file.split('.')[0] + '.bmp', mask)


if __name__ == '__main__':
    jpgtobmp('ss.jpeg')
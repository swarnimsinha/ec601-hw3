import cv2
import numpy as np
import sys


def main():

    try:
        fn = sys.argv[1]
    except IndexError:
        fn = "Lenna.png"

    img = cv2.imread(fn)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    [cv, thresh] = cv2.threshold(gray, 128, 255, 2)
    cv2.imshow('Threshold', thresh)

    [cv, binThresh] = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY)
    cv2.imshow('Binary Threshold', binThresh)

    [cv, thresh1] = cv2.threshold(gray, 27, 255, cv2.THRESH_BINARY)
    [cv, thresh2] = cv2.threshold(gray, 125, 255, cv2.THRESH_BINARY_INV)
    bandThresh = cv2.bitwise_and(thresh1, thresh2)
    cv2.imshow('Band Threshold', bandThresh)

    [cv, thresh3] = cv2.threshold(
        gray, 128, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)
    semiThr = cv2.bitwise_and(gray, thresh3)
    cv2.imshow('Semi Threshold', semiThr)

    thresh4 = cv2.adaptiveThreshold(
        gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 101, 10)
    cv2.imshow('Adaptive Threshold', thresh4)

    cv2.waitKey(0)


if __name__ == "__main__":
    main()

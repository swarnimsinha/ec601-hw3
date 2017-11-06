import cv2
import numpy as np
import sys

def main():

    try:
        fn = sys.argv[1]
    except IndexError:
        fn = "Lenna.png"

    src = cv2.imread(fn, 1)

    b,g,r = cv2.split(src)

    #RGB chanels
    print("RGB value: ",src[20,25])
    #RED
    cv2.imwrite("RED.png",r)
    #BLUE
    cv2.imwrite("BLUE.png",b)
    #GREEN
    cv2.imwrite("GREEN.png",g)


    #YCrCb chanels
    img = cv2.cvtColor(src, cv2.COLOR_BGR2YCrCb)

    Y,Cr,Cb = cv2.split(img)

    print("YCrCb value: ",src[20,25])
    #RED
    cv2.imwrite("Yr.png",Y)
    #BLUE
    cv2.imwrite("Cr.png",Cr)
    #GREEN
    cv2.imwrite("Cb.png",Cb)


    #YCrCb chanels
    img = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)

    H,S,V = cv2.split(img)

    print("HSV value: ",src[20,25])
    #HUE
    cv2.imwrite("Hue.png",H)
    #Saturation
    cv2.imwrite("Saturation.png",S)
    #Value
    cv2.imwrite("Value.png",V)


    cv2.waitKey(0)

if __name__ == '__main__':
    main()
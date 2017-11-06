import cv2
import numpy as np
import sys

def Add_gaussian_Noise(pic, mean, sigma):
    
    noisyPic=pic.copy()
    cv2.randn(noisyPic,mean,sigma)
    cv2.add(pic, noisyPic, noisyPic)
    
    return noisyPic

def Add_salt_pepper_Noise(pic, pa, pb):
    amount1 = int(pic.shape[0]*pic.shape[1]*pa)
    amount2 = int(pic.shape[0]*pic.shape[1]*pb)
    
    picCopy=pic.copy()
    
    for i in range(amount1):
        picCopy[np.random.randint(0,pic.shape[0]-1), np.random.randint(0,pic.shape[1]-1)]=0
        
    for i in range(amount2):
        picCopy[np.random.randint(0,pic.shape[0]-1), np.random.randint(0,pic.shape[1]-1)]=255
        
    return picCopy

def main():
    mean = 0
    sigma = 100
    pa = 0.01
    pb = 0.01
    

    try:
        fn = sys.argv[1]
    except IndexError:
        fn = "Lenna.png"

    pic = cv2.imread(fn)
    gray = cv2.cvtColor(pic,cv2.COLOR_BGR2GRAY)
    cv2.imshow("./LennaGray.png",gray)
    
    gaussImg = Add_gaussian_Noise(gray,mean,sigma)
    cv2.imshow("./gaussianNoise.png",gaussImg)
    boxFilterImg = cv2.boxFilter(gaussImg, -1, (3, 3))
    cv2.imshow("./gaussianBoxfilter.png",boxFilterImg)
    gaussFilterImg=cv2.GaussianBlur(gaussImg, (3,3), 1.5, 3)
    cv2.imshow("./gaussianGaussfilter.png",gaussFilterImg)
    medianFilterImg=cv2.medianBlur(gaussImg,5)
    cv2.imshow("./gaussianMedianfilter.png",medianFilterImg)
    
    pepperSaltImg=Add_salt_pepper_Noise(gray,pa,pb)
    cv2.imshow("./peppersaltnoise.png",pepperSaltImg)
    boxFilterImg = cv2.boxFilter(pepperSaltImg, -1, (3, 3))
    cv2.imshow("./peppersaltBoxfilter.png",boxFilterImg)
    gaussFilterImg=cv2.GaussianBlur(pepperSaltImg, (3,3), 1.5, 3)
    cv2.imshow("./peppersaltGaussfilter.png",gaussFilterImg)
    medianFilterImg=cv2.medianBlur(pepperSaltImg,5)
    cv2.imshow("./peppersaltMedianfilter.png",medianFilterImg)

    cv2.waitKey(0)
    
if __name__ == "__main__":
    main()

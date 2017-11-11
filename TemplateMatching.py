import numpy as np
import cv2


# src: source image, temp: template image, stepsize: the step size for sliding the template
def TemplateMatching(src, temp, stepsize):
    mean_t = 0
    var_t = 0
    location = [0, 0]
    # Calculate the mean and variance of template pixel values
    # ------------------ Put your code below ------------------
    mean_t = np.mean(temp)
    var_t = np.var(temp)
    max_corr = 0
    # Slide window in source image and find the maximum correlation
    for i in np.arange(0, src.shape[0] - temp.shape[0], stepsize):
        for j in np.arange(0, src.shape[1] - temp.shape[1], stepsize):
            mean_s = 0
            var_s = 0
            corr = 0
            # Calculate the mean and variance of source image pixel values inside window
            # ------------------ Put your code below ------------------
            window = src[i:i + temp.shape[0], j:j + temp.shape[1]]
            mean_s = np.mean(window)
            var_s = np.var(window)
            # Calculate normalized correlation coefficient (NCC) between source and template
            # ------------------ Put your code below ------------------
            for k in range(0, temp.shape[0]):
                for l in range(0, temp.shape[1]):
                    corr += (window[k, l] - mean_s) * \
                        (temp[k, l] - mean_t)
            corr = corr / (temp.shape[0] * temp.shape[1] * var_s * var_t)
            if corr > max_corr:
                max_corr = corr
                location = [i, j]
    return location


# load source and template images
source_img = cv2.imread('source_img.jpg', 0)  # read image in grayscale
source = cv2.imread('source_img.jpg')   # read the image, later use this image for showing the matched template
temp = cv2.imread('template_img.jpg', 0)  # read image in grayscale
location = TemplateMatching(source_img, temp, 20)

# Draw a red rectangle on match_img to show the template matching result
# ------------------ Put your code below ------------------
match_img = cv2.rectangle(source, (location[1], location[0]), (
    location[1] + temp.shape[1], location[0] + temp.shape[0]), (0, 0, 255), 3)
# Save the template matching result image (match_img)
# ------------------ Put your code below ------------------
cv2.imwrite('MyTemplateMatching.jpg', match_img)
# Display the template image and the matching result
cv2.namedWindow('TemplateImage', cv2.WINDOW_NORMAL)
cv2.namedWindow('MyTemplateMatching', cv2.WINDOW_NORMAL)
cv2.imshow('TemplateImage', temp)
cv2.imshow('MyTemplateMatching', match_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

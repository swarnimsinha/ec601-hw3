# ec601-hw3
Q1) How does a program read the cvMat object, in particular, what is the order of the pixel structure?
A) A program can read the cvMat object in three ways:
    a) C style operators[] (pointers) - The efficient way
    b) The iterator method - The safe way
    c) Address calculation with reference returning - The .at method
Depending on the image, it can either be saved in a multichannel (colored) e.g. BGR or a single channel (greyscale) container

Q2) ColorImage.cpp is a program that takes a look at colorspace conversions in OpenCV. Run the code in ColorImage.cpp and comment on the outputs. Implement the same thing in Python and save each image.
A) ColorImage.cpp outputs each channel of the image independently.
Q2 - contd) What are the ranges of pixel values in each channel of each of the above mentioned colorspaces?
    a) RGB - 0-255
    b) YCbCr - Depending on the conversion, 0-255, 16-255 and 16-235-240 (JPEG uses 0-255)
    c) HSV - Ranges from 0 to 360°

Q3) Change the kernel sizes for all the filters with all different values for noises and print the results for 3x3, 5x5 and 7x7 kernels. Comment on the results. Which filter seems to work "better" for images with salt-and-pepper noise and Gaussian noise?
A) As the kernel size increases, the blurring/noise increases in all the examples apart from salt-and-pepper. Median filter is the most effective amongst all.
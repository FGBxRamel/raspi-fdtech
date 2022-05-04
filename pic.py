import imageio.v3 as iio
import numpy as np

# TODO: Write search algo 
# First: go trough every x pixel, look if pixel in color range, if yes then remember that pixel
# Second: Go to every one of that pixel, make average of the color of x*x pixels around the pixel, save that
# Third: Compare all the boxes, take one with highest match to given color
# Fourth: World domination



img = iio.imread("test3.jpg")
img_array = np.array(img)
print(img_array[1000][100])

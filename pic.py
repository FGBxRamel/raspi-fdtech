from turtle import width
import imageio.v3 as iio
import numpy as np

# TODO: Write search algo
# First: go trough every x pixel, look if pixel in color range, if yes then remember that pixel
# Second: Go to every one of that pixel, make average of the color of x*x pixels around the pixel, save that
# Third: Compare all the boxes, take one with highest match to given color
# Fourth: World domination

img = np.array(iio.imread("test3.jpg"))
print(img.shape)
length = 8

start = (0, 0)
done = False

while not done:
    if img.shape[1] < x + length or img.shape[0] < y + length:
        done = True
    else:
        median = list((0, 0, 0))
        for y in range(start[0], start[0]+length+1):
            for x in range(start[1], start[1]+length+1):
                for i in range(0, 3):
                    median[i] = median[i] + img[y, x][i]
        for j in range(0, 3):
            median[j] = median[j] / 64

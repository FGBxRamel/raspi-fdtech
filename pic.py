from turtle import width
import imageio.v3 as iio
import numpy as np

# TODO: Write search algo
# First: go trough every x pixel, look if pixel in color range, if yes then remember that pixel
# Second: Go to every one of that pixel, make average of the color of x*x pixels around the pixel, save that
# Third: Compare all the boxes, take one with highest match to given color
# Fourth: World domination

img = iio.imread("test3.jpg")
img_array = np.array(img)
length = 8
median = (0,0,0)

start = (0, 0)
done = False
for y in range(start[0], start[0]+length+1):
    for x in range(start[1], start[1]+length+1):
        for i in range(0,4):
            list(median)[i] = list(median)[i] + img_array[y][x][i]



while not done:
    pass 
import imageio.v3 as iio
import numpy as np

# TODO: Write own "downscaling" -> Take 4*4 pixels, make average color value (RGB) and and check against given color
# Don't forget what happens when you're at the end of the pic

img = iio.imread("test3.jpg")
img_array = np.array(img)
print(img_array[1000][100])

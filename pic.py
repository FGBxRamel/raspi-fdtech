import imageio.v3 as iio
import numpy as np

img = iio.imread("test3.jpg")
img_array = np.array(img)
print(img_array[1000][100])

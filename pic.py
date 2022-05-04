from operator import length_hint
import cv2 as cv
import numpy as np


class Color:
    """A class for a color.\n
    It needs a color code in the format of a list (R, G, B).\n
    Optional arguments:\n
        tolerance: is the range in which every color value ist okay (R+-x, G+-x, B+-x). Default: 5.\n
        length: The length of the sides of the downscaled picture. The bigger the number, the more precise (and long) it will be. Default: 128
    """

    def __init__(self, farbcode: list, tolerance: int = 5, length : int = 128) -> None:
        self.color = list(farbcode)
        self.tolerance = int(tolerance)
        self.length = int(length)
        self._addTolerance()

    def _addTolerance(self) -> list:
        """Internal function to add the given tolerance to the RGB list. Gives back a list, with a list with the start and stop value of the color value.\n
        Example: list[0] -> (145, 155)\n
        means that the R value can range from 145 to 155. list[1]; list[2] is G; B.
        """
        self.range = []
        for i in range(0, 3):
            self.range[i] = list(
                (self.color[i]-self.tolerance, self.color[i]+self.tolerance))
        return self.range

    def getY(self):
        # TODO Check if the found field is in an acceptable color range
        # If not: return None
        # TODO Change image to freshly taken one
        img = np.array(cv.resize(cv.imread("test3.jpg"), (self.length, self.length)))
        winner = {}
        # this dict has the structure: offset : pixel-y-coordinate 
        for y in range(0, self.length):
            for x in range(0, self.length):
                for i, pair in enumerate(self.range):
                    img_color = img[y, x][i]
                    if img_color <= pair[0] or img_color >= pair[1]:
                        offset = abs(img_color - self.color)
                        winner[offset] = y if not offset in winner.keys() else winner[offset]
                        



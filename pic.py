import cv2 as cv
import numpy as np
import io
import picamera


class Color:
    """A class for a color.\n
    Optional arguments:\n
        colorcode: can take a color code in the format of a list (R, G, B).\n
        If nothing is given it will make a fresh picture and take the average color in the middle of the picture.\n
        
        tolerance: is the range in which every color value ist okay (R+-x, G+-x, B+-x). Default: 20.\n
        
        length: The length of the sides of the downscaled picture. The bigger the number, the more precise (and long) it will be. Default: 128
    """

    def __init__(self, colorcode: list = (-1, -1, -1), tolerance: int = 10, length: int = 128) -> None:
        self.color = list(colorcode)
        self.tolerance = int(tolerance)
        self.length = int(length)
        self.color = self._getColor() if self.color[0] == -1 else self.color
        self._addTolerance()


    def _addTolerance(self) -> list:
        """Internal function to add the given tolerance to the RGB list. Gives back a list, with a list with the start and stop value of the color value.\n
        Example: list[0] -> (145, 155)\n
        means that the R value can range from 145 to 155. list[1]; list[2] is G; B.
        """
        self.range = []
        for i in range(0, 3):
            self.range.append(list(
                (int(self.color[i])-self.tolerance, int(self.color[i])+self.tolerance)))
        print(f"Tolerance list is {self.range}")
        return self.range

    def getY(self) -> int:
        """Gives back the y-Coordinate of the last pixel found matching the color."""
        img = self.getImage()
        # this dict has the structure: avg_offset : pixel-y-coordinate
        winner = {}
        for y in range(0, self.length):
            for x in range(0, self.length):
                # avg_offset is calculated with abs(pixel R_Value - Color_R_Value) + abs(G_value - Color_G_Value) + abs(B_Value - Color_B_Value)
                # It should find the pixel which is nearest to the given color
                avg_offset = 0
                # Get pairs of the color values, as seen in the _addTolerance func, and the index of them
                for i, pair in enumerate(self.range):
                    # Get the R/G/B Value of the pixel
                    img_color = img[y, x][i]
                    # If the pixel color is in the range, add the offset to the average, if not just ignore pixel
                    if img_color >= pair[0] and img_color <= pair[1]:
                        avg_offset += abs(img_color - self.color[i])
                        valid = True
                    else:
                        valid = False
                        break
                if valid:
                    winner[avg_offset] = y
        return winner[min(winner.keys())] if not len(winner) == 0 else None

    def _getColor(self) -> list:
        """Internal function for getting the average color of the middle pixels of a freshly taken picture. Gives back a list with the RGB values."""
        input("Press Enter to take the picture")
        img = self.getImage()
        avg = np.array((0,0,0), dtype=int)
        for y in range(self.length//2-10, self.length//2-4):
            for x in range(self.length//2-2, self.length//2+3):
                avg = np.add(avg, img[y, x])
        for i, num in enumerate(avg):
            avg[i] = num//25
        return avg

    def getImage(self) -> np.ndarray:
        """Takes a picture and gives it back as an numpy ndarray"""
        with picamera.PiCamera() as camera:
            camera.resolution = (self.length, self.length)
            img = np.empty((self.length * self.length * 3), dtype=np.uint8)
            camera.capture(img, "rgb")
            img = img.reshape((self.length, self.length, 3))
            return img


if __name__ == "__main__":
    color = Color()
    print(color.color)

"""
File: fire.py
---------------------------------
This file contains a method called
highlight_fires which detects the
pixels that are recognized as fire
and highlights them for better observation
"""
from simpleimage import SimpleImage


HURDLE_FACTOR = 1.05


def highlight_fires(filename):
    """
    :param filename: str, the file path of the original image
    :return: the image show the fired area in red color and unfired area in gray scale
    """
    img = SimpleImage(filename)
    for y in range(img.height):
        for x in range(img.width):
            pixel = img.get_pixel(x, y)
            avg = (pixel.red + pixel.green + pixel.blue)/3
            # the condition is to see the area is on fir or not
            if pixel.red > avg * HURDLE_FACTOR:
                pixel.red = 255
                pixel.blue = 0
                pixel. green = 0
            else:
                pixel.red = avg
                pixel.blue = avg
                pixel.green = avg
    return img


def main():
    """
    This program highlight the fired area in red color and unfired area in gray scale in a image
    """
    original_fire = SimpleImage('images/greenland-fire.png')
    original_fire.show()
    highlighted_fire = highlight_fires('images/greenland-fire.png')
    highlighted_fire.show()


if __name__ == '__main__':
    main()

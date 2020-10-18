"""
File: green_screen.py
-------------------------------
This file creates a new image that uses
MillenniumFalcon.png as background and
replace the green pixels in ReyGreenScreen.png
"""

from simpleimage import SimpleImage


def combine(background_img, figure_img):
    """
    :param background_img: (SimpleImage) the original image
    :param figure_img: (SimpleImage) the original image
    :return: The new image combine the figure and the background
    """
    for y in range(figure_img.height):
        for x in range(figure_img.width):
            new_pixel = figure_img.get_pixel(x, y)
            bigger = max(new_pixel.red, new_pixel.blue)  # to see which color info is bigger
            if new_pixel.green > bigger * 2:  # to see is green screen or not
                pixel_bg = background_img.get_pixel(x, y)
                new_pixel.red = pixel_bg.red
                new_pixel.blue = pixel_bg.blue
                new_pixel.green = pixel_bg.green
    return figure_img


def main():
    """
    This program combine two images, new new image keep the figure and replace the green screen with background image
    """
    space_ship = SimpleImage("images/MillenniumFalcon.png")
    figure = SimpleImage("images/ReyGreenScreen.png")
    result = combine(space_ship, figure)
    result.show()


if __name__ == '__main__':
    main()

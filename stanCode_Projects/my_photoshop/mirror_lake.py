"""
File: mirror_lake.py
----------------------------------
This file reads in mt-rainier.jpg and
makes a new image that creates a mirror
lake vibe by placing the inverse image of
mt-rainier.jpg below the original one
"""
from simpleimage import SimpleImage


def reflect(filename):
    """
    :param filename: str, the file path of the original image
    :return: original image at the upper side and mirror the original image at the bottom side
    """
    img = SimpleImage(filename)
    # create a blank canvas with double the height of the original image
    new_image = SimpleImage.blank(img.width, img.height * 2)
    #  the loops assign R B G color info to every pixels in the blank canvas
    for y in range(img.height):
        for x in range(img.width):
            img_pixel = img.get_pixel(x, y)
            pixel1 = new_image.get_pixel(x, y)  # the original image
            pixel2 = new_image.get_pixel(x, new_image.height - y - 1)  # the mirrored image
            pixel1.red = img_pixel.red
            pixel1.blue = img_pixel.blue
            pixel1.green = img_pixel.green
            pixel2.red = img_pixel.red
            pixel2.blue = img_pixel.blue
            pixel2.green = img_pixel.green
    return new_image


def main():
    """
    This program will create a blank canvas with double the size of the original image, then
    assign the original image at the upper side and mirror the original image at the bottom side.
    """
    original_mt = SimpleImage('images/mt-rainier.jpg')
    original_mt.show()
    reflected = reflect('images/mt-rainier.jpg')
    reflected.show()


if __name__ == '__main__':
    main()

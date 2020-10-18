"""
File: shrink.py
Name: TaoKe Chorng
-------------------------------
Create a new "out" image half the width and height of the original.
Set pixels at x=0 1 2 3 in out , from x=0 2 4 6 in original,
and likewise in the y direction.
"""

from simpleimage import SimpleImage


def shrink(filename):
    """
    :param filename: str, the file path of the original image
    :return img: the updated image with half the width and height of the original image
    """
    img = SimpleImage(filename)
    # create a blank  canvas with half the width and height of the original image
    new_image = SimpleImage.blank(img.width//2, img.height//2)
    for y in range(new_image.height):
        for x in range(new_image.width):
            # get color info from every 2 pixels from the original image
            img_pixel = img.get_pixel(x * 2, y * 2)
            pixel = new_image.get_pixel(x, y)
            pixel.red = img_pixel.red
            pixel.blue = img_pixel.blue
            pixel.green = img_pixel.green
    return new_image


def main():
    """
    This program shrink the original image with half the height and width
    """
    original = SimpleImage("images/poppy.png")
    original.show()
    after_shrink = shrink("images/poppy.png")
    after_shrink.show()


if __name__ == '__main__':
    main()

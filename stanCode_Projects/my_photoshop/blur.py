"""
File: blur.py
Name: TaoKe Chorng
-------------------------------
This file shows the original image first,
smiley-face.png, and then compare to its
blurred image. The blur algorithm uses the
average RGB values of a pixel's nearest neighbors
"""

from simpleimage import SimpleImage


def blur(img):
    """
    :param img: (SimpleImage) the original image
    :return: The updated image with blur result
    """
    new_image = SimpleImage.blank(img.width, img.height)  # create a new blank canvas
    for y in range(new_image.height):
        for x in range(new_image.width):
            new_pixel = new_image.get_pixel(x, y)  # (comment for TaoKe Chorng) get the 8 bit*3 info 0000000*3
            # blur four corner's pixels
            if x == 0 and y == 0:
                pixel = img.get_pixel(x, y)
                pixel6 = img.get_pixel(x + 1, y)
                pixel8 = img.get_pixel(x, y + 1)
                pixel9 = img.get_pixel(x + 1, y + 1)
                # (comment for TaoKe Chorng) adjust the 00000000 info
                new_pixel.red = (pixel.red + pixel6.red + pixel8.red + pixel9.red) / 4
                new_pixel.blue = (pixel.blue + pixel6.blue + pixel8.blue + pixel9.blue) / 4
                new_pixel.green = (pixel.green + pixel6.green + pixel8.green + pixel9.green) / 4
            elif x == img.width - 1 and y == 0:
                pixel4 = img.get_pixel(x - 1, y)
                pixel = img.get_pixel(x, y)
                pixel7 = img.get_pixel(x - 1, y + 1)
                pixel8 = img.get_pixel(x, y + 1)
                new_pixel.red = (pixel.red + pixel4.red + pixel8.red + pixel7.red) / 4
                new_pixel.blue = (pixel.blue + pixel4.blue + pixel8.blue + pixel7.blue) / 4
                new_pixel.green = (pixel.green + pixel4.green + pixel8.green + pixel7.green) / 4
            elif x == 0 and y == img.height - 1:
                pixel2 = img.get_pixel(x, y - 1)
                pixel3 = img.get_pixel(x + 1, y - 1)
                pixel = img.get_pixel(x, y)
                pixel6 = img.get_pixel(x + 1, y)
                new_pixel.red = (pixel2.red + pixel3.red + pixel.red + pixel6.red) / 4
                new_pixel.blue = (pixel.blue + pixel2.blue + pixel3.blue + pixel6.blue) / 4
                new_pixel.green = (pixel.green + pixel2.green + pixel3.green + pixel6.green) / 4
            elif x == img.width-1 and y == img.height-1:
                pixel1 = img.get_pixel(x - 1, y - 1)
                pixel2 = img.get_pixel(x, y - 1)
                pixel4 = img.get_pixel(x - 1, y)
                pixel = img.get_pixel(x, y)
                new_pixel.red = (pixel1.red + pixel2.red + pixel.red + pixel4.red) / 4
                new_pixel.blue = (pixel.blue + pixel2.blue + pixel1.blue + pixel4.blue) / 4
                new_pixel.green = (pixel.green + pixel2.green + pixel1.green + pixel4.green) / 4
            # blur the upper side
            elif y == 0 and img.width - 1 > x > 0:
                pixel4 = img.get_pixel(x - 1, y)
                pixel = img.get_pixel(x, y)
                pixel6 = img.get_pixel(x + 1, y)
                pixel7 = img.get_pixel(x - 1, y + 1)
                pixel8 = img.get_pixel(x, y + 1)
                pixel9 = img.get_pixel(x + 1, y + 1)
                new_pixel.red = (pixel4.red + pixel.red + pixel6.red + pixel7.red + pixel8.red + pixel9.red) / 6
                new_pixel.blue = (pixel4.blue + pixel.blue + pixel6.blue + pixel7.blue + pixel8.blue + pixel9.blue) / 6
                new_pixel.green = (pixel4.green + pixel.green + pixel6.green + pixel7.green + pixel8.green +
                                   pixel9.green) / 6
            # blur the right side pixels
            elif x == 0 and img.height - 1 > y > 0:
                pixel2 = img.get_pixel(x, y - 1)
                pixel3 = img.get_pixel(x + 1, y - 1)
                pixel = img.get_pixel(x, y)
                pixel6 = img.get_pixel(x + 1, y)
                pixel8 = img.get_pixel(x, y + 1)
                pixel9 = img.get_pixel(x + 1, y + 1)
                new_pixel.red = (pixel2.red + pixel3.red + pixel.red + pixel6.red + pixel8.red + pixel9.red) / 6
                new_pixel.blue = (pixel2.blue + pixel3.blue + pixel.blue + pixel6.blue + pixel8.blue + pixel9.blue) / 6
                new_pixel.green = (pixel2.green + pixel3.green + pixel.green + pixel6.green + pixel8.green +
                                   pixel9.green) / 6
            # blur the left side pixels
            elif x == img.width - 1 and img.height - 1 > y > 0:
                pixel1 = img.get_pixel(x - 1, y - 1)
                pixel2 = img.get_pixel(x, y - 1)
                pixel4 = img.get_pixel(x - 1, y)
                pixel = img.get_pixel(x, y)
                pixel7 = img.get_pixel(x - 1, y + 1)
                pixel8 = img.get_pixel(x, y + 1)
                new_pixel.red = (pixel1.red + pixel2.red + pixel4.red + pixel.red + pixel7.red + pixel8.red) / 6
                new_pixel.blue = (pixel1.blue + pixel2.blue + pixel4.blue + pixel.blue + pixel7.blue + pixel8.blue) / 6
                new_pixel.green = (pixel1.green + pixel2.green + pixel4.green + pixel.green + pixel7.green +
                                   pixel8.green) / 6
            # blur the bottom side pixels
            elif img.width - 1 > x > 0 and y == img.height - 1:
                pixel1 = img.get_pixel(x - 1, y - 1)
                pixel2 = img.get_pixel(x, y - 1)
                pixel3 = img.get_pixel(x + 1, y - 1)
                pixel4 = img.get_pixel(x - 1, y)
                pixel = img.get_pixel(x, y)
                pixel6 = img.get_pixel(x + 1, y)
                new_pixel.red = (pixel1.red + pixel2.red + pixel3.red + pixel4.red + pixel.red + pixel6.red) / 6
                new_pixel.blue = (pixel1.blue + pixel2.blue + pixel3.blue + pixel4.blue + pixel.blue + pixel6.blue) / 6
                new_pixel.green = (pixel1.green + pixel2.green + pixel3.green + pixel4.green + pixel.green +
                                   pixel6.green) / 6
            # blur the rest pixels
            else:
                pixel1 = img.get_pixel(x - 1, y - 1)
                pixel2 = img.get_pixel(x, y - 1)
                pixel3 = img.get_pixel(x + 1, y - 1)
                pixel4 = img.get_pixel(x - 1, y)
                pixel = img.get_pixel(x, y)
                pixel6 = img.get_pixel(x + 1, y)
                pixel7 = img.get_pixel(x - 1, y + 1)
                pixel8 = img.get_pixel(x, y + 1)
                pixel9 = img.get_pixel(x + 1, y + 1)
                new_pixel.red = (pixel1.red + pixel2.red + pixel3.red + pixel4.red + pixel.red + pixel6.red +
                                 pixel7.red + pixel8.red + pixel9.red) / 9
                new_pixel.blue = (pixel1.blue + pixel2.blue + pixel3.blue + pixel4.blue + pixel.blue + pixel6.blue +
                                  pixel7.blue + pixel8.blue + pixel9.blue) / 9
                new_pixel.green = (pixel1.green + pixel2.green + pixel3.green + pixel4.green + pixel.green + pixel6.green +
                                   pixel7.green + pixel8.green + pixel9.green) / 9
    return new_image


def main():
    """
    This program blur the original image with the blur function and
    """
    old_img = SimpleImage("images/smiley-face.png")
    old_img.show()
    blurred_img = blur(old_img)
    for i in range(10):
        blurred_img = blur(blurred_img)
    blurred_img.show()


if __name__ == '__main__':
    main()




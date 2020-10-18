"""
File: best_photoshop_award.py
Name: TAO KE CHORNG
----------------------------------
This file creates a photoshopped image
that is going to compete for the 2020 Best
Photoshop Award for SC101P.
Please put all the images you use in image_contest folder
and make sure to choose which award you are aiming at
"""
from simpleimage import SimpleImage

GREEN = 1.23  # to see the pixel is green screen or not
BLACK = 120  # to see the pixel is black hair or not


def making_masterpiece(figure_img, background_img):
    """
    This function replace the figure image's green area with the background
    :param figure_img: SimpleImage, green screen figure image
    :param background_img: SimpleImage, the background image
    :return: SimpleImage, figure image's green pixels replace with background image's pixels
    """
    for y in range(figure_img.height):
        for x in range(figure_img.width):
            pixel = figure_img.get_pixel(x, y)
            bigger = max(pixel.red, pixel.blue)
            total = pixel.red + pixel.blue + pixel.green
            if pixel.green > bigger * GREEN and total > BLACK:
                pixel_bg = background_img.get_pixel(x, y)
                pixel.red = pixel_bg.red
                pixel.blue = pixel_bg.blue
                pixel.green = pixel_bg.green
    return figure_img


def main():
    """
    This program combine two images to make the masterpiece
    """
    figure = SimpleImage("images/figure.jpg")
    background = SimpleImage("images/back.jpg")
    master_piece = making_masterpiece(figure, background)
    master_piece.show()


if __name__ == '__main__':
    main()

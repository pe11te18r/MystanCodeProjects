"""
File: mirror_lake.py
----------------------------------
This file reads in mt-rainier.jpg and
makes a new image that creates a mirror
lake vibe by placing an inverse image of
mt-rainier.jpg below the original one.
"""
from simpleimage import SimpleImage


def reflect(filename):
    """
    :param filename: str, the file path of the original image
    :return: SimpleImage, the image with the mirror one
    """
    img = SimpleImage(filename)
    blank = SimpleImage.blank(img.width, img.height * 2)
    for x in range(img.width):
        for y in range(img.height):
            pixel = img.get_pixel(x, y)
            blank1 = blank.get_pixel(x, y)
            blank2 = blank.get_pixel(x, (blank.height - 1 - y))
            blank1.red = blank2.red = pixel.red
            blank1.green = blank2.green = pixel.green
            blank1.blue = blank2.blue = pixel.blue
    return blank


def main():
    """
    TODO: Get the mirror image of the image
    """
    original_mt = SimpleImage('images/mt-rainier.jpg')
    original_mt.show()
    reflected = reflect('images/mt-rainier.jpg')
    reflected.show()


if __name__ == '__main__':
    main()

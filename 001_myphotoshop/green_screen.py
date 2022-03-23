"""
File: green_screen.py
-------------------------------
This file creates a new image that uses
MillenniumFalcon.png as background and
replace the green pixels in "ReyGreenScreen.png".
"""

from simpleimage import SimpleImage


def combine(background_img, figure_img):
    """
    :param background_img: SimpleImage, the image would replace the green screen
    :param figure_img: SimpleImage, the image of the figure and the green screen
    :return: SimpleImage, the combined image
    """
    background_img.make_as_big_as(figure_img)
    for x in range(figure_img.width):
        for y in range(figure_img.height):
            pixel_fig = figure_img.get_pixel(x, y)
            pixel_back = background_img.get_pixel(x, y)
            bigger = max(pixel_fig.red, pixel_fig.blue)
            if bigger * 2 < pixel_fig.green:  # 綠屏
                pixel_fig.red = pixel_back. red
                pixel_fig.green = pixel_back.green
                pixel_fig.blue = pixel_back.blue
    return figure_img


def main():
    """
    TODO: combine two image, replace the green screen with the background
    """
    space_ship = SimpleImage("images/MillenniumFalcon.png")
    figure = SimpleImage("images/ReyGreenScreen.png")
    result = combine(space_ship, figure)
    result.show()


if __name__ == '__main__':
    main()

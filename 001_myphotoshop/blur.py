"""
File: blur.py
Name: Peter Lin
-------------------------------
This file shows the original image first,
smiley-face.png, and then compare to its
blurred image. The blur algorithm uses the
average RGB values of a pixel's nearest neighbors.
"""

from simpleimage import SimpleImage


def blur(image):
    """
    :param image: SimpleImage, the raw image
    :return: SimpleImage, the blurred image
    """
    new_img = SimpleImage.blank(image.width, image.height)
    redsum = greensum = bluesum = 0
    for x in range(image.width):
        for y in range(image.height):
            new_pixel = new_img.get_pixel(x, y)
            w = image.width - 1
            h = image.height - 1
            num = 0
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if 0 <= (x + i) <= w and 0 <= (y + j) <= h:  # 設定邊界條件
                        pixel = image.get_pixel(x + i, y + j)
                        num += 1  # 如果超出邊界條件就不用計算
                        redsum += pixel.red
                        greensum += pixel.green
                        bluesum += pixel.blue
            new_pixel.red = redsum / num
            new_pixel.green = greensum / num
            new_pixel.blue = bluesum / num
            redsum = greensum = bluesum = 0
    return new_img


def main():
    """
    TODO: blur the image!
    """
    old_img = SimpleImage("images/smiley-face.png")
    old_img.show()

    blurred_img = blur(old_img)
    for i in range(5):
        blurred_img = blur(blurred_img)
    blurred_img.show()


# ---- DO NOT EDIT CODE BELOW THIS LINE ---- #

if __name__ == '__main__':
    main()

"""
File: shrink.py
-------------------------------
Create a new "out" image half the width and height of the original.
Set pixels at x=0 1 2 3 in out , from x=0 2 4 6 in original,
and likewise in the y direction.
"""

from simpleimage import SimpleImage


def shrink(filename):
    """
    :param filename: str, the file path of the original file
    :return img: SimpleImage, the shrinked picture
    Algorithm : 以1/2等比例縮小，所以用長寬各取2，以2*2 為一個單位做平均，成為新的像素RGB值
    """
    image = SimpleImage(filename)
    small = SimpleImage.blank(image.width // 2, image.height // 2)  # 用 floor division 來處理奇數長寬的問題
    for x in range(image.width // 2):
        for y in range(image.height // 2):
            sum_red = 0
            sum_green = 0
            sum_blue = 0
            new_pixel = small.get_pixel(x, y)
            for i in range(2):
                for j in range(2):
                    pixel = image.get_pixel(x * 2 + i, y * 2 + j)
                    sum_red += pixel.red
                    sum_green += pixel.green
                    sum_blue += pixel.blue
            new_pixel.red = sum_red / 4
            new_pixel.green = sum_green / 4
            new_pixel.blue = sum_blue / 4
    return small


def main():
    """
    TODO: shrink the image
    """
    original = SimpleImage("images/poppy.png")
    original.show()
    after_shrink = shrink("images/poppy.png")
    after_shrink.show()


if __name__ == '__main__':
    main()

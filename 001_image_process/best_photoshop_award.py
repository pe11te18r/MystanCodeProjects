"""
File: best_photoshop_award.py
----------------------------------
This file creates a photoshopped image
that is going to compete for the Best
Photoshop Award for SC001.
Please put all the images you will use in the image_contest folder
and make sure to choose the right folder when loading your images.
"""
from simpleimage import SimpleImage


def main():
    """
    IDEA: 這是一部由新海誠所編劇並執導的動畫電影，講述一個超能力少年與流浪女孩的故事。
          一股「讓天氣放晴」的力量，是多麽的奇幻！
    """
    fig = SimpleImage('image_contest/Peter.jpg')  # 1150 * 2496
    bg = SimpleImage('image_contest/sky.jpg')  # 570 * 763
    fig.make_as_big_as(bg)  # 570 * 763
    new_img = combine(fig, bg)
    new_img.show()


def combine(fig, bg):
    for x in range(fig.width):
        for y in range(fig.height):
            fig_pixel = fig.get_pixel(x, y)
            bg_pixel = bg.get_pixel(x, y)
            total = fig_pixel.red + fig_pixel.blue + fig_pixel.green
            if 200 < y < 500:
                if total < 559 and fig_pixel.red < 140:
                    bg_pixel.red = fig_pixel.red
                    bg_pixel.green = fig_pixel.green
                    bg_pixel.blue = fig_pixel.blue
    return bg


if __name__ == '__main__':
    main()

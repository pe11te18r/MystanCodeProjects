"""
File: DRAW LINE
Name: Peter Lin
-------------------------
TODO: print a hallow circle at the click of the odd number times, a line at the click of the even number times.
"""

from campy.graphics.gobjects import GOval, GLine
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked

SIZE = 5

# Global variation
window = GWindow()
circle = GOval(SIZE, SIZE)
count = 1
xi = 0
yi = 0


def main():
    """
    This program creates lines on an instance of GWindow class.
    There is a circle indicating the user’s first click. A line appears
    at the condition where the circle disappears as the user clicks
    on the canvas for the second time.
    """
    onmouseclicked(draw_line)


def draw_line(mouse):
    global count, xi, yi
    circle.color = 'black'
    if count % 2 == 1:  # at the odd number of times, print a hallow circle only
        window.add(circle, x=mouse.x, y=mouse.y)
        xi = circle.x  # definite the start of the line
        yi = circle.y
    else:  # ath the even number of times, replace the hallow circle with a line
        xf = mouse.x  # definite the end of the line
        yf = mouse.y
        line = GLine(xi, yi, xf, yf)
        window.remove(circle)
        window.add(line)
    count += 1


if __name__ == "__main__":
    main()

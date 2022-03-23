"""
File: bouncing ball
Name: Peter Lin
-------------------------
TODO: to make the ball bouncing
"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked

VX = 3
DELAY = 10
GRAVITY = 1
SIZE = 20
REDUCE = 0.9
START_X = 30
START_Y = 40
COUNT = 1

window = GWindow(800, 500, title='bouncing_ball.py')
ball = GOval(SIZE, SIZE, x=START_X, y=START_Y)


def main():
    """
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.
    """
    ball.filled = True
    ball.fill_color = 'black'
    window.add(ball)
    onmouseclicked(bounce)


def bounce(mouse):
    global COUNT
    vy = 0.2  # 向下為正，向上為負
    if ball.x == START_X and ball.y == START_Y and COUNT <= 3:  # if function is the switch of the onmouseclicked
        while True:
            ball.move(VX, vy)
            vy += GRAVITY
            if ball.y+SIZE >= window.height:  # change the direction and reduce the max of vy
                vy *= REDUCE
                vy = -vy
            pause(10)
            if ball.x+SIZE >= window.width:  # return back to the initial condition
                ball.x = START_X
                ball.y = START_Y
                COUNT += 1
                break


if __name__ == "__main__":
    main()

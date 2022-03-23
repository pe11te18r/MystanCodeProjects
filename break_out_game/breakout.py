"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

YOUR DESCRIPTION HERE
"""

from campy.gui.events.timer import pause
from campy.graphics.gobjects import GLabel
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 1000 / 120  # 120 frames per second
NUM_LIVES = 3  # Number of attempts


def main():
    graphics = BreakoutGraphics()
    lives = NUM_LIVES

    # Add the animation loop here!
    while True:
        pause(FRAME_RATE)
        if graphics.ball_lost():
            lives -= 1
            if lives > 0:
                graphics.reset_ball()
            else:
                label = GLabel('GAME OVER !!!', x=graphics.window_width * 0.02, y=graphics.window_height * 0.6)
                label.font = 'Helvetica-60-Bold'
                label.color = 'chocolate'
                graphics.window.add(label)
                break
        if graphics.mission_completed():
            break
        graphics.detect_object()
        if graphics.ball.x <= 0 or graphics.ball.x + graphics.ball_radius * 2 > graphics.window_width:
            graphics.ball_x_rebound()
        if graphics.ball.y <= 0:
            graphics.ball_y_rebound()
        graphics.ball.move(graphics.get_dx(), graphics.get_dy())


if __name__ == '__main__':
    main()

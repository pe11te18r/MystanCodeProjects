"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao.

YOUR DESCRIPTION HERE     待處理：每個brick要有自己的名字:用list的方式存取所有brick的資料,打到短邊追撞？
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5  # Space between bricks (in pixels). This space is used for horizontal and vertical spacing
BRICK_WIDTH = 40  # Height of a brick (in pixels)
BRICK_HEIGHT = 15  # Height of a brick (in pixels)
BRICK_ROWS = 10  # Number of rows of bricks
BRICK_COLS = 10  # Number of columns of bricks
BRICK_OFFSET = 50  # Vertical offset of the topmost brick from the window top (in pixels)
BALL_RADIUS = 10  # Radius of the ball (in pixels)
PADDLE_WIDTH = 75  # Width of the paddle (in pixels)
PADDLE_HEIGHT = 15  # Height of the paddle (in pixels)
PADDLE_OFFSET = 50  # Vertical offset of the paddle from the window bottom (in pixels)
INITIAL_Y_SPEED = 7  # Initial vertical speed for the ball
MAX_X_SPEED = 5  # Maximum initial horizontal speed for the ball


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH, paddle_height=PADDLE_HEIGHT,
                 paddle_offset=PADDLE_OFFSET, brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS, brick_width=BRICK_WIDTH,
                 brick_height=BRICK_HEIGHT, brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING, title='Breakout'):

        # Create a graphical window, with some extra space
        self.window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        self.window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=self.window_width, height=self.window_height, title=title)

        # Create a paddle
        self.paddle = GRect(paddle_width, paddle_height,
                            x=(self.window_width - paddle_width) / 2, y=self.window_height - paddle_offset)
        self.paddle_offset = paddle_offset
        self.paddle_width = paddle_width
        self.paddle.filled = True
        self.window.add(self.paddle)

        # Center a filled ball in the graphical window
        self.ball = GOval(ball_radius * 2, ball_radius * 2,
                          x=self.window_width / 2 - ball_radius, y=self.window_height / 2 - ball_radius)
        self.ball.filled = True
        self.ball_radius = ball_radius
        self.window.add(self.ball)

        # Default initial velocity for the ball
        self.__dx = 0
        self.__dy = 0

        # Initialize our mouse listeners
        onmouseclicked(self.handle_click)
        onmousemoved(self.paddle_move)

        # Draw bricks
        for i in range(brick_cols):
            for j in range(brick_rows):
                self.brick = GRect(brick_width, brick_height,
                                   x=(brick_width + brick_spacing) * i,
                                   y=(brick_height + brick_spacing) * j + brick_offset)
                self.brick.filled = True
                if j < 2:
                    self.brick.color = 'red'
                    self.brick.fill_color = 'red'
                elif 2 <= j < 4:
                    self.brick.color = 'orange'
                    self.brick.fill_color = 'orange'
                elif 4 <= j < 6:
                    self.brick.color = 'yellow'
                    self.brick.fill_color = 'yellow'
                elif 6 <= j < 8:
                    self.brick.color = 'green'
                    self.brick.fill_color = 'green'
                else:
                    self.brick.color = 'blue'
                    self.brick.fill_color = 'blue'
                self.window.add(self.brick)

        # Default the counter
        self.brick_account = brick_cols * brick_rows
        self.remove_account = 0

    def paddle_move(self, mickey):
        paddle_x = mickey.x - self.paddle_width / 2
        if paddle_x < 0:
            paddle_x = 0
        elif paddle_x > self.window_width - self.paddle_width:
            paddle_x = self.window_width - self.paddle_width
        self.window.add(self.paddle, x=paddle_x, y=self.window_height - self.paddle_offset)

    def handle_click(self, trigger):
        if self.ball.x == self.window_width / 2 - self.ball_radius and self.ball.y == self.window_height / 2 - self.ball_radius:
            if self.__dx == self.__dy == 0:
                self.ball_velocity()

    def ball_velocity(self):
        self.__dx = random.randint(0, MAX_X_SPEED)
        self.__dy = INITIAL_Y_SPEED
        if random.random() > 0.5:
            self.__dx = -self.__dx

    def get_dx(self):
        return self.__dx

    def get_dy(self):
        return self.__dy

    def ball_lost(self):
        is_ball_lost = self.ball.y > self.window_height
        return is_ball_lost

    def reset_ball(self):
        self.ball.x = self.window_width / 2 - self.ball_radius
        self.ball.y = self.window_height / 2 - self.ball_radius
        self.__dx = self.__dy = 0

    def ball_x_rebound(self):
        self.__dx = -self.__dx

    def ball_y_rebound(self):
        self.__dy = -self.__dy

    def detect_object(self):
        detector1 = self.window.get_object_at(self.ball.x, self.ball.y)
        detector2 = self.window.get_object_at(self.ball.x + self.ball_radius * 2, self.ball.y)
        detector3 = self.window.get_object_at(self.ball.x, self.ball.y + self.ball_radius * 2)
        detector4 = self.window.get_object_at(self.ball.x + self.ball_radius * 2, self.ball.y + self.ball_radius * 2)
        if detector1 is not None:
            if detector1 is not self.paddle:
                self.ball_y_rebound()
                self.window.remove(detector1)
                self.remove_account += 1
        elif detector2 is not None:
            if detector2 is not self.paddle:
                self.ball_y_rebound()
                self.window.remove(detector2)
                self.remove_account += 1
        elif detector3 is not None:
            if detector3 is self.paddle:
                if self.__dy > 0:
                    self.ball_y_rebound()
            else:
                self.ball_y_rebound()
                self.window.remove(detector3)
                self.remove_account += 1
        elif detector4 is not None:
            if detector4 is self.paddle:
                if self.__dy > 0:
                    self.ball_y_rebound()  # paddle有厚度：如果今天球碰到paddle，確保他是往下墜落在彈，如果是網上就不再彈，用if / elif
            else:
                self.ball_y_rebound()
                self.window.remove(detector4)
                self.remove_account += 1

    def mission_completed(self):
        is_mission_completed = self.remove_account == self.brick_account
        return is_mission_completed

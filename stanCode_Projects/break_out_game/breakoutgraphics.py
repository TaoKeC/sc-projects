"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao

YOUR DESCRIPTION HERE
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random
from campy.gui.events.timer import pause

BRICK_SPACING = 5  # Space between bricks (in pixels). This space is used for horizontal and vertical spacing.
BRICK_WIDTH = 40  # Height of a brick (in pixels).
BRICK_HEIGHT = 15  # Height of a brick (in pixels).
BRICK_ROWS = 10  # Number of rows of bricks.
BRICK_COLS = 10  # Number of columns of bricks.
BRICK_OFFSET = 50  # Vertical offset of the topmost brick from the window top (in pixels).
BALL_RADIUS = 10  # Radius of the ball (in pixels).
PADDLE_WIDTH = 75  # Width of the paddle (in pixels).
PADDLE_HEIGHT = 15  # Height of the paddle (in pixels).
PADDLE_OFFSET = 50  # Vertical offset of the paddle from the window bottom (in pixels).

INITIAL_Y_SPEED = 7.0  # Initial vertical speed for the ball.
MAX_X_SPEED = 5  # Maximum initial horizontal speed for the ball.

NUM_LIVES = 3
FRAME_RATE = 1000 / 120


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH,
                 paddle_height=PADDLE_HEIGHT, paddle_offset=PADDLE_OFFSET,
                 brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS,
                 brick_width=BRICK_WIDTH, brick_height=BRICK_HEIGHT,
                 brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING,
                 title='Breakout'):
        # Create a graphical window, with some extra space.
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)

        # Create a paddle.
        self.paddle = GRect(width=paddle_width, height=paddle_height)
        self.paddle.filled = True
        self.window.add(self.paddle, x=(window_width - self.paddle.width) / 2, y=window_height - paddle_offset)
        # Center a filled ball in the graphical window.
        self.ball = GOval(width=ball_radius * 2, height=ball_radius * 2)
        self.ball.filled = True
        self.window.add(self.ball, x=(window_width - self.ball.width) / 2, y=(window_height - self.ball.height) / 2)
        # Default initial velocity for the ball.
        self.__dx = random.randint(1, MAX_X_SPEED)
        if random.random() > 0.5:
            self.__dx = -self.__dx
        self.__dy = INITIAL_Y_SPEED
        # Initialize our mouse listeners.
        onmouseclicked(self.leave_original)
        onmousemoved(self.paddle_move)
        # Draw bricks.
        position_x = 0 - brick_width - brick_spacing
        position_y = brick_offset
        for i in range(brick_cols):
            for j in range(brick_rows):
                position_x += brick_width + brick_spacing
                self.bricks = GRect(width=BRICK_WIDTH, height=BRICK_HEIGHT)
                if i <= 1:
                    self.bricks.color = 'red'
                    self.bricks.filled = True
                    self.bricks.fill_color = 'red'
                elif 1 < i <= 3:
                    self.bricks.color = 'orange'
                    self.bricks.filled = True
                    self.bricks.fill_color = 'orange'
                elif 3 < i <= 5:
                    self.bricks.color = 'yellow'
                    self.bricks.filled = True
                    self.bricks.fill_color = 'yellow'
                elif 5 < i <= 7:
                    self.bricks.color = 'green'
                    self.bricks.filled = True
                    self.bricks.fill_color = 'green'
                else:
                    self.bricks.color = 'blue'
                    self.bricks.filled = True
                    self.bricks.fill_color = 'blue'
                self.window.add(self.bricks, x=position_x, y=position_y)
            position_y += (brick_height + brick_spacing)
            position_x = 0 - brick_width - brick_spacing
        # lives
        self.lives = NUM_LIVES
        self.live_label = GLabel(f'lives: {self.lives}')
        self.window.add(self.live_label, x=0, y=self.window.height - self.live_label.height)
        # Win/Lose labels
        self.loss_label = GLabel('You lose')
        self.win_label = GLabel('You win!')
        # Counter (count for how many bricks are break)
        self.close_counter = brick_rows * brick_cols
        self.counter = 0
        # Close condition
        self.close = False

    def check_for_collisions(self):
        # four vertex of the ball
        self.vertex1 = self.window.get_object_at(self.ball.x, self.ball.y)
        self.vertex2 = self.window.get_object_at(self.ball.x + self.ball.width, self.ball.y)
        self.vertex3 = self.window.get_object_at(self.ball.x, self.ball.y + self.ball.height)
        self.vertex4 = self.window.get_object_at(self.ball.x + self.ball.width, self.ball.y + self.ball.height)

        # the see the ball meet bricks or not
        self.maybe_brick1 = self.vertex1
        self.maybe_brick2 = self.vertex2

        if self.maybe_brick1 is not None and self.maybe_brick1 is not self.paddle and self.maybe_brick1 \
                is not self.live_label:
            # the following content will execute, if the ball meet a brick
            self.window.remove(self.vertex1)
            self.__dy = - self.__dy
            self.counter += 1
        elif self.maybe_brick2 is not None and self.maybe_brick2 is not self.paddle and self.maybe_brick2 \
                is not self.live_label:
            # the following content will execute, if the ball meet a brick
            self.window.remove(self.vertex2)
            self.__dy = - self.__dy
            self.counter += 1
        elif self.vertex3 == self.paddle:
            # the following content will execute, if the ball meet the paddle
            if self.__dy > 0:
                self.__dy = - self.__dy
        elif self.vertex4 == self.paddle:
            # the following content will execute, if the ball meet the paddle
            if self.__dy > 0:
                self.__dy = - self.__dy

    def leave_original(self, event):
        # when user click the mouse, this function will execute
        if self.ball.x == (self.window.width - self.ball.width) / 2 and \
                self.ball.y == (self.window.height - self.ball.height) / 2:
            self.ball_move()

    def paddle_move(self, event):
        # when user move the mouse, this function will execute
        self.paddle.x = event.x - self.paddle.width / 2
        if self.paddle.x <= 0:
            self.paddle.x = 0
        if self.paddle.x >= self.window.width - self.paddle.width:
            self.paddle.x = self.window.width - self.paddle.width

    def ball_move(self):
        self.ball.move(self.__dx, self.__dy)

    def meet_wall(self):
        # when the ball meet a ball, it will bounce
        if self.ball.x <= 0 or self.ball.x >= self.window.width - self.ball.width:
            self.__dx = - self.__dx
        if self.ball.y <= 0:
            self.__dy = - self.__dy

    def dead(self):
        # when the ball out of range
        if self.ball.y >= self.window.height - self.ball.height:
            self.lives -= 1
            self.live_label.text = f'lives: {self.lives}'
            self.window.add(self.ball, x=(self.window.width - self.ball.width) / 2,
                            y=(self.window.height - self.ball.height) / 2)

    def loss(self):
        # user out of range three times
        if self.lives <= 0:
            self.window.clear()
            self.window.add(self.loss_label, x=(self.window.width - self.loss_label.width) / 2,
                            y=(self.window.height - self.loss_label.height) / 2)
            self.close = True

    def win(self):
        # user break all bricks
        if self.counter == self.close_counter:
            self.window.clear()
            self.window.add(self.win_label, x=(self.window.width - self.loss_label.width) / 2,
                            y=(self.window.height - self.loss_label.height) / 2)
            self.close = True

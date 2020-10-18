"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao

YOUR DESCRIPTION HERE
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 1000 / 120  # 120 frames per second.
NUM_LIVES = 3


def main():
    """
    This program is a break out game, user can break all the bricks to win or lose three lives
    to lose.
    """
    graphics = BreakoutGraphics()  # elements of the game
    # Add animation loop here!
    while True:
        if graphics.lives > 0:
            if graphics.ball.x != (graphics.window.width - graphics.ball.width) / 2 \
                    or graphics.ball.y != (graphics.window.height - graphics.ball.height) / 2:
                # the upper if condition is to see the user click the mouse or not(if the user click the mouse, the ball
                # will leave it's original position), if the user click the mouse the game will start.
                graphics.ball_move()
                if graphics.ball.x == (graphics.window.width - graphics.ball.width) / 2 \
                        or graphics.ball.y == (graphics.window.height - graphics.ball.height) / 2:
                    graphics.ball_move()
                    # if the ball pass it's original position, it will stop(this if condition is to prevent it).
                graphics.meet_wall()
                graphics.check_for_collisions()
                graphics.dead()
                graphics.loss()
                graphics.win()
                pause(FRAME_RATE)
                if graphics.close:  # end of the game
                    break
            else:
                pause(FRAME_RATE)


if __name__ == '__main__':
    main()

"""
File: sierpinski.py
Name: Tao Ke Chorng
---------------------------
This file recursively prints the Sierpinski triangle on GWindow.
The Sierpinski triangle is a fractal described in 1915 by Waclaw Sierpinski.
It is a self similar structure that occurs at different levels of iterations.
"""

from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GLine
from campy.gui.events.timer import pause

# Constants
ORDER = 3                  # Controls the order of Sierpinski Triangle
LENGTH = 600               # The length of order 1 Sierpinski Triangle
UPPER_LEFT_X = 150		   # The upper left x coordinate of order 1 Sierpinski Triangle
UPPER_LEFT_Y = 100         # The upper left y coordinate of order 1 Sierpinski Triangle
WINDOW_WIDTH = 950         # The width of the GWindow
WINDOW_HEIGHT = 700        # The height of the GWindow

# Global Variable
window = GWindow(width=WINDOW_WIDTH, height=WINDOW_HEIGHT)  # The canvas to draw Sierpinski Triangle


def main():
	"""
	TODO: draw subdivided triangles recursively into smaller equilateral triangles
	"""
	sierpinski_triangle(ORDER, LENGTH, UPPER_LEFT_X, UPPER_LEFT_Y)


def sierpinski_triangle(order, length, upper_left_x, upper_left_y):
	"""
	:param order: order of Sierpinski Triangle
	:param length: length of Sierpinski Triangle in the specific order
	:param upper_left_x: upper left x coordinate of Sierpinski Triangle in the specific order
	:param upper_left_y: upper right x coordinate of Sierpinski Triangle in the specific order
	:return: None
	"""
	if order == 0:
		return
	else:
		w = length * 0.5  # half of a side length of a tri
		h = length * 0.866  # height of a tri
		# left tri: t1, right tri: t2, middle tri: t3
		t1 = GLine(upper_left_x, upper_left_y, upper_left_x + length, upper_left_y)
		t2 = GLine(upper_left_x, upper_left_y, upper_left_x + w, upper_left_y + h)
		t3 = GLine(upper_left_x + length, upper_left_y, upper_left_x + w, upper_left_y + h)
		window.add(t1)
		window.add(t2)
		window.add(t3)
		# for left tri
		sierpinski_triangle(order - 1, length / 2, upper_left_x, upper_left_y)
		# for right tri
		sierpinski_triangle(order - 1, length / 2, upper_left_x + (length / 2), upper_left_y)
		# for middle tri
		sierpinski_triangle(order - 1, length / 2, upper_left_x + w / 2, upper_left_y + h / 2)


if __name__ == '__main__':
	main()
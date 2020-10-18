"""
File: quadratic_solver.py
Name: Tao-Ke Chorng
-----------------------
This program should implement a console program
that asks 3 inputs (a, b, and c)
from users to compute the roots of equation
ax^2 + bx + c = 0
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""

import math



def main():
	"""
	The program help user to find out roots of a quadratic function
	"""
	print("stanCode Quadratic Solver!")
	# Ask user to enter three integers
	a = int(input("Enter a: "))
	b = int(input("Enter b: "))
	c = int(input("Enter c: "))
	discriminant = b ** 2 - 4 * a * c
	# Use discriminant method to find out the combination of numbers can have 1, 2 or no real roots.
	if discriminant < 0:
		print("No real roots.")
	if discriminant > 0:
		x1 = (-b + math.sqrt(discriminant)) / 2 * a
		x2 = (-b - math.sqrt(discriminant)) / 2 * a
		print("Two roots: "+str(x1)+", "+str(x2))
	if discriminant == 0:
		x1 = (-b + math.sqrt(discriminant)) / 2 * a
		x2 = (-b - math.sqrt(discriminant)) / 2 * a
		print("one root: "+str(x1))



###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
	main()

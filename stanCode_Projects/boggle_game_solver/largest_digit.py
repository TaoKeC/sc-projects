"""
File: largest_digit.py
Name: Tao Ke Chorng
----------------------------------
This file recursively prints the biggest digit in
5 different integers, 12345, 281, 6, -111, -9453
If your implementation is correct, you should see
5, 8, 6, 1, 9 on Console.
"""
counter = 0
counter_2 = 10
biggest = 0
layer = 0


def main():
	print(find_largest_digit(12345))	  # 5
	print(find_largest_digit(281))        # 8
	print(find_largest_digit(6))          # 6
	print(find_largest_digit(-111))       # 1
	print(find_largest_digit(-9453))      # 9


def find_largest_digit(n):
	"""
	:param n: the input integer that will found the biggest digit
	:return: biggest digit in the integer
	"""
	global counter, biggest, counter_2, layer
	layer += 1
	if 1 > n > -1:
		# base case, the see the number is the biggest or not
		helper = biggest  # helper help to return the biggest digit
		biggest = 0
		return helper
	else:
		# the recursive condition will find how big is the number in digit position, if digit equal to 0,
		# the recursive condition will divide the hole integer by 10 to then do the recursive condition recursively,
		# and finally hit the base case
		if n >= 0:
			n -= 1
			counter += 1
			if n % counter_2 == 0:
				n /= counter_2
				if counter > biggest:
					biggest = counter
				counter = 0
			return find_largest_digit(n)
		else:
			# if the input integer less than 0
			n = - n
			n -= 1
			counter += 1
			if n % counter_2 == 0:
				n /= counter_2
				if counter > biggest:
					biggest = counter
				counter = 0
			return find_largest_digit(n)


if __name__ == '__main__':
	main()

"""
File: boggle.py
Name: Tao Ke Chorng
----------------------------------------
TODO:
"""

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'
word = []
alpha = 'qwertyuioplkjhgfdsaxzcvbnm'
counter = 1
row_of_letter = []
num_of_words = 0
printed_words = []  # store already printed words


def main():
	"""
	TODO: This program ask user input 16 alphabets in a specific way, then it will play the boggle game and
	print out all matches.
	"""
	global counter
	read_dictionary()
	count = 1
	# the while loop ask user to in put 4 rows of letters, and see it's legal or not
	while True:
		row = input(f'{counter} row of letters: ')
		row = row.lower()
		if len(row) >= 7:
			if row[0] in alpha and row[2] in alpha and row[4] in alpha and row[6] in alpha:
				if row[1] == ' ' and row[3] == ' ' and row[5] == ' ':
					counter += 1
					for j in range(len(row)):
						if j % 2 == 0:
							row_of_letter.append(row[j])
					count += 1
					if count > 4:
						break
				else:
					print('Illegal input')
			else:
				print('Illegal input')
		else:
			print('Illegal input')
	row1 = row_of_letter[:4]
	row2 = row_of_letter[4:8]
	row3 = row_of_letter[8:12]
	row4 = row_of_letter[12:16]
	board = [row1, row2, row3, row4]
	# these two loops will loop over every start position to find a word
	for y in range(4):
		for x in range(4):
			maybe_word = board[x][y]  # the start position to find a word
			find_word(board, x, y, maybe_word, [(x, y)])
	print(f'There are {num_of_words} words in total.')


def find_word(board, x, y, maybe_word, index_lst):
	"""
	:param board: a list that store all four rows
	:param x: the x position of a alphabet
	:param y: the y position of a alphabet
	:param maybe_word: to see the combination of alphabet is in dictionary or not
	:param index_lst: the index position of a alphabet
	:return: None
	"""
	global num_of_words
	if maybe_word in word and len(maybe_word) >= 4:
		if maybe_word not in printed_words:
			printed_words.append(maybe_word)
			print(f'Found \"{maybe_word}\"')
			num_of_words += 1
	if has_prefix(maybe_word):
		for i in range(-1, 2):
			for j in range(-1, 2):
				if 0 <= x + i < 4 and 0 <= y + j < 4:
					if (x + i, y + j) not in index_lst:
						# choose
						index_lst.append((x + i, y + j))
						maybe_word += board[x + i][y + j]
						#  Explore
						find_word(board, x + i, y + j, maybe_word, index_lst)
						#  un-choose
						maybe_word = maybe_word[:len(maybe_word)-1]
						index_lst.pop()


def read_dictionary():
	"""
	This function reads file "dictionary.txt" stored in FILE
	and appends words in each line into a Python list
	"""
	with open(FILE, 'r') as f:
		for line in f:
			word.append(line.strip())


def has_prefix(sub_s):
	"""
	:param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
	:return: (bool) If there is any words with prefix stored in sub_s
	"""
	for ch in word:
		if ch.startswith(sub_s):
			return ch.startswith(sub_s)


if __name__ == '__main__':
	main()

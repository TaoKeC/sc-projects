"""
File: anagram.py
Name: Tao Ke Chorng
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""

# Constants
FILE = 'dictionary.txt'       # This is the filename of an English dictionary
EXIT = '-1'                   # Controls when to stop the loop
word = []                     # list for words in the dictionary
find = []                     # list for the anagrams
counter = 0


def main():
    read_dictionary()
    print('Welcome to stanCode \"Anagram Generator\" (or -1 to quit)')
    while True:
        user_input = input('Find anagram for: ')
        user_input = user_input.lower()
        if user_input == EXIT:
            break
        find_anagrams(user_input)


def read_dictionary():
    with open(FILE, 'r') as f:
        for line in f:
            word.append(line.strip())


def find_anagrams(s):
    """
    :param s: user input
    :return: None
    """
    print('Searching...')
    find_anagrams_helper(s, '', len(s), find, [])
    print(f'{len(find)} anagrams: {find}')


def find_anagrams_helper(s, current_word, length, lst, index):
    global counter
    if len(current_word) == length and current_word in word:
        if current_word not in lst:
            lst.append(current_word)
            print(f'Found: {current_word}')
            print('Searching...')
            counter += 1
    else:
        for i in range(len(s)):
            if i not in index:  # using index to see the word in the specific position is append or not
                # choose
                current_word += s[i]
                index.append(i)
                # explore
                if has_prefix(current_word):
                    find_anagrams_helper(s, current_word, length, lst, index)
                # un-choose
                current_word = current_word[:-1]
                index.pop()


def has_prefix(sub_s):
    """
    :param sub_s: the un-check combination
    :return: the combination is in the dictionary or not
    """
    for ch in word:
        if ch.startswith(sub_s):
            return ch.startswith(sub_s)


if __name__ == '__main__':
    main()

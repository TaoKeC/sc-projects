"""
File: complement.py
Name: Douglas Chorng
----------------------------
This program uses string manipulation to
tackle a real world problem - finding the
complement strand of a DNA sequence.
THe program asks uses for a DNA sequence as
a python string that is case-insensitive.
Your job is to output the complement of it.
"""


def main():
    """
    The program will convert the DNA strand (user input) into certain paired nucleic acid
    """
    c = input('Please give me a DNA strand and I\'ll find the complement: ')
    # ask user enter a list of DNA strand combine with 'A','T','G','C','a','t','g','c'
    build_complement(c)


def build_complement(c):
    """
    The function convert alphabets in input c into certain alphabets.
    :param c: str, can be 'A','T','G','C','a','t','g','c'
    :return: The string of converted alphabets.
    """
    c = c.upper()  # The Str Class method changes input c into capital.
    total = ''
    for i in range(len(c)):
        # Using for loop to convert the input alphabet from index 0 to the last index
        # to certain alphabet, A to T, C to G vice versa.
        ans = ''
        if c[i] == 'A':
            ans += 'T'
        if c[i] == 'T':
            ans += 'A'
        if c[i] == 'C':
            ans += 'G'
        if c[i] == 'G':
            ans += 'C'
        total += ans
    print('The complement of', c, 'is', total)
    return total






###### DO NOT EDIT CODE BELOW THIS LINE ######
if __name__ == '__main__':
    main()

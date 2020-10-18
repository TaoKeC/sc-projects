"""
File: similarity.py
Name: Douglas Chorng
----------------------------
This program compares short dna sequence, s2,
with sub sequences of a long dna sequence, s1
The way of approaching this task is the same as
what people are doing in the bio industry.
"""


def main():
    """
    The program compare long DNA and short DNA and find out the highest
    match rate sequence between two DNA.
    """
    dna_long = input("Please give me a DNA sequence to search: ")
    # ask user enter a list of DNA strand combine with 'A','T','G','C','a','t','g','c'
    long = dna_long.upper()  # convert input dna_long into capital
    dna_short = input("What DNA sequence would you like to match? ")
    # ask user enter a list of DNA strand combine with 'A','T','G','C','a','t','g','c'
    short = dna_short.upper()  # convert input dna_short into capital
    homology(long, short)


def homology(long, short):
    """
    The function compare each alphabet between two variables, then find out
    the highest match rate sequence and print it out.
    :param long: str, the long DNA to be compared, combine with 'A','T','G','C'
    :param short: str, the short DNa to be compared, combine with 'A','T','G','C'
    :return: the highest match rate sequence
    """
    total = 0
    start_place = 0  # The position of where the short string will start to compare
    for j in range(len(long)-len(short)+1):
        # the j loop represent how many times two strings will compare.
        ans = ''
        counter = 0
        for k in range(len(short)):
            # the k loop represent for how many alphabets two strings will compare
            compare1 = long[k + start_place]
            compare2 = short[k]
            if compare1 == compare2:
                counter += 1
            else:
                pass
            ans += long[k + start_place]
        num = counter
        # the num variable represent the match rate of two strings in
        # the sequence
        if num > total:
            # the if condition will find out which sequence have the highest match rate
            total = num
            print_ans = ans
        start_place += 1
    print('The best match is', print_ans)
    return print_ans


###### DO NOT EDIT CODE BELOW THIS LINE ######
if __name__ == '__main__':
    main()

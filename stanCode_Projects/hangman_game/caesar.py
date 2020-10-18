"""
File: caesar.py
Name: Douglas Chorng
------------------------------
This program demonstrates the idea of caesar cipher.
Users will be asked to input a number to produce shifted
ALPHABET as the cipher table. After that, any strings typed
in will be encrypted.
"""


# This constant shows the original order of alphabetic sequence
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def main():
    """
    The program will ask user input a secret number and ciphered string and give back
    a deciphered string
    """
    num = int(input("Secret number: "))
    # num represent how many time the constant ALPHABET shift
    string = input("What\'s the ciphered string? ")
    # the sting that will be decipher later
    string = string.upper()  # convert string into capital
    deciphered(string, num)


def deciphered(string, num):
    """
    The function will help user shift the ALPHABET 'num'(user input) times
    and decipher the user input(string)
    :param string: str, user input, ciphered code
    :param num: int, user input, the time constant ALPHABET will shift
    :return: deciphered code/ string
    """
    old_alpha = ''
    for j in range(0, len(ALPHABET) - num):
        old_alpha += ALPHABET[j]
    shift_alpha = ''
    for i in range(len(ALPHABET)-num, len(ALPHABET)):
        shift_alpha += ALPHABET[i]
    new_alpha = shift_alpha + old_alpha
    # the variable new_alpha combine the original part(old_alpha) and the shifted part(shift_alpha)
    # and make them into a new alphabet combination to decipher the ciphered code
    ans = ''
    for k in range(len(string)):
        # using the k for loop to correspond the ciphered string to the ALPHABET
        # to decipher the ciphered string
        s = new_alpha.find(string[k])
        if s == -1:
            ans += string[k]
        else:
            ans += ALPHABET[s]
    print('The deciphered sting is:', ans)
    return ans

#####  DO NOT EDIT THE CODE BELOW THIS LINE  #####
if __name__ == '__main__':
    main()

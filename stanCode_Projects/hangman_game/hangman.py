"""
File: hangman.py
Name: Douglas Chorng
-----------------------------
This program plays hangman game.
Users sees a dashed word, trying to
correctly figure the un-dashed word out
by inputting one character each round.
If the user input is correct, show the
updated word on console. Players have N_TURNS
to try in order to win this game.
"""

import random

# This constant controls the number of guess the player has
N_TURNS = 7


def main():
    """
    The program is a hangman game, it is going to see the user
    can guess the word in certain times or not.
    """
    hangman()


def hangman():
    word = random_word()
    length = len(word)
    con = ''
    counter = N_TURNS
    for i in range(length):
        con += '-'  # con is the original look of the word
    print('The word looks like: ' + con)
    while True:  # start the to guess the word
        print('You have', counter, 'guesses left.')
        guess = input('Your guess: ')
        guess = guess.upper()
        string1 = ''
        for k in range(length):
            # k loop check your guess is True or False
            if guess == word[k]:
                string1 += guess
                print('You are correct!')
            else:
                string1 += con[k]
        if string1 == con:
            print('There is no', guess + '\'s', 'in the world.')
            counter -= 1
            if counter == 0:
                # this if condition will execute if you guess wrong more than 7 times
                print('You are completely hung : ( ')
                print('The word was:', word)
                break
        con = string1
        if con == word:
            # this if condition will execute if you guess the word right in
            # less than 7 times wrong
            print('You win!!')
            print('The word was:', word)
            break
        print('Your word looks like:', con)
    return con


def random_word():
    num = random.choice(range(9))
    if num == 0:
        return "NOTORIOUS"
    elif num == 1:
        return "GLAMOROUS"
    elif num == 2:
        return "CAUTIOUS"
    elif num == 3:
        return "DEMOCRACY"
    elif num == 4:
        return "BOYCOTT"
    elif num == 5:
        return "ENTHUSIASTIC"
    elif num == 6:
        return "HOSPITALITY"
    elif num == 7:
        return "BUNDLE"
    elif num == 8:
        return "REFUND"


#####  DO NOT EDIT THE CODE BELOW THIS LINE  #####
if __name__ == '__main__':
    main()

"""
File: rocket.py
Name: Douglas Chorng
-----------------------
This program should implement a console program
that draws ASCII art - a rocket.
The size of rocket is determined by a constant
defined as SIZE at top of the file.
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""
SIZE = 3  # The constant define the size of the rocket


def main():
    """
    The program will print a rocket by using four different functions.
    """
    head()
    belt()
    upper()
    lower()
    belt()
    head()


def head():
    """
    The function print out the head & bottom of the rocket
    """
    for i in range(SIZE):
        for j in range(SIZE - i):
            print(" ", end="")
        for k in range(i + 1):
            print("/", end="")
        for s in range(i + 1):
            print("\\", end="")
        print('')


def belt():
    """
    The function print out upper and lower belt of the rocket
    """
    for i in range(SIZE * 2 + 2):
        if i == 0:
            print("+", end="")
        elif i == SIZE * 2 + 2 - 1:
            print("+", end="")
        else:
            print("=", end="")
    print("")


def upper():
    """
    The function print out the rocket's upper body.
    """
    for i in range(SIZE):
        for j in range(1):
            print("|", end="")
        for k in range(1, SIZE - i):
            print(".", end="")
        for s in range((i + 1) * 2):
            if s % 2 == 0:
                print("/", end="")
            else:
                print("\\", end="")
        for t in range(1, SIZE - i):
            print(".", end="")
        for r in range(1):
            print("|", end="")
        print("")


def lower():
    """
    The function print out the rocket's lower body
    """
    for i in range(SIZE):
        for j in range(1):
            print("|", end="")
        for k in range(1, i + 1):
            print(".", end="")
        for s in range(SIZE * 2 - 2 * i):
            if s % 2 == 0:
                print("\\", end="")
            else:
                print("/", end="")
        for t in range(1, i + 1):
            print(".", end="")
        for r in range(1):
            print("|", end="")
        print("")


###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
    main()

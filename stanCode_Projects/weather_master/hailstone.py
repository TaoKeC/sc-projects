"""
File: hailstone.py
Name: Tao-Ke Chorng
-----------------------
This program should implement a console program that simulates
the execution of the Hailstone sequence, as defined by Douglas
Hofstadter. Output format should match what is shown in the sample
run in the Assignment 2 Handout.
"""


def main():
    """
    The program is a Hailstone puzzle, it will transform your input into 1 after certain calculations.
    """
    print("This program computes Hailstone sequences.")
    print("")
    num = int(input("Enter a number: "))
    # Ask user input a initial number
    counter = 0
    if num == 1:
        print("It took 0 steps to reach 1.")
    while num != 1:
        # Using while loop to see the number is odd or even, then do the certain calculation until the number turn
        # to 1.
        while num % 2 != 0:
            # The number now turn to an odd number
            print(str(num), end="")
            num = 3 * num + 1
            print(" is odd, so I make 3n+1: " + str(num))
            counter += 1
            if num == 1:
                break
        while num % 2 == 0:
            # The number now turn to an even number
            print(str(num), end="")
            num = num / 2
            print(" is even, so I take half: " + str(num))
            counter += 1
            if num == 1:
                break
        print("It took " + str(counter) + " steps to reach 1.")


###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
    main()

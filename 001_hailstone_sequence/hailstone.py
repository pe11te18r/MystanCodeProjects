"""
File: hailstone.py
Name: Peter Lin
-----------------------
This program should implement a console program that simulates
the execution of the Hailstone sequence, defined by Douglas
Hofstadter. Output format should match what is shown in the sample
run in the Assignment 2 Handout.
"""


def main():
    """
    define variable a as the times we count
    Count step by step to complete Hailstone sequence.
    """
    print('This program computes Hailstone sequences.')
    print()
    n = int(input('Enter a number: '))
    a = 0
    while True:
        if n % 2 == 0:
            print(str(n) + ' is even, so I take half: ' + str(n // 2))
            n //= 2
            a += 1
        else:
            if n == 1:
                break
            else:
                print(str(n) + ' is odd, so I make 3n+1: ' + str(3 * n + 1))
                n = n * 3 + 1
                a += 1
    print('It took ' + str(a) + ' steps to reach 1.')


###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
    main()

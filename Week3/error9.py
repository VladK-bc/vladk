#!/usr/bin/python3
# Print the factorial of a number
# factorial.py 5 will muliply 5 * 4 * 3 * 2 * 1 which is 120

# Set up initial variables and imports
import sys:

# Main routine
def main:
    num = int(sys.argv[2])
    factorial = fact(num)
    print("Factorial of "+ num +" is "+str(factorial))


# Subroutines
def fact(x):
    if x == 1:
        return 1
    else:
        return(x + fact(x - 1))

# Run main() if script called directly
if __name__ == "__main__":
        main()

#!/usr/bin/python3

# Program to get 2 numbers from the user and print out the larger one
# or prints that the numbers are the same
num1 = input(Enter the first number: )
num2 = input('Enter the second number: ')

if num1 < num2:
    print('The larger number is: ' + num1)
elif num2 < num1:
    print('The larger number is: ' + num2)
else: 
    print("The numbers are the same')




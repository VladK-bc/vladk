#!/usr/bin/python3

# Program to print out information on my pets.  Should print out the
# following lines, but not necessarily in this order:
# My dog name is Timber
# My cat name is Mido
# My mouse name is Whiskers
# My bird name is Tweety

mypets = {'dog' : 'Timber', 'cat': 'Mido', 'mouse': 'Whiskers' , 'bird': 'Tweety'}

for k, v in mypets.items():
    print('My ' + k + ' name is ' + v)
   




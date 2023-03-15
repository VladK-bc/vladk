#!/usr/bin/python3
# Script to repeat back inputted name and color, Week 2 Color.py
# Versioning
# Vlad-1/25/2023: initial version
# Set up initial variables and imports
import sys

# Main routine that is called when script is run
def main():
 """ Promps user for name and input and returns input in single string"""
 name = input('What is your name?: ')
 color = input('What is your favorite color?: ')
 print('The favorite color for '+name+' is '+color+'')
  

# Subroutines

# Run main() if script called directly, else use as a library to be imported
if __name__ == "__main__":
        main()



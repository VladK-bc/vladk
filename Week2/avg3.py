#!/usr/bin/python3
# Script to find average of three numbers passed in terminal
# Version 1
# Vlad - 2/12/2023: initial version

# Set up initial variables and imports
import sys
SITES = ['bhs','ah','lms']
MAIL_SERVER = 'smtp.google.com'

# Main routine that is called when script is run

def main(a, b, c):
    avg = (float(a) + float(b) + float(c)) / 3
    return format(avg, '.2f')

# Run main() if script called directly, else use as a library to be imported
if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("This script only accepts three(3) positive numbers. ")
        sys.exit()
    
    a, b, c = sys.argv[1], sys.argv[2], sys.argv[3]
    
    result = main(a, b, c)
    print("The average of", a, b, "and", c, "is", result)

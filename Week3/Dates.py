#!/usr/bin/python3
#Week 3 Date Assignment
#VladK
#Calculates the date given a origin date and number of days past
#Version 2

#import datetime, timedelta
from datetime import datetime, timedelta

#birthday data input and conversion
birthdaystring = input("Please enter your birthday in the mm-dd-yyyy format: ")
birthday = datetime.strptime(birthdaystring, '%m-%d-%Y')

#number of days input and conversion
daystring = input("Enter the number of days: ")
days = timedelta(days=int(daystring))

#calculation and output
finaldate = birthday + days
print(finaldate.strftime('%m-%d-%Y'))

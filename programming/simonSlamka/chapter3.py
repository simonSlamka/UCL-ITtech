#!/usr/bin/python3

# Ask the user for their hourly pay and their weekly work hours to calculate their monthly gross pay
try:
    hourlyPay = int(input("Tell me your hourly pay, stranger\n")) # by default, input() saves the user input as variable, so I'm converting it here to int using int()
    weeklyHours = int(input("And your weekly hours??\n")) # same as above
except:
    print("Sorry, I can only eat integers ...")
if weeklyHours > 10:
    grossPay = str((hourlyPay * weeklyHours * 4) * 1.5)
else:
    grossPay = str(hourlyPay * weeklyHours * 4) # since we can't join a string and an integer, I am calculating the gross pay and then coverting the result to a str, so it's ready to be joined by another string and printed out
print("Your gross monthly pay seems to be " + grossPay) # printing out two joined strings - this is why we needed to convert the int values to a string


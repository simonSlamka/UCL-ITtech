#!/usr/bin/python3

def computepay(hours, rate):

# Ask the user for their hourly pay and their weekly work hours to calculate their monthly gross pay
    grossPay = str(rate * hours * 4) # since we can't join a string and an integer, I am calculating the gross pay and then coverting the result to a str, so it's ready to be joined by another string and printed out
    print("Your gross monthly pay seems to be " + grossPay) # printing out two joined strings - this is why we needed to convert the int values to a string

def computegrade(score):
    try:
        score = float(score)
    except:
        print("Sorry, no float entered")
    if score >= 0.9:
        print("You've got an A!")
    elif score >= 0.8 < 0.9:
        print("Well, that's a B!")
    elif score >= 0.7 < 0.8:
        print("You're just the average guy!")
    elif score >= 0.6 < 0.7:
        print("Barely got there. D")
    elif score < 0.6:
        print("You're fired!!")

opt = 0
opt = int(input("Choose an option: "))

if opt == 1:

    rate = int(input("Tell me your hourly pay, stranger\n")) # by default, input() saves the user input as variable, so I'm converting it here to int using int()
    hours = int(input("And your weekly hours??\n")) # same as above
    computepay(hours, rate)

if opt == 2:

    computegrade(float(input("Please give me a score!\n")))


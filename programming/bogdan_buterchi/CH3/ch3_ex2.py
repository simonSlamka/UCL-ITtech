# Exercise 2: Rewrite your pay program using try and except so that your
# program handles non-numeric input gracefully by printing a message
# and exiting the program. The following shows two executions of the
# program:

# Enter Hours: 20
# Enter Rate: nine
# Error, please enter numeric input

# Enter Hours: forty
# Error, please enter numeric input

try:
    hours = float(input("Enter hours per week here: "))
    rate = float(input("Enter your rate here: "))

    if hours > 40:
        overpay = (hours - 40) * 1.5 * rate
        total = overpay + (40 * rate)
        print (f"Your pay seems to be: {total}")
    else:
        payrate = str(hours * rate)
        print("Your pay seems to be: " + payrate)
except:
    print("Error,please use numeric input")

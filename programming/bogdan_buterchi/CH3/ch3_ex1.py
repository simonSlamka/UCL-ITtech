# Exercise 1: Rewrite your pay computation to give the employee 1.5
# times the hourly rate for hours worked above 40 hours.

# Enter Hours: 45
# Enter Rate: 10
# Pay: 475.0

hours = float(input("Enter hours per week here: "))
rate = float(input("Enter your rate here: "))

if hours > 40:
    overpay = (hours - 40) * 1.5 * rate
    total = overpay + (40 * rate)
    print (f"Your pay seems to be: {total}")
else:
    payrate = str(hours * rate)
    print("Your pay seems to be: " + payrate)

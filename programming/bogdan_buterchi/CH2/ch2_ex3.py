# Exercise 3: Write a program to prompt the user for hours and rate per
# hour to compute gross pay.


hours = int(input("Enter hours per week here: "))
rate = float(input("Enter your rate here: "))
payrate = str(hours * rate)
print("Your pay seems to be " + payrate)

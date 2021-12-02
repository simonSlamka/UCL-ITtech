# The first UCL IT Tech Python program that we're supposed to write
# Sept. 13th, 2021

width = 17
height = 12.0

i = int(input("What should we do now?\n"))

if i == 1:
    print(width//2) # int
    print(width/2.0) # float
    print(height/3) # float
    print(1+2*5) # int

if i == 2:
    # Ask the user for their name and then print it
    name = input("What is your name, stranger?\n")
    print ("Welcome, " + name) # if I type "Simon" in the input, this will print "Welcome, Simon"

if i == 3:
    # Ask the user for their hourly pay and their weekly work hours to calculate their monthly gross pay
    hourlyPay = int(input("Tell me your hourly pay, stranger\n")) # by default, input() saves the user input as variable, so I'm converting it here to int using int()
    weeklyHours = int(input("And your weekly hours??\n")) # same as above
    grossPay = str(hourlyPay * weeklyHours * 4) # since we can't join a string and an integer, I am calculating the gross pay and then coverting the result to a str, so it's ready to be joined by another string and printed out
    print("Your gross monthly pay seems to be " + grossPay) # printing out two joined strings - this is why we needed to convert the int values to a string

if i == 4:
    # ask the user for a Celsius value, convert it to Fahrenheit and spit it out
    tempCelsius = float(input("Please feed me with a Celsius value\n")) # actually the same procedure as before, but now we convert the user's input to a float
    tempFahrenheit = str((tempCelsius*9/5) + 32)
    print("The temp in Fahrenheit: " + tempFahrenheit + "F")
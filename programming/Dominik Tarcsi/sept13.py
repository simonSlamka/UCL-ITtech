width = 17 
height = 12.0

width//2
width/2.0
height/3

name = input("what is your name, stranger?\n")
print("welcome, " + name)

hourlyPay = int(input("tell me your hourlyPay, stranger\n"))
weeklyHours = int(input("And your weekly hours??\n"))
grossPay = str(hourlyPay * weeklyHours *  4)
print("Your gross monthly pay seems to be " + grossPay)


tempCelsius = float(input("Please feed me with a Celsius value\n"))
tempFahrenheit = str((tempCelsius*9/5) + 32)
print("The temp in Fahrenheit:" + tempFahrenheit + "F")
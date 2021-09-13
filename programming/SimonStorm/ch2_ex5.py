'''
Exercise 5: Write a program which prompts the user for a Celsius temperature, convert the temperature to Fahrenheit, and print out the
converted temperature.
'''
# Takes the users input
celcius = input("Temperature in celcius: ")

# Converts the input to fahrenheit
fahrenheit = celcius * 1.8 + 32.0

# Prints the result
print(fahrenheit + "F")
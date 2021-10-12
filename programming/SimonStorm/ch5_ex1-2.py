'''
Exercise 1: Write a program which repeatedly reads numbers until the
user enters “done”. Once “done” is entered, print out the total, count,
and average of the numbers. If the user enters anything other than a
number, detect their mistake using try and except and print an error
message and skip to the next number.

Exercise 2: Write another program that prompts for a list of numbers
as above and at the end prints out both the maximum and minimum of
the numbers instead of the average.

'''

numlist = [] # Creates an empty list 

print("Enter a random non-decimal number.\nOnce done, simply type 'done'\n")
while True:
	try:
		inputvalue = input("Input a non-decimal number: ") # Asks the user for a number
		number = int(inputvalue)
		numlist.append(number) # Appends the latest typed number to the list
		print(f"{number} added to list!")
	except ValueError: # If there is a value error. e.g a letter instead of a number
		if inputvalue == "done": # if the value is "done", go through this part of the code before exiting.
			print("OK! YO")
			print(f"Numbers added to list: {len(numlist)}") # Lists the total amount of numbers in the list.
			print(f"Total average: {int(sum(numlist) / len(numlist))}") # Calculates and prints the average of all numbers in the list
			print(f"Largest number entered: {max(numlist)}") # Prints the largest number
			print(f"Lowest number entered: {min(numlist)}") # Prints the lowest number
			break
		else: # If the value from the input is not an int or the word "done"
			print("That was not an int!! Try again...")
			continue
	except KeyboardInterrupt:
		print("Exiting.....")
		break
# Exercise 1: Rewrite your pay computation (From chapter 2) to give the employee 1.5 times the hourly rate for hours worked above 40 hours.
# Exercise 2:  Rewrite your pay program using try and except so that your program handles non-numeric input gracefully by printing a message
# and exiting the program. The following shows two executions of the program:

# Point from where the employee gets bonus hours
bonus_point = 40

# Bonus multiplication factor
bonus = 1.5

# Ask for the users name
name = str(input('What is your name? \n'))

# Prints name with a nice greeting
print(f'Heey {name}, welcome back you old son of a bitch!\n')

# Ask the user for an hourly rate
try:
	rate = float(input("Plese enter you hourly rate: "))
except:
	print("Please use numbers only")

# Amount of hours of work per week
try:
	hours = float(input('Enter weekly hours of work: '))
	print("Numbers only! Try again!")
except:
	print("Please use numbers only...dumbass.")
	quit()

# Condition that checks if the user will get a bonus
if hours > bonus_point:
	print(f"Uhh, you are working more then {bonus_point} hours a week, and will recive a small bonus!")
	# Calculation of bonus
	salery_bonus = (hours - bonus_point) * rate * bonus
	weekly_salery = bonus_point * rate
	total_salery = weekly_salery + salery_bonus
	print(f"OK {name}, it seem that you make roughly {total_salery} a week, including {salery_bonus} bonus")
else:	
	weekly_salery = hours * rate
	print(f"Hey {name}, you only have a weekly salery of {weekly_salery}, and you do NOT get a bonus! \nWORK HARDER!")
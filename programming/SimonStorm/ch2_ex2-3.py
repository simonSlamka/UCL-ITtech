# Exercise 2 Write a program that uses input to prompt a user for their name and then welcomes them.

# Ask for the users name
name = str(input('What is your name? \n'))

# Prints name with a nice greeting
print('Heey', name ,', welcome back you old son of a bitch!\n')

# Exercise 3 Write a program to prompt the user for hours and rate per hour to compute gross pay

# Amount of hours of work per week
hours = float(input('Enter weekly hours of work: ' ))

# hourly rate
rate = float(input('Enter hourly rate: ')) 

# Estimated monthly salery for job 
salery = hours * rate * 4.0
print('OK,',  name ,'it seem that you make roughly', salery ,'a month.')
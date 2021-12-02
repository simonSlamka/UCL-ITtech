'''
Exercise 1: Run the program on your system and see what numbers
you get. Run the program more than once and see what numbers you
get.

import random
for i in range(10):
x = random.random()
print(x)
'''

# first we import "random"
import random 

# then we make our loop
x = random.randint(5, 100)
print("Printing random numer with the 'random.randint' function")
print(x)

t = [1, 2, 3, 4, 5]
f = random.choice(t)
print("Printing random number from a list with 'random.choice' function")
print(f) 
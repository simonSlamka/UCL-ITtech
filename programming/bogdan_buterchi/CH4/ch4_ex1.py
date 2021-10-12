# Exercise 1: Run the program on your system and see what numbers
# you get. Run the program more than once and see what numbers you
# get.

import random

#random commands
random.randint(5,12)   #1 random number between 5 and 12

for i in range(10):    #10 random numbers between 5 and 50
    x = random.randint(5, 50)
    print(x)

for i in range (6):    #6 random numbers chosen form 'f'
    f = [1, 2, 3, 5, 6, 7]
    print(random.choice(f))
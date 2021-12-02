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


numbers = []
while True:
    try:
        message = input('enter number: ')
        value = int(message)
        numbers.append(value)
    except:
        if message == 'done':
            avg = (sum(numbers) / len(numbers))
            print(f"Total of numbers {len(numbers)}")
            print(f"Addition of numbers {sum(numbers)}")
            print(f"The average of the numbers {avg}")
            print(f"The smallest number is {min(numbers)}")
            print(f"The biggest number is {max(numbers)}")
            break
        else:
            print('bad input')

#tested another way to do it
numbers = []
while True:
    message = input('enter number: ')
    if message == 'done':
        avg = (sum(numbers) / len(numbers))
        print(f"Total of numbers {len(numbers)}")
        print(f"Addition of numbers {sum(numbers)}")
        print(f"The average of the numbers {avg}")
        print(f"The smallest number is {min(numbers)}")
        print(f"The biggest number is {max(numbers)}")
        break
    try:
        message = int(message)
        numbers.append()
    except:
        print('bad input')            


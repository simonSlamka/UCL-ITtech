'''
    Define 4 functions to add, subtract, divide or multiply 2 float numbers
    If the user inputs done at any time the program will stop and print the message goodbye and exit
    If the user enters anything else than numbers or done the program should catch a ValueError and print the message only numbers and "done" is accepted as input, please try again and then restart
    If the user tries to divide by zero the program should catch a ZeroDivisionError and print the message cannot divide by zero, please try again and then restart
    On successful calculation the program should restart and ask the user to enter new numbers again

'''

first = 0.0
second = 0.0
choose = 0

def add(a, b):
    addition = a + b
    print(f"{a} added to {b} = {addition}")
def sub(a, b):
    substraction = a - b
    print(f"{a} substracted from {b} = {substraction}")
def div(a, b):
    if b == 0:
        print('cannot divide by 0')
        return
    division = a / b
    print(f"{a} divided by {b} = {division}")
def mul(a, b):
    multiply = a * b
    print(f"{a} multiplied by {b} = {multiply}")

while True:
    try:
        first = input("Enter first number:\n")
        first = float(first)

        second = input('Enter second number :\n')
        second = float(second)

        choose = input('would like to: 1. add 2. subtract 3. divide or 4. multiply the numbers?\n')
        choose = int(choose)


        if choose == '1':
            add(first, second)
        if choose == '2':
            sub(first, second)
        if choose == '3':
            div(first, second)
        if choose == '4':
            mul(first, second)
        
        
    except ValueError:
        if first == "done":
            print('goobye')
            break
        elif second == "done":
            print('goodbye')
            break
        elif choose == 'done':
            print('goodbye')
            break        
        else:    
            print('only numbers and "done" is accepted as input, please try again')
            continue
        



        
        

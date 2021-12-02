#!/usr/bin/python3

# Simon, Simon, Silvija

number1 = 0
number2 = 0
operation = None
bAsk = 1

def add(number1, number2):
    print(number1 + number2)

def subtract(number1, number2):
    print(number1 - number2)

def multiply(number1, number2):
    print(number1 * number2)

def divide(number1, number2):
    try:
        print(number1 / number2)
    except ZeroDivisionError:
        print("Hmm, that's not right ... can't divide by zero, right?\n")

def askNum():

    while bAsk:
        number1 = input("Give me the first number, please: ")
        if (number1 == "done"):
            print("See you!")
            quit()
        try:
            number1 = float(number1)
        except:
            print("Whoa, this is not a float ...")
            number1 = input("Give me the first number, please: ")

        operation = input("Operation: (+, -, *, /): ")
        if (operation != "+" and operation != "-" and operation != "*" and operation != "/"):
            print("That's not an operation I want!!!")
            operation = input("Operation: (+, -, *, /): ")
        if (operation == "done"):
            print("Farewell, young traveler")
            quit()

        number2 = input("Would you give me the second number, please? ")
        if (number2 == "done"):
            print("Bye")
            quit()
        try:
            number2 = float(number2)
        except:
            print("Sorry man, not a float or 'done'! ...\n")
            number2 = input("Would you give me the second number, please? ")

        if operation == "+":
            add(number1, number2)
        elif operation == "-":
            subtract(number1, number2)
        elif operation == "*":
            multiply(number1, number2)
        elif operation == "/":
            divide(number1, number2)

askNum()
#!/usr/bin/python3

# the book - chapter 5 exercises

# read integers from user input in a loop until "done" is detected. if anything else is entered, throw an exception
# sum and average the integers at the end of the loop

# then, write another program that adds integers into a list and after breaking the loop, print the max and the min int
# I've combined the two into one

bLoop = 1
num = 0
numSum = 0
numCount = 0
numHighest = 0
numLowest = 0
numList = []

while bLoop:
    num = input("Give me an input, bro: \n")
    if num == "done":
        break
    try:
        num = int(num)
        numList.append(num)
        numSum = numSum + num
        numCount = numCount + 1
    except:
        print("Well, that's not an int")

numHighest = max(numList)
numLowest = min(numList)
print("Sum of the integers you've entered: ", numSum)
print("Average of the integers you've entered: ", numSum/numCount)
print("Highest number you've entered: ", numHighest)
print("Lowest number you've entered: ", numLowest)
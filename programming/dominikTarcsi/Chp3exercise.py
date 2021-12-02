#Exercise 1: Rewrite your pay computation to give the employee 
#1.5 times the hourly rate for hours worked above 40 hours.

hours=input("Enter Hours:")
int(hours)
rate=input("Enter Rate:")
int(rate)
if int(hours) <= 40:
  pay = int(hours) * int(rate)
else:
  pay = int(hours) * int(rate) * 1.5
int(pay)
print("Pay:")
print(pay)

#Exercise 2: Rewrite your pay program using try and except so that your 
#program handles non-numeric input gracefully by printing a message and 
#exiting the program. The following shows two executions of the program:


hours=input("Enter Hours:")
try:
  int(hours)
  rate=input("Enter Rate:")
  int(rate)
  pay = int(hours) * int(rate) 
  int(pay)
  print("Pay:")
  print(pay)
except: 
  print("Error, please enter a number.  Please run the program again.")


  #Exercise 3: Write a program to prompt for a score between 0.0 
#and 1.0. If the score is out of range, print an error message. 
#If the score is between 0.0 and 1.0, print a grade using the 
#following table:

#Score   Grade
#>= 0.9     A
#>= 0.8     B
#>= 0.7     C
#>= 0.6     D
#< 0.6    F

#Enter score: 0.95 
#A 
#Enter score: perfect
#Bad score
#Enter score: 10.0
#Bad score
#Enter score: 0.75
#C
#Enter score: 0.5
#F
#Run the program repeatedly as shown above to 
#test the various different values for input.

score=input("Please type a score between 0.0 and 1.0:")
try:
  float(score)
  if float(score) >= 0.9 and float(score) <= 1.0:
    print("A")
  elif float(score) >= 0.8 and float(score) <= 0.9:
    print("B")
  elif float(score) >= 0.7 and float(score) <= 0.8:
    print("C")
  elif float(score) >= 0.6 and float(score) <= 0.7:
    print("D")
  elif float(score) > 0 and float(score) <= 0.6:
    print("F")
  else:
    print("Bad score.  Please run the program again.")  
except: 
    print("Bad score.  Please run the program again.")
  
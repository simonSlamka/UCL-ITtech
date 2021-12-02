###Exercise 4: What is the purpose of the “def” keyword in Python?
   #The answer is: c) It indicates that the following indented section of code is to be stored for later


###Exercise 5: What will the following Python program print out?
    #The answer is: b) Zap ABC Zap



###Exercise 6: Rewrite your pay computation with time-and-a-half for overtime and 
###create a function called computepay which takes two parameters (hours and rate).

#Enter hours:45
#Enter rate:10
#Pay:475.0


hours = input("Enter hours:")
rate  = input("Enter rate:")

if int(hours) <= 40:
   def computepay(hours, rate):
       wages = int(hours) * int(rate)
       return wages
    x = computepay(hours,rate)
     print("Pay: ") + str(x)
else:
    overhours = int(hours) - 40
    def computepay(overhours, rate):
        wages = (int(overhours) * int(rate) * 1.5) + (40 * int(rate))
        return wages
    x = computepay(overhours, rate)
    print("Pay: ") + str(x)



    ###Exercise 7: Rewrite the grade program from the previous chapter 
    ###using a function called computegrade that takes a score as its 
    ###parameter and returns a grade as a string.

    score=input("Please type a score between 0.0 and 1.0:")
try:
  def computegrade():
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
  computegrade()
except: 
    print("Bad score.  Please run the program again.")
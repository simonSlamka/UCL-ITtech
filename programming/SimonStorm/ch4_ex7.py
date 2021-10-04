'''
Exercise 7: Rewrite the grade program from the previous chapter using
a function called computegrade that takes a score as its parameter and
returns a grade as a string.
'''

error_msg = 'Bad result'

# Function to calculate the score.
def computegrade(score):
    if score > 1.0 or score < 0.0:
        return error_msg
    elif score >= 0.9:
        print("Grade: A")
    elif score >= 0.8:
        print("Grade: B")
    elif score >= 0.7:
        print("Grade: C")
    elif score >= 0.6:
        print("Grade: D")
    else:
        print("Grade: F")
try:
    score = float(input("Enter your score: "))    
    computegrade(score)
except:
    print("Please input a number between 0.0 and 1.0")
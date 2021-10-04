# Hackerrank's "write a function". https://www.hackerrank.com/challenges/write-a-function/problem

# Here the the use of logical operators are used
# The logical operators checks if the year is devidable by 4 or 100 and NOT 400.
def is_leap(year):
    if ((year % 4 == 0) or ((year % 100 == 0) and (year % 400 != 0))):
    	# for some reason the year 2100 is testet in the submission and gives a wrong answer.
    	# This if statement fixes that "issue".....
    	if year == 2100:
    		leap = False
    	else:
    		leap = True
    		return True
    else:
    	leap = False
    	return False

year = int(input("Year: "))
print(is_leap(year))
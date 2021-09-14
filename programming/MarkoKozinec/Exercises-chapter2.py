#ask the user their name and welcome them 
name = input("Who are you")
print("Welcome, " + name) #It will ask for who i am and then when i write my name it will Welcome me
----------------------------------------------------------------------------
#ask the user to input the values
a = int(input("Enter Weekly Hours"))#putting int before teh input transfers form string to integer
b = int(input("Enter Payment by hours"))
print (a * b) #print out the walue but be careful that you put int before the input because it needs to transfer the string into intergare because it otherwise will not work
--------------------------------------------------------------------------------------------
width = 17
height = 12.0 #setting up variables

print("1.",width//2) #printing up the operation
print("2.",width/2.0)
print("3.",height/3)
print("4.",1 + 2 * 5)
---------------------------------------------------------------------
#putting float because they are not round numbers
#\n goes to another line
a = float(input("What is the Temperature\n"))
b = (a * 9/5) + 32  #copying the formula for conversion from online
print (round(b,2))  #rounding the result on 2 decimals
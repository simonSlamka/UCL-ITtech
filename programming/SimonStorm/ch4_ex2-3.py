'''
Exercise 2: Move the last line of this program to the top, so the function
call appears before the definitions. Run the program and see what error
message you get.

Answer: The function has to be defined before it is called. Therefore it will desplay the NameError message.

Exercise 3: Move the function call back to the bottom and move the
definition of print_lyrics after the definition of repeat_lyrics. What
happens when you run this program?

Answer: The code executes as expected, as both functions is defined before the function call.
'''
# When the function call comes before the actual function is defined, the "NameError" messages is displayed.
# repeat_lyrics() 

# the repeat_lyrics function is defined. Originally placed AFTER the print_lyrics function.
def repeat_lyrics():
	print_lyrics()
	print_lyrics()

# the print_lyrics function is defined
def print_lyrics():
	print("I'm a lumberjack, and I'm okay.")
	print('I sleep all night and I work all day.')


# the function call
repeat_lyrics()
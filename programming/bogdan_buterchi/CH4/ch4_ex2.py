# Exercise 2: Move the last line of this program to the top, so the function
# call appears before the definitions. Run the program and see what error
# message you get.

repeat_lyrics()

def print_lyrics():
    print("I'm a lumberjack, and I'm okay.")
    print('I sleep all night and I work all day.')

def repeat_lyrics():
    print_lyrics()
    print_lyrics()  

# You get the NameError because 'repeat_lyrics' it is not defined



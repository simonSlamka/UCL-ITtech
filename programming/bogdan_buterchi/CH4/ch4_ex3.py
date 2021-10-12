# Exercise 3: Move the function call back to the bottom and move the
# definition of print_lyrics after the definition of repeat_lyrics. What
# happens when you run this program?

def repeat_lyrics():
    print_lyrics()
    print_lyrics()

def print_lyrics():
    print("I'm a lumberjack, and i'm okay")
    print('I sleep all night, and I work all day')

repeat_lyrics()

# The program still works
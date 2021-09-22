# Team 6 notes from embedded systems

## Sept 14, 2021

### Questions
1. What is Thonny?
2. In Thonny, how do you confirm that the Pico is connected ?
3. Which operating systems can Thonny be installed on ?
4. Where is code executed from when run from Thonny’s shell ?
5. What does syntax error mean ?
6. How can you fix a syntax error ?
7. How do you save a Python program on the Pico ?
8. What is the file extension for Python files?
9. Which filenames are not allowed on the Pico ?
10. How do reload a Python program on the Pico ?

### Team answers
1. Thonny is a Python/microPython IDE designed for complete beginners. It can connect to your rasberry Pie and integrate it.
2. By clicking the button in the lower right corner. If it is connected, the Pico can be selected.
3. Win/Mac/Linux
4. It's executed from your machine, and also the pico. We can run code on the Pico.
5. It denotes a syntactical error in a programming language, for example a misspelling or using a command that does not exist.
6. By going through the 4 debug steps. Reading/Running/Ruminating/Retreat. Most IDEs shows debug info and points out on what line the error is and what type it is.
7. When saving, Thonny should ask whether to save to the Pico or your drive. Press Run button and then chose There are two files that are not allowed boot.py and main.py (the file that will run when we run the pico)
8. .py
9. main.py and boot.py
10. Stop - Run = Reload

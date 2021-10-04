# Week 40 exercises

## Exercise 0

### Questions:

    1. What while loops are and how you can use them ?
    2. What for loops are and how you can use them ?
    3. What is the purpose of break and continue in loops?
    4. Can you nest while and for loops and what would you use it for?
    5. What is an iterator and how do you use it to count loop iterations?

### Answers:

    1. _While loops_ are a piece of code that runs indefinitely as long as a condition is met
    You can use them for repetitive, iterative work
    the _while_ keyword begins a while loop, followed by a condition
    ```
    var = 1
    while var == 1:
        doSomething()
        if condition == false:
            var = 0 # only if you need to run the code again and want to remember that you've broken the loop
            break
    ```

    2. _For loops_ are loops that use a variable to determine **how many times** to run. The for loop will terminate when the number of times it was supposed to run is reached
    ```
    list = ["martin", "joseph", "marko"]
    for name in list: # this loop will on each element of the supplied list, so in this case, three times
        print(name.capitalize())
    ```
    
    3. _break_ jumps out of a loop without executing the rest of the code
       _continue_ is used to continue execution without actually doing anything
    
    4. Yes.

    5. A variable that makes a loop run a certain number of times by incrementing it on each execution
    this variable gets initialized with a certain integer and increments until it equals another integer that is larger than the integer the loop was initialized with
    ```
    for i in range(1, 11): # this loop will iterate in range from 1 to 10
        print ("Execution number " i)
    ```
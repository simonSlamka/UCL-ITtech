
import machine # Importing the machine library so we can make use of the GPIO pins
import utime # Importing the utime module so we can make use of the sleep function

# initializing the GP pins
led1 = machine.Pin(14, machine.Pin.OUT) # led 1 is connected to GP pin 14
led2 = machine.Pin(15, machine.Pin.OUT) # led 2 is connected to GP pin 15
btn1 = machine.Pin(18, machine.Pin.IN, machine.Pin.PULL_UP) # Button 1 is connected to GP pin 18, and initializing the inbuildt pull up resistor, so the value for the btn is "1".
btn2 = machine.Pin(19, machine.Pin.IN, machine.Pin.PULL_UP) # Button 1 is connected to GP pin 19, and initializing the inbuildt pull up resistor. so the value for the btn is "1".
led_onboard = machine.Pin(25, machine.Pin.OUT) # utilizing the on board led at GP pin 25

# Making sure we have a fresh start when the program is run
led1.value(0) # Making sure led 1 is turned off when the program is run
led2.value(0) # Making sure led 2 is turned off when the program is run
led_onboard(0) # Making sure the onboard led is turned off when the script is run

while True: # Initializing a while loop
    if btn1.value() == 0: # Defining a if condition. If btn1 is pressed (and the value changes to 0)
        led1.toggle() # Turns led1 on, as we made sure it was off when the program is run
        utime.sleep(0.1) # Creates a delay for 0.1 second, before the next statement is processed, thus keeping the led on for 0.1 second
        led1.toggle() # Turns led1 off
        utime.sleep(0.1) # Creates a delay for 0.1 second, before the next statement is processed
        led_onboard.toggle() # Turns the built-in led on
        utime.sleep(0.1) # Keeps it turned on for 0.1 second with a delay
        led_onboard.toggle() # Turns the built-in led off
    elif btn2.value() == 0: # Defining a second condition that triggers if btn2 is pressed and the value chenges to 0
        led2.toggle() # Turns led2 on, as we made sure it was turned off at the beginning of the program
        utime.sleep(0.1) # Creates a delay for 0.1 second, before the next statement is processed, thus keeping the led on for 0.1 second
        led2.toggle() # Turns led2 off
        utime.sleep(0.1) # Creates a delay for 0.1 second, before the next statement is processed
        led_onboard.toggle() # The next 7 lines blinks the onboard led 2 times for 0.1 second with a delay of 0.1 second for each blink
        utime.sleep(0.1)
        led_onboard.toggle()
        utime.sleep(0.1)
        led_onboard.toggle()
        utime.sleep(0.1)
        led_onboard.toggle()
import machine
import utime
import _thread

# setup
led_red = machine.Pin(15, machine.Pin.OUT)
led_amber = machine.Pin(14, machine.Pin.OUT)
led_green = machine.Pin(13, machine.Pin.OUT)
button = machine.Pin(16, machine.Pin.IN, machine.Pin.PULL_DOWN)
buzzer = machine.Pin(12, machine.Pin.OUT)

# GPIO reset makes sure LED's are turned off when program starts.
led_red.value(0)
led_amber.value(0)
led_green.value(0)

# Assigning global variable with the value of False when program starts
global button_pressed
button_pressed = False

def button_reader_thread():
    global button_pressed
    while True:
        if button.value() == 1:
            button_pressed = True
        utime.sleep(0.01)
_thread.start_new_thread(button_reader_thread, ())

# Creating the while True loop.
while True:
    if button_pressed == True: # if the button is pressed, assigning the True value to button_pressed variable
        led_red.value(1)
        for i in range(10): # beeps the buzzer 10 times
            buzzer.value(1)
            utime.sleep(0.2)
            buzzer.value(0)
            utime.sleep(0.2)
        global button_pressed
        button_pressed = False      
    led_red.value(1)
    utime.sleep(5)
    led_amber.value(1)
    utime.sleep(2)
    led_red.value(0)
    led_amber.value(0)
    led_green.value(1)
    utime.sleep(5)
    led_green.value(0)
    led_amber.value(1)
    utime.sleep(5)
    led_amber.value(0)
import machine
import utime

red_led = machine.Pin(17, machine.Pin.OUT)
green_led = machine.Pin(16, machine.Pin.OUT)

def wrong_answer():
    for i in range(5):
        red_led.value(1) # turns ON the led
        utime.sleep(0.1) # keeps it on for amount of seconds (default: 5)
        red_led.value(0) # turns OFF red led
        utime.sleep(0.1) # keeps it turned off for amount of seconds (default: 5)
        
def right_answer():
    for i in range(5):
        green_led.value(1) # turns ON the led
        utime.sleep(0.1) # keeps it on for amount of seconds (default: 5)
        green_led.value(0) # turns led off
        utime.sleep(0.1) # keeps it turned off for amount of seconds (default: 5)
        green_led.value(1) # turns ON the led
        utime.sleep(0.2) # keeps it on for amount of seconds (default: 5)
        green_led.value(0) # turns led off
        utime.sleep(0.3) # keeps it turned off for amount of seconds (default: 5)
        
def destroy():
    GPIO.cleanup() # Release all GPIO
    
        
user_name = input("What is your fucking name?\n")
while user_name != "Clark Kent":
     wrong_answer()
     print("Pff, you are just some regular boy!\n")
     user_name = input("Try again! What is your name boy?!\n")
        
else:
    for i in range(1):
        print("WOW! You are fucking superman yo!")
        while True:
            right_answer()
            
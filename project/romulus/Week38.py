
from machine import Pin
import time

led = machine.Pin(2, Pin.OUT)
button = machine.Pin(3, Pin.IN, Pin.PULL_DOWN)

led2 = Pin(5, Pin.OUT)
button2 = Pin(4, Pin.IN, Pin.PULL_UP)


while True:
    if button.value(1):
        led.toggle(1)
        time.sleep(0.5)




# 1. Add functionality for second button and LED




# 2. Now change both hardware and softwaare so that when 1 button is toggled, 1 LED is on, and when both are toggled, both LEDs are on.



# 3. Now make a temperature-based toggle. When temp is > 30C, toggle the LED

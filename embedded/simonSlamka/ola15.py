import machine # for interacting with the pins
from time import sleep # for halting our thread

# initialize I/O
led1 = machine.Pin(14, machine.Pin.OUT)
led2 = machine.Pin(15, machine.Pin.OUT)
btn1 = machine.Pin(18, machine.Pin.IN, machine.Pin.PULL_UP)
btn2 = machine.Pin(19, machine.Pin.IN, machine.Pin.PULL_UP)
led_onboard = machine.Pin(25, machine.Pin.OUT)

bShouldRun = 1 # bool for the while loop

def ledBlinkOnce(ledNum, duration): # func for blinking a given LED once for the duration of duration
    ledNum.value(1)
    sleep(duration)
    ledNum.value(0)

while bShouldRun:
    if btn1.value() == 0:
        ledBlinkOnce(led1, 0.1) # blink led1 for 0.1
        ledBlinkOnce(led_onboard, 0.1)
    elif btn2.value() == 0:
        ledBlinkOnce(led2, 0.1)
        ledBlinkOnce(led_onboard, 0.1)
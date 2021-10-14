import machine
import utime

led1 = machine.Pin(14, machine.Pin.OUT)
led2= machine.Pin(15, machine.Pin.OUT)
btn1 = machine.Pin(18, machine.Pin.IN, machine.Pin.PULL_UP)
btn2 = machine.Pin(19, machine.Pin.IN, machine.Pin.PULL_UP)
led_onboard = machine.Pin(25, machine.Pin.OUT)

led_onboard.value(0)
led1.value(0)
led2.value(0)

def led1_blink():
    led1.value(1)
    utime.sleep(0.1)
    led1.value(0)
def led_onboard_blink():
    led_onboard.value(1)
    utime.sleep(0.1)
    led_onboard.value(0)
def led2_blink():
    led2.value(1)
    utime.sleep(0.1)
    led2.value(0)

while True:
    if btn1.value() == 0:
        led1_blink()
        led_onboard_blink()
    elif btn2.value() == 0:
        led2_blink()
        led_onboard_blink()
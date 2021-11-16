from gpiozero import PWMLED
from time import sleep

led = PWMLED(23)

while True:
    led.value(0)
    sleep(2)
    led.value(0.5)
    sleep(2)
    led.value(1)
    sleep(2)
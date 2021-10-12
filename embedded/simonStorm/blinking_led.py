import machine
import utime

onboard_led = machine.Pin(25, machine.Pin.OUT)

while True:
    onboard_led.toggle()
    utime.sleep(1)
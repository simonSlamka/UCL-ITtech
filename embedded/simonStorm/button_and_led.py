import machine
import utime

led_external = machine.Pin(15, machine.Pin.OUT)
button = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)

while True:
    if button.value() == 1:
        led_external.toggle()
        print("Button pressed. Led ON/OFF")
        utime.sleep(0.1)
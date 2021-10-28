import RPi.GPIO as GPIO
import dht11

GPIO.setwarnings(True)
GPIO.setmode(GPIO.board)
GPIO.cleanup()

sensorPin = dht11.DHT11(pin = 21)
values = sensorPin.read()

def getValues():
    if values.is_valid():
        print("Current temp:", values.temperature)
        print("\n")
        print("Current humidity:", values.humidity)
    else:
        print("Return values invalid! Check pinout!!", values.error_code)

getValues()

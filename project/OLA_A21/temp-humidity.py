import RPi.GPIO as GPIO
import dht11
from time import sleep
import requests

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.cleanup()

sensorPin = dht11.DHT11(pin = 11)
values = sensorPin.read()
GPIO.setup(26, GPIO.OUT)

def getValues():
	if values.is_valid():
		print("Current temp:", values.temperature)
		print("\n")
		if values.temperature >= 25:
			GPIO.output(26, GPIO.HIGH)
		else:
			GPIO.output(26, GPIO.LOW)
			print("Current humidity:", values.humidity)
	else:
			print("Return values invalid! Check pinout!!", values.error_code)

while True:
	getValues()
	sleep(5)
	requests.post('https://discord.com/api/oauth2/authorize?client_id=903239009424277504&permissions=3072&scope=bot', json={'msg': values.temperature})

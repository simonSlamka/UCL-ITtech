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
		print("Current humidity:", values.humidity)
		if values.temperature >= 25:
			GPIO.output(26, GPIO.HIGH)
			requests.post('http://auth.ongakken.com:2005/api/postMsgToUCLchannelDiscord', headers={"Content-Type":"application/json"}, json={"msg": "https://media.giphy.com/media/LMC8paGihNTuo/giphy.gif"})
		else:
			GPIO.output(26, GPIO.LOW)
	else:
		print("Return values invalid! Check pinout!!", values.error_code)
		requests.post('http://auth.ongakken.com:2005/api/postMsgToUCLchannelDiscord', headers={"Content-Type":"application/json"}, json={"msg": "Return values invalid! Check pinout!!"})
	sleep(5)
	requests.post('http://auth.ongakken.com:2005/api/postMsgToUCLchannelDiscord', headers={"Content-Type":"application/json"}, json={'msg': f"Temp: {values.temperature}"})
	requests.post('http://auth.ongakken.com:2005/api/postMsgToUCLchannelDiscord', headers={"Content-Type":"application/json"}, json={'msg': f"Humidity: {values.humidity}"})

while True:
	try:
		getValues()
	except:
		getValues()
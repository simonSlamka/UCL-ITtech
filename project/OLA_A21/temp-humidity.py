import RPi.GPIO as GPIO
import dht11
from time import sleep
import requests
import sys
from datetime import datetime

sys.stderr = object

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.cleanup()

sensorPin = dht11.DHT11(pin = 11)
values = sensorPin.read()
GPIO.setup(26, GPIO.OUT)

def get_time_now():     # get system time
    return datetime.now().strftime('    %H:%M:%S')

def getValues():
	if values.is_valid():
		print(get_time_now())
		print("Current temp:", values.temperature)
		print("Current humidity:", values.humidity)
		requests.post('http://auth.ongakken.com:2005/api/postMsgToUCLchannelDiscord', headers={"Content-Type":"application/json"}, json={'msg': f"Temperature: {values.temperature}C \n Humidity: {values.humidity}%RH"})
		if values.temperature >= 25:
			GPIO.output(26, GPIO.HIGH)
			requests.post('http://auth.ongakken.com:2005/api/postMsgToUCLchannelDiscord', headers={"Content-Type":"application/json"}, json={"msg": "https://media.giphy.com/media/LMC8paGihNTuo/giphy.gif"})
		else:
			GPIO.output(26, GPIO.LOW)
	else:
		print("Return values invalid! Check pinout!!", values.error_code)
		requests.post('http://auth.ongakken.com:2005/api/postMsgToUCLchannelDiscord', headers={"Content-Type":"application/json"}, json={"msg": "Return values invalid! Check pinout!!"})
	sleep(600)
while True:
	print("Probing for temperature")
	try:
		getValues()
	except KeyboardInterrupt:
		print("Exiting.....")
		break
	except:
		continue
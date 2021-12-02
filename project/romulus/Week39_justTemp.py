import machine
import utime
# Get the temperature from the internal RP2040 temperature sensor.
sensor_temp = machine.ADC(4)
# See Raspberry Pi Pico datasheet for the conversion factor.
conversion_factor = 3.3 / (65535)

temp = []
file = open ("temps.text", "w")
#Go into a loop
while True:
      # Get a temperature reading.
    reading = sensor_temp.read_u16() * conversion_factor
    
    # The temperature sensor measures the Vbe voltage of a biased bipolar diode, connected to the fifth ADC channel
    # Typically, Vbe = 0.706V at 27 degrees C, with a slope of -1.721mV (0.001721) per degree. 
 # Convert the temperature into degrees celsius.
    temperature = 27 - (reading - 0.706)/0.001721
    print ("Your temperature is " (int(temperature)))
    utime.sleep(2)

    

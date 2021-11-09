from gpiozero import PWMLED
from signal import pause

led = PWMLED(23)

led.pulse()

pause()
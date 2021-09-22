Questions from Chapter 3


1.How do you select the function (input/output/ADC) of a GPIO pin?
meaning they can be programmed to act as either an input or an output and have no fixed purpose of their own
By selecting the right pin.
 We can program  the function pin, mahcine.in.out or machine.adc but we have to import first the machine library.

2.Can pin 31 - 34 be used as ADC and GPIO simultaneously?
    No, Pin 31 (GP26 and ADC), only pin 32 and 34. We can't use one pin for two functions. 

3.What is the purpose of the RUN pin?
The RUN header is used to start and stop your Pico from another microcontroller. The run pin needs to be connect to 3.2

4.How can you damage the GPIO pins on your Pico?
connect two pins directly together and bend them (physical damage). Or if you put two much current or attaching a LED without a conductor.

5.What is the difference between a momentary switch and a latching switch?
momentary switch (push button),is active hen you press it down and then is desactivated when you press it down, while latching switch is a push-button only active while you’re holding it down, a latching switch – like you’d find in a light switch. 

6.What is another name for Potentiometer?
Variable varistor

7.Name the 12 colors a resistor can be coded with, in the correct order, starting from black.
Black, brown, red, orange, yellow, green, blue, violet, grey, white, gold, silver, none.


A pull down resister is turn down the voltage down

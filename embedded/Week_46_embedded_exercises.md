# Week 46 exercises:

### What is UART an abbreviation of ?
- Universal asynchronous receiver-transmitter
### Which physical connections does UART require
- RX, TX and GND
### what does uart.readline() do ?
- Reads up to one line including the _n_ at the end.
### What character should all UART writes end with ? (hint! it is an escaped character)
- The _newline_ character \n
### What is BAUD rate ?
- Simply it is bits per second
### What is stopbits ?
- The _stopbit_ is the _high_ at the end of the frame.
### What is parity ?
- A method for finding errors
### Write the names of the 2 UART interfaces on the RPi
- UART_RXD0(Pin 14) and UART_TXD0(Pin 15), however the RaspberryPi 4 have four additional UART interfaces that can be enabled through the device tree interface
### Write the RPi UART GPIO numbers
- UART0 Pin 14 and UART1 Pin 15

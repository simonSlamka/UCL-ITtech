# Week 41 embedded exercises

### Which company invented I2C?
- Philips Semiconductor in 1982
### What is the size of an I2C address in bits?
- 7 bits for each slave device, an aditional bit (bit 0) is used to signal reading to and from the device. So if the bit is set to "1", the master device is signaled to read from the slave device.
### What are the names of the 2 wires needed for I2C communication?
- SCL (Serial Clock) and SDA (Serial Data)
### Does I2C require pullup resistors?
- Yes
### What is the logical levels of SCL and SDA in the normal state?
- Both logical levels are set to high.
### What is the logical levels of SCL and SDA in the start condition?
- The start condition is set when the SDA logical level transitions from high to low. The SCL logical level must be high.
### What is the logical levels of SCL and SDA in the stop condition?
- The stop condition is set when the SDA logical level transitions from low to high. The SCL logical level must be high
### What is the transfer rate in fast mode?
- 400 kbit/s
### What is the transfer rate in high-speed mode?
- 3.4 Mbit/s
### What is OLA15?
- OLA15 is, for embedded systems a "test" we will have to pass to be admittet for the final exam.
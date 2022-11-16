from machine import ADC, Pin
from utime import sleep

in_pin = ADC(26)
conversion_factor = 3.3 / 65535
low, high = 750, 34900

while True:
    raw = in_pin.read_u16()
    volts = raw * conversion_factor
    percentage = (int(((raw - low) * 100) / (high - low)))
    print('Raw: {} '.format(raw), 'Voltage {:.1f}V'.format(volts),'Percentage: {}%'.format(percentage))
    sleep(1) 



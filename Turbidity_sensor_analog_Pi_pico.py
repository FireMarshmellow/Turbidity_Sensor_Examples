#   __  __      _ _               ______ _
#  |  \/  |    | | |             |  ____(_)
#  | \  / | ___| | | _____      _| |__   _ _ __ ___
#  | |\/| |/ _ \ | |/ _ \ \ /\ / /  __| | | '__/ _ \
#  | |  | |  __/ | | (_) \ V  V /| |    | | | |  __/
#  |_|  |_|\___|_|_|\___/ \_/\_/ |_|    |_|_|  \___|
#  @Mellow_labs
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



# Teplomer s DS18B20

import machine, onewire, ds18x20, time
from machine import Pin, SoftI2C
from machine_i2c_lcd import I2cLcd


# Define the LCD I2C address and dimensions
I2C_ADDR = 0x27
I2C_NUM_ROWS = 4
I2C_NUM_COLS = 20

# Initialize I2C and LCD objects
i2c = SoftI2C(sda=Pin(21), scl=Pin(22), freq=400000)

devices = i2c.scan()
if len(devices) == 0:
    print("Ziadne i2c zariadenie!")
else:
    print('i2c zariadenia nájdené:',len(devices))
for device in devices:
    print("Hexa adresa: ",hex(device))

lcd = I2cLcd(i2c, I2C_ADDR, I2C_NUM_ROWS, I2C_NUM_COLS)

lcd.putstr("Teplomer pracuje. :)")
time.sleep(4)

# Initialize DS18x20 devices

ds_pin = machine.Pin(2)
ds_sensor = ds18x20.DS18X20(onewire.OneWire(ds_pin))

roms = ds_sensor.scan()
print('Nájdené DS zariadenia: ', roms)

while True:
    lcd.clear()
    ds_sensor.convert_temp()
    time.sleep_ms(1500)
    i = 0
    for rom in roms:
       i = i + 1
       print("")
       print("Poradie senzora:", i)
       print(rom)
       temperature = ds_sensor.read_temp(rom)
       print(temperature)
       lcd.move_to(0, i-1)
       lcd.putstr("Teplota " + str(i) + ": " + str(temperature) )
       # Display two different messages on different lines
       # By default, it will start at (0,0) if the display is empty
       time.sleep(2)
   


from machine import RTC
from machine import I2C, Pin
from machine import Pin, PWM
from pico_i2c_lcd import I2cLcd
import utime
import machine
#===============================================================

I2C_ADDR  =  0x27
I2C_NUM_ROWS = 4
I2C_NUM_COLS = 20

i2c = I2C(sda=Pin(21), scl=Pin(22), freq=100000)
#Configuración LCD
lcd = I2cLcd(i2c, I2C_ADDR, I2C_NUM_ROWS, I2C_NUM_COLS)

#==============================================================



rtc = RTC()
rtc.datetime((2022, 4, 26, 0, 12, 0, 0, 0))

#=========================================================================

def horadisplay():
    while True:
        utime.sleep(0.5)
        lcd.move_to(0,0)
        lcd.putstr("Pet Feeder")
        a = rtc.datetime()
        hora = ("hora: " +str(a[4]) +":"+str(a[5])+":"+str(a[6]))
        print(hora)
    
        #lcd.message("IP"+rede[0], 2)
        lcd.move_to(0,1)
        lcd.putstr(hora+"  ")
        utime.sleep(0.5)




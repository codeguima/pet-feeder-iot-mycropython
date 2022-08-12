#---ATP JHONNY GUIMARAES---iot-----------------------------------------

import machine
import esp
import micropython
import network
import time
import utime
import gc
import ufirebase as firebase
gc.collect()
#----------------------------------------------------------------------
from time import sleep
from wifi import conecta
from machine import I2C, Pin
from machine import Pin, PWM
from lcd_api import LcdApi
from pico_i2c_lcd import I2cLcd
from lcd_main import main
from hora import horadisplay

#----------------------------------------------------------------------
# Imprime na tela configurações iniciais
#--------------------------------------------------------------------

I2C_ADDR  =  0x27
I2C_NUM_ROWS = 4
I2C_NUM_COLS = 20

i2c = I2C(sda=Pin(21), scl=Pin(22), freq=100000)
#Configuración LCD
lcd = I2cLcd(i2c, I2C_ADDR, I2C_NUM_ROWS, I2C_NUM_COLS)

main()#função importada da lcd_main
lcd.clear()
utime.sleep(2)

#--------------------------------------------------------------------
#Conecta Wifi
#--------------------------------------------------------------------

lcd.putstr('Conectando wifi...')
station = conecta('rede', 'senha')
utime.sleep(2)
lcd.clear()


if not station.isconnected():
    lcd.putstr('Não Conectado')
    utime.sleep(2)
    lcd.clear()
    
else:
    lcd.putstr('Conectado!!')
    utime.sleep(2)
    lcd.clear()
    
    
#----------------------------------------------------------

while True:
    try:
        motor = firebase.get('endereço de retorno de dados da nuvem 'GET')
        print(motor)
        if motor == 1:
            rele = (machine.Pin(2, machine.Pin.OUT))
            rele.value(1)
            lcd.putstr('Alimentando...')
            utime.sleep(1)
            rele.value(0)
            utime.sleep(2)
            lcd.clear()
        if motor == 0:
            lcd.putstr('Aguardando...')
            horadisplay()

        utime.sleep(2)
        lcd.clear()

  
    except KeyboardInterrupt:
        lcd.putstr('Ctrl-C pressionado!!!  O ESP32 foi desconectado da rede')
        utime.sleep(2)
        lcd.clear()
        client.disconnect()
        sys.exit()
        
    except OSError as e:
        restart_and_reconnect()
#---------------------------------------------------------------------------------------------------

        
        
        
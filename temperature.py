# lire la température
from machine import ADC
# 3.3 volts pour lecture 2^^16 - 1
# conversion_factor = 3.3 / (65535)

from ws2812 import WS2812
import utime
import machine
power = machine.Pin(25,machine.Pin.OUT)
power.value(0)
led = WS2812(23,1)#WS2812(pin_num,led_count)

# clignote x fois

def blink(x):  
    for i in range(x) :
        power.value(1)
        time.sleep(0.1)
        power.value(0)
        time.sleep(0.1)
    utime.sleep(1)
        
blink(5)

# roue de couleur de rouge > vert > bleu
for pos in range (255):
    led.pixels_fill(led.wheel(pos))
    led.pixels_show()
    print (pos)
    utime.sleep(0.01)

while True:
    sensor_temp = ADC(4)
    temperature = sensor_temp.read_u16() * 3.3 / (65535)  
    temperature = 15 + (0.706 - temperature )/0.001721
    print (temperature)
    pos = (int (temperature -10 )) % 10
    print (pos)
    blink(pos) # clignote pos fois
    led.pixels_fill(led.wheel(pos))
    led.pixels_show()
# lire la température
from machine import ADC
# 3.3 volts pour lecture 2^^16 - 1
# conversion_factor = 3.3 / (65535)

from ws2812 import WS2812
import utime
import machine

led = WS2812(16,1)#WS2812(pin_num,led_count)

# clignote x fois

def blink(t):
    u = (int (t -10 )) % 10 # unités
    d = (int (t -10 )) # dizaines
    for i in range(u) :
        led.pixels_fill(led.wheel(d * 10))
        led.pixels_show()
        utime.sleep(0.1)
        led.pixels_fill(led.wheel(u))
        led.pixels_show()
        utime.sleep(0.1)
    utime.sleep(1)
        
blink(5)

# roue de couleur de rouge > vert > bleu
for pos in range (255):
    led.pixels_fill(led.wheel(pos))
    led.pixels_show()
    utime.sleep(0.001)

while True:
    sensor_temp = ADC(4)
    temperature = sensor_temp.read_u16() * 3.3 / (65535)  
    temperature = 15 + (0.706 - temperature )/0.001721
    print (temperature)
    pos = (int (temperature -10 )) % 10
    print (pos)
    blink(temperature) # clignote pos fois
    led.pixels_fill(led.wheel(pos))
    led.pixels_show()
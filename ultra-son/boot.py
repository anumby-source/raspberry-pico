from ws2812 import WS2812
import utime
import machine
power = machine.Pin(2,machine.Pin.OUT)
power.value(0)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 150, 0)
GREEN = (0, 255, 0)
CYAN = (0, 255, 255)
BLUE = (0, 0, 255)
PURPLE = (180, 0, 255)
BRUN = (180, 0, 255)
RED = (255, 0, 0)
ORANGE = (255,0,150)
WHITE = (255, 255, 255)
COLORS = (BLACK, BRUN, RED, ORANGE, YELLOW, GREEN,  BLUE, CYAN, PURPLE, WHITE)

led = WS2812(23,1)#WS2812(pin_num,led_count)


print("Beautiful color")
for color in COLORS:
        led.pixels_fill(color)
        led.pixels_show()
        utime.sleep(0.2)
        
         # roue de couleur de rouge > vert > bleu
for pos in range (255):
     led.pixels_fill(led.wheel(pos))
     led.pixels_show()
     
     
        
from machine import Pin, time_pulse_us
import time

SOUND_SPEED=340 # Vitesse du son dans l'air
TRIG_PULSE_DURATION_US=10


echo_pin = Pin(21, Pin.IN)

trig_pin = Pin(20, Pin.OUT)

plus = Pin(19, Pin.OUT)


plus.value(1)



while True:
 # Prepare le signal
 trig_pin.value(0)
 time.sleep_us(5)
 # Créer une impulsion de 10 µs
 trig_pin.value(1)
 time.sleep_us(TRIG_PULSE_DURATION_US)
 trig_pin.value(0)

 ultrason_duration = time_pulse_us(echo_pin, 1, 30000) # Renvoie le temps de propagation de l'onde (en µs)
 if ultrason_duration < 0 : ultrason_duration = 30000
 print(f"Distance : {ultrason_duration} us")
 distance_cm = SOUND_SPEED * ultrason_duration / 20000
 led.pixels_fill(led.wheel(int (distance_cm) % 128))
 led.pixels_show()

 print(f"Distance : {distance_cm} cm")
 time.sleep_ms(500)

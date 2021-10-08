# clignote


from machine import Pin
import time

led = Pin(25, Pin.OUT)

ledR = Pin(2, Pin.OUT)
ledR.value(1)

ledG = Pin(3, Pin.OUT)
ledG.value(1)

ledB = Pin(4, Pin.OUT)
ledB.value(1)

while True:
    led.value(1)
    ledG.toggle()
    ledR.toggle()
    time.sleep(1)
    led.value(0)
    ledR.toggle()
    time.sleep(1)




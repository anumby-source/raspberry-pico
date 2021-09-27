from machine import Pin
led = Pin(25, Pin.OUT)
led.value(1)
i = 0
ledR = Pin(2, Pin.OUT)
ledR.value(1)

ledG = Pin(3, Pin.OUT)
ledG.value(1)

ledB = Pin(4, Pin.OUT)
ledB.value(1)


from machine import Pin, Timer
led = Pin(25, Pin.OUT)
timer = Timer()

def blink(timer):
    led.toggle()
    ledG.toggle()
    if((i / 2) % 2):
        ledR.toggle()

timer.init(freq=2.5, mode=Timer.PERIODIC, callback=blink)

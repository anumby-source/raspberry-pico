import time
import board
import digitalio
import busio
import usb_midi
import time

import adafruit_midi
from adafruit_midi.note_off import NoteOff
from adafruit_midi.note_on import NoteOn


class Button:
    """
    Midi Key Button
    """

    def __init__(self, pin, notes):
        self.status = False
        self.notes = notes
        self.io_ = digitalio.DigitalInOut(pin)
        self.io_.switch_to_input(pull=digitalio.Pull.UP)

    def value(self):
        return self.io_.value


#
# 12 touches
#
Buttons = []

Buttons.append(Button(board.GP2, [60]))   # middle C
Buttons.append(Button(board.GP3, [61]))   # 
Buttons.append(Button(board.GP4, [62]))   # 
Buttons.append(Button(board.GP5, [63]))   # 
Buttons.append(Button(board.GP6, [64]))   # 
Buttons.append(Button(board.GP7, [65]))   # 
Buttons.append(Button(board.GP8, [66]))   # 
Buttons.append(Button(board.GP9, [67]))   # 
Buttons.append(Button(board.GP10, [68]))   # 
Buttons.append(Button(board.GP11, [69]))   # 
Buttons.append(Button(board.GP12, [70]))   # 
Buttons.append(Button(board.GP13, [71]))   # 
# Set USB MIDI up on channel 0
midi = adafruit_midi.MIDI(midi_out=usb_midi.ports[1], out_channel=0)

# key press LED
led = digitalio.DigitalInOut(board.GP25)
led.direction = digitalio.Direction.OUTPUT


while True:

    # key press changing?
    is_change = False
    for button in Buttons:
        if button.value() != button.status:
            is_change = True
            break

    if is_change is False:
        # nothing todo
        time.sleep(0.1)
        continue

    is_press = False
    for button in Buttons:
        if button.value() != button.status:
            # press or relase key
            if button.value():
                # LED off and sound off
                for note in button.notes:
                    midi.send(NoteOff(note, 0))
            else:
                # LED on and sound on, velocity=100
                is_press = True
                for note in button.notes:
                    time.sleep(0.11)
                    midi.send(NoteOn(note, 100))
        button.status = button.value()

    led.value = is_press

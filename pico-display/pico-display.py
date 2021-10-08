https://github.com/pimoroni/pimoroni-pico/tree/main/micropython/examples/pico_display

---------------------------
import utime
import picodisplay

# Initialise Picodisplay with a bytearray display buffer
buf = bytearray(picodisplay.get_width() * picodisplay.get_height() * 2)
picodisplay.init(buf)
picodisplay.set_backlight(1.0)

picodisplay.set_pen(255, 0, 0)                    # Set a red pen
picodisplay.clear()                               # Clear the display buffer
picodisplay.set_pen(255, 255, 255)                # Set a white pen
picodisplay.text("pico anumby", 10, 10, 240, 6)  # Add some text
picodisplay.update()                              # Update the display with our changes

   # Set the RGB LED to blue

while True:
    utime.sleep(1) # inverse RGB
    picodisplay.set_led(0, 255, 0)  # Set the RGB LED to green
    if picodisplay.is_pressed(picodisplay.BUTTON_A) :
        picodisplay.set_led(255, 255, 255)  # Set the RGB LED to green
    utime.sleep(1) # inverse RGB
    picodisplay.set_led(255, 0, 0)  # Set the RGB LED to green
    utime.sleep(1) # inverse RGB
    picodisplay.set_led(0, 0, 255)  # Set the RGB LED to green




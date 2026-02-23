# Traduit un texte en morse et affiche les caractères traduits au fur et à mesure de l'éxécution.
# LCD  GROVE RGB Blacklight I2C
# LED Néopixel
# Taper le texte lettre et chiffre uniquement dans la console puis RUN.
# Ecrit par Franco Pontiggia/Gémini/ChatGpt fev2026

import board 
import neopixel
import pwmio
import busio
import time

# ------------------- Config Matériel -------------------
pixel = neopixel.NeoPixel(board.GP23, 1, brightness=1.0, auto_write=False)
buzzer = pwmio.PWMOut(board.GP15, duty_cycle=0, frequency=850) # =====Sortie HP GP15
i2c = busio.I2C(board.GP21, board.GP20)  #============================SCL=GP21, SDA=GP20

LCD_ADDR = 0x3E
RGB_ADDR = 0x62

lcd_cols = 16
lcd_rows = 2

# ------------------- Fonctions LCD -------------------
def i2c_write(addr, data):
    while not i2c.try_lock():
        pass
    i2c.writeto(addr, bytes(data))
    i2c.unlock()

def cmd(c):
    i2c_write(LCD_ADDR, [0x80, c])

def data(d):
    i2c_write(LCD_ADDR, [0x40, d])

def set_rgb(r,g,b):
    i2c_write(RGB_ADDR, [0x00,0x00])
    i2c_write(RGB_ADDR, [0x01,0x00])
    i2c_write(RGB_ADDR, [0x08,0xAA])
    i2c_write(RGB_ADDR, [0x04,r])
    i2c_write(RGB_ADDR, [0x03,g])
    i2c_write(RGB_ADDR, [0x02,b])

def lcd_clear():
    cmd(0x01)
    time.sleep(0.05)
    cmd(0x80)

def lcd_print(message):
    lcd_clear()
    for c in message:
        data(ord(c))

# ------------------- Initialisation LCD  GROVE RGB Blacklight I2C--------
time.sleep(0.1)
cmd(0x38)
cmd(0x39)
cmd(0x14)
cmd(0x78)
cmd(0x5E)
cmd(0x6D)
time.sleep(0.2)
cmd(0x38)
cmd(0x0F)  # display on, cursor on, blink on
cmd(0x01)
time.sleep(0.05)
cmd(0x80)

set_rgb(0,0,255)

# ------------------- Paramètres Morse réglages: longueur point trait blanc -------------------
DOT = 0.1
DASH = DOT * 3
SYMBOL_PAUSE = DOT
LETTER_PAUSE = DOT * 3
WORD_PAUSE = DOT * 7

MORSE_CODE = {
    "A": ".-", "B": "-...", "C": "-.-.", "D": "-..",
    "E": ".", "F": "..-.", "G": "--.", "H": "....",
    "I": "..", "J": ".---", "K": "-.-", "L": ".-..",
    "M": "--", "N": "-.", "O": "---", "P": ".--.",
    "Q": "--.-", "R": ".-.", "S": "...", "T": "-",
    "U": "..-", "V": "...-", "W": ".--", "X": "-..-",
    "Y": "-.--", "Z": "--..",
    "0": "-----", "1": ".----", "2": "..---", "3": "...--",
    "4": "....-", "5": ".....", "6": "-....", "7": "--...",
    "8": "---..", "9": "----."
}

# ------------------- Fonctions Morse -------------------
def blink(symbol):
    duration = DOT if symbol == "." else DASH
    # LED + buzzer
    pixel[0] = (0,0,255)
    pixel.show()
    buzzer.duty_cycle = 32768
    time.sleep(duration)
    # LED + buzzer off
    pixel[0] = (0,0,0)
    pixel.show()
    buzzer.duty_cycle = 0
    time.sleep(SYMBOL_PAUSE)

def send_morse(message):
    lcd_clear()
    lcd_line = ""
    for word in message.split(" "):
        for letter in word:
            morse = MORSE_CODE.get(letter.upper())
            if morse:
                # Afficher lettre sur LCD progressivement
                lcd_line += letter.upper()
                if len(lcd_line) > lcd_cols*lcd_rows:
                    lcd_line = lcd_line[-lcd_cols*lcd_rows:]
                lcd_print(lcd_line)
                # Morse
                for symbol in morse:
                    # couleur LCD selon symbole
                    if symbol == ".":
                        set_rgb(0,0,255)  # bleu
                    else:
                        set_rgb(255,0,0)  # rouge
                    blink(symbol)
                time.sleep(LETTER_PAUSE - SYMBOL_PAUSE)
        time.sleep(WORD_PAUSE - LETTER_PAUSE)
        lcd_line += " "
        lcd_print(lcd_line)

# ----- Programme principal attend un message lettre et chiffre au clavier ------------
print("Tape un message (lettres/chiffres) et Entrée :")
try:
    while True:
        message = input("> ")
        send_morse(message)
        print("Message transmis en Morse !")

except KeyboardInterrupt:
    pixel.fill((0,0,0))
    pixel.show()
    buzzer.duty_cycle = 0
    lcd_clear()
    print("Programme arrêté.")


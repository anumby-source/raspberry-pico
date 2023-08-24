#include <NeoPixelConnect.h>

#define ItsyBitsyRP2040

// Original value of 255 is WAY too bright - worryingly so.
// 32 is okay, but a bit bright for dim lighting, close up.
//define MAX_INTENSITY 32
#define MAX_INTENSITY 8

// https://github.com/MrYsLab/NeoPixelConnect

// Original: "Create an instance of NeoPixelConnect and initialize it
// to use GPIO pin 4 (D12) as the control pin, for a string
// of 8 neopixels. Name the instance p

// RP2040-Zero : one builtin WS2812, on GP16
// Adafruit ItsyBitsy RP2040 : one builtin WS2812, on GP17, but power
// on GP16, active high



NeoPixelConnect p(23, 1);

// this array will hold a pixel number and the rgb values for the
// randomly generated pixel values
uint8_t random_pixel_setting[4];

// select a random pixel number in the string
uint8_t get_pixel_number(){
//    return((uint8_t)random(0,7));
  return 0;   // There is only one
}

// select a random intensity
uint8_t get_pixel_intensity(){
// Original value of 255 is WAY too bright - worryingly.
//    return((uint8_t)random(0,255));
    return((uint8_t)random(0, MAX_INTENSITY));
}

void get_random_pixel_and_color(){
    random_pixel_setting[0] = get_pixel_number();
    random_pixel_setting[1] = get_pixel_intensity();
    random_pixel_setting[2] = get_pixel_intensity();
    random_pixel_setting[3] = get_pixel_intensity();
}

void setup(){
    Serial.begin(115200);
    delay(2000);
    Serial.println("In setup");

}

void loop(){

    // get a pixel number
    get_random_pixel_and_color();

    // display the randomly assigned pixel and color
    p.neoPixelSetValue(random_pixel_setting[0], random_pixel_setting[1],
                       random_pixel_setting[2],
                       random_pixel_setting[3], true);
    delay(100);
    // clear all pixels
    p.neoPixelClear();
    delay(100);
}

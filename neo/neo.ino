#include <NeoPixelConnect.h>



// Original value of 255 is WAY too bright - worryingly so.
// 32 is okay, but a bit bright for dim lighting, close up.
//define MAX_INTENSITY 32
#define MAX_INTENSITY 8

// https://github.com/MrYsLab/NeoPixelConnect


NeoPixelConnect strip(23, 1);

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
    for( int i=0; i<256; i++){
      Wheel(i);
      delay(10);
    }
}

void loop(){

    // get a pixel number
    get_random_pixel_and_color();

    // display the randomly assigned pixel and color
    strip.neoPixelSetValue(random_pixel_setting[0], random_pixel_setting[1],
                       random_pixel_setting[2],
                       random_pixel_setting[3], true);
    delay(100);
    // clear all pixels
    strip.neoPixelClear();
    delay(100);
}
void Color(byte x,byte y,byte z) {
    strip.neoPixelSetValue(0, x,y,z, true);
}

// Input a value 0 to 255 to get a color value.
// The colours are a transition r - g - b - back to r.
void Wheel(byte WheelPos) {
  if(WheelPos < 85) {
   return Color(WheelPos * 3, 255 - WheelPos * 3, 0);
  } else if(WheelPos < 170) {
   WheelPos -= 85;
   return Color(255 - WheelPos * 3, 0, WheelPos * 3);
  } else {
   WheelPos -= 170;
   return Color(0, WheelPos * 3, 255 - WheelPos * 3);
  }
}

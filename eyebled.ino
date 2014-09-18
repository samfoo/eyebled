#include <LPD8806.h>
#include "SPI.h"

int nLEDs = 160;
int dataPin  = 2;
int clockPin = 3;
LPD8806 strip = LPD8806(nLEDs, dataPin, clockPin);

uint32_t red = strip.Color(127, 0, 0);
uint32_t green = strip.Color(0, 127, 0);
uint32_t blue = strip.Color(0, 0, 127);
uint32_t yellow = strip.Color(127, 127, 0);

#define NONE          0
#define PING         '!'
#define PONG         '?'
#define GREEN        'G'
#define BUILDING_OK  'B'
#define BUILDING_BAD 'C'
#define RED          'R'

int nowShowing = NONE;

void setup() {
  strip.begin();
  strip.show();

  Serial.begin(9600);
}

void candyStripe(uint32_t a, uint32_t b, uint8_t len, uint8_t wait) {
  for(int idx = 0; idx < (len * 2); idx++) {
    for(int i = 0; i < strip.numPixels(); i++) {
      uint32_t p = (i + idx) % strip.numPixels();
      uint32_t c = (i / len) % 2 ? a : b;

      strip.setPixelColor(p, c);
    }
    strip.show();
    delay(wait);
  }
}

void colorSolid(uint32_t c) {
  for(int i = 0; i < strip.numPixels(); i++) {
     strip.setPixelColor(i, c);
  }
  strip.show();
}

void colorFlash(uint32_t a, uint8_t wait) {
  colorSolid(a);
  delay(wait);
  colorSolid(strip.Color(0, 0, 0));
  delay(wait);
}

int getCommand() {
  if (Serial.available() > 0) {
    int in = Serial.read();
    if (in == -1) return NONE;

    switch(in) {
      case PING:
        Serial.write(PONG);
        break;
      case GREEN:
      case BUILDING_OK:
      case BUILDING_BAD:
      case RED:
        return in;
    }
  }

  return NONE;
}

void loop() {
  int c = getCommand();
  nowShowing = c || nowShowing;

  switch(nowShowing) {
    case NONE:
      colorSolid(yellow);
      break;

    case GREEN:
      colorSolid(green);
      break;

    case BUILDING_OK:
      candyStripe(red, blue, 4, 25);
      break;

    case BUILDING_BAD:
      candyStripe(red, green, 4, 25);
      break;

    case RED:
      colorFlash(red, 1000);
      break;
  }
}


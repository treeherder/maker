#include <Arduino.h>

#define led_1 9
#define led_2 8
#define led_3 7

void setup()
{
  pinMode(led_1, OUTPUT);
  pinMode(led_2, OUTPUT);
  pinMode(led_3, OUTPUT);
}

int rgb(int red, int green, int blue)
{
  analogWrite(led_1, red);
  return 0; 
}

void loop()
{
  rgb(255,0,0);
}

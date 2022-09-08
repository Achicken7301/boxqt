// Potentiometer is connected to GPIO 34 (Analog ADC1_CH6)
const int potPin = 2;
#include "SparkFun_LIS331.h"
#include <Wire.h>

LIS331 xl;
// variable for storing the potentiometer value
int potValue = 0;

void setup() {
  pinMode(potPin, INPUT);
  Wire.begin();
  xl.setI2CAddr(0x19);
  xl.begin(LIS331::USE_I2C);
  Serial.begin(115200);
}

void loop() {
  // Reading potentiometer value
  int potValue = analogRead(potPin);
  
  int16_t x, y, z;
  xl.readAxes(x, y, z);  // The readAxes() function transfers the

  //  float LIS331::convertToG(int maxScale, int reading)
  //{
  //  float result = (float(maxScale) * float(reading))/2047;
  //  return result;
  //}
  //  200 = maxScale
  Serial.print(xl.convertToG(100, x)); Serial.print(" ");
  Serial.print(xl.convertToG(100, y)); Serial.print(" ");
  Serial.print(xl.convertToG(100, z)); Serial.print(" ");
  Serial.println(potValue);
}

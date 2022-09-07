#include "SparkFun_LIS331.h"
#include <Wire.h>

LIS331 xl;

void setup()
{
  Wire.begin();
  xl.setI2CAddr(0x19);
  xl.begin(LIS331::USE_I2C);
  Serial.begin(115200);
}

void loop()
{
  int16_t x, y, z;
  xl.readAxes(x, y, z);  // The readAxes() function transfers the

  //  float LIS331::convertToG(int maxScale, int reading)
  //{
  //  float result = (float(maxScale) * float(reading))/2047;
  //  return result;
  //}
  //  200 = maxScale
  Serial.print(xl.convertToG(200, x)); Serial.print(" ");
  Serial.print(xl.convertToG(200, y)); Serial.print(" ");
  Serial.println(xl.convertToG(200, z));


}

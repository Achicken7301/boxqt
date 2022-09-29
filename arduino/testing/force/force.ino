// Potentiometer is connected to GPIO 34 (Analog ADC1_CH6)
const int potPin = 2;
#include "SparkFun_LIS331.h"
#include <Wire.h>
#include "BluetoothSerial.h"

#if !defined(CONFIG_BT_ENABLED) || !defined(CONFIG_BLUEDROID_ENABLED)
#error Bluetooth is not enabled! Please run `make menuconfig` to and enable it
#endif

BluetoothSerial SerialBT;

LIS331 xl;
// variable for storing the potentiometer value
int potValue = 0;

void setup() {
  pinMode(potPin, INPUT);
  SerialBT.begin("DeviceOnHand"); //Bluetooth device name
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
  //  100 = maxScale
  
//  Serial.print(millis()); Serial.print(" ");
//  Serial.print(xl.convertToG(100, x)); Serial.print(" ");
//  Serial.print(xl.convertToG(100, y)); Serial.print(" ");
//  Serial.print(xl.convertToG(100, z)); Serial.print(" ");
//  Serial.println(potValue);
  SerialBT.print(millis()); SerialBT.print(" ");
  SerialBT.print(xl.convertToG(100, x)); SerialBT.print(" ");
  SerialBT.print(xl.convertToG(100, y)); SerialBT.print(" ");
  SerialBT.print(xl.convertToG(100, z)); SerialBT.print(" ");
  SerialBT.println(potValue);
}

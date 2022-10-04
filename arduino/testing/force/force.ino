// Potentiometer is connected to GPIO 34 (Analog ADC1_CH6)
const int potPin = 2;
#include "BluetoothSerial.h"

#if !defined(CONFIG_BT_ENABLED) || !defined(CONFIG_BLUEDROID_ENABLED)
#error Bluetooth is not enabled! Please run `make menuconfig` to and enable it
#endif

BluetoothSerial SerialBT;
int potValue = 0;

void setup() {
  pinMode(potPin, INPUT);
  SerialBT.begin("DeviceOnHand"); //Bluetooth device name
  Serial.begin(115200);
}

void loop() {
  // Reading potentiometer value
  int potValue = analogRead(potPin);
  Serial.println(potValue);
  SerialBT.println(potValue);
  delay(2);
}

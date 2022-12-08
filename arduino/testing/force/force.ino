#include "BluetoothSerial.h"

#if !defined(CONFIG_BT_ENABLED) || !defined(CONFIG_BLUEDROID_ENABLED)
#error Bluetooth is not enabled! Please run `make menuconfig` to and enable it
#endif

#if !defined(CONFIG_BT_SPP_ENABLED)
#error Serial Bluetooth not available or not enabled. It is only available for the ESP32 chip.
#endif

BluetoothSerial SerialBT;

const int potPin = A0;

void setup() {
  pinMode(potPin, INPUT);
  Serial.begin(115200);
  SerialBT.begin("DeviceOnHand"); //Bluetooth device name
}

void loop() {
  SerialBT.printf("%d\n", analogRead(potPin));
  Serial.printf("%d\n", analogRead(potPin));
}

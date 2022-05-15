// Basic demo for accelerometer readings from Adafruit MPU6050

#include <Adafruit_MPU6050.h>
#include <Adafruit_Sensor.h>
#include <Wire.h>

Adafruit_MPU6050 mpu;

#include "BluetoothSerial.h"

#if !defined(CONFIG_BT_ENABLED) || !defined(CONFIG_BLUEDROID_ENABLED)
#error Bluetooth is not enabled! Please run `make menuconfig` to and enable it
#endif

BluetoothSerial SerialBT;

void setup(void) {
  Serial.begin(115200);
  SerialBT.begin("IMUonBag"); //Bluetooth device name
  SerialBT.println("Start sending data");
  Serial.println("The device started, now you can pair it with bluetooth!");
  while (!Serial) {
    delay(10); // will pause Zero, Leonardo, etc until serial console opens
  }

  // Try to initialize!
  if (!mpu.begin()) {
    Serial.println("Failed to find MPU6050 chip");
    while (1) {
      delay(10);
    }
  }

  mpu.setAccelerometerRange(MPU6050_RANGE_16_G);
  mpu.setGyroRange(MPU6050_RANGE_250_DEG);
  mpu.setFilterBandwidth(MPU6050_BAND_21_HZ);
  Serial.println("");
  delay(100);
}

void loop() {

  /* Get new sensor events with the readings */
  sensors_event_t a, g, temp;
  mpu.getEvent(&a, &g, &temp);

  /* Print out the values */
  Serial.print("AccelX:");
  Serial.print(a.acceleration.x);

  Serial.print(" ");
  Serial.print("AccelY:");
  Serial.print(a.acceleration.y);

  Serial.print(" ");
  Serial.print("AccelZ:");
  Serial.print(a.acceleration.z);

  Serial.print(", ");
  Serial.print("GyroX:");
  Serial.print(g.gyro.x);

  Serial.print(" ");
  Serial.print("GyroY:");
  Serial.print(g.gyro.y);

  Serial.print(" ");
  Serial.print("GyroZ:");
  Serial.print(g.gyro.z);

  Serial.println("");
  //  Bluetooth
  SerialBT.print(a.acceleration.x);
  SerialBT.print(" ");
  SerialBT.print(a.acceleration.y);
  SerialBT.print(" ");
  SerialBT.print(a.acceleration.z);
  SerialBT.print(" ");
  SerialBT.print(g.gyro.x);
  SerialBT.print(" ");
  SerialBT.print(g.gyro.y);
  SerialBT.print(" ");
  SerialBT.println(g.gyro.z);
//  delay(10);
}
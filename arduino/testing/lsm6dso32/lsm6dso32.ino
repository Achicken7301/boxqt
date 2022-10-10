// Basic demo for accelerometer & gyro readings from Adafruit
// LSM6DSO32 sensor

#include <Adafruit_LSM6DSO32.h>
#include <Wire.h>
// For SPI mode, we need a CS pin
#define LSM_CS 10
// For software-SPI mode we need SCK/MOSI/MISO pins
#define LSM_SCK 13
#define LSM_MISO 12
#define LSM_MOSI 11
#include "BluetoothSerial.h"

#if !defined(CONFIG_BT_ENABLED) || !defined(CONFIG_BLUEDROID_ENABLED)
#error Bluetooth is not enabled! Please run `make menuconfig` to and enable it
#endif

BluetoothSerial SerialBT;
Adafruit_LSM6DSO32 dso32;
void setup(void) {
  SerialBT.begin("DeviceOnBagLSM6DSO32"); //Bluetooth device name
  Serial.begin(115200);
  while (!Serial) {
    delay(10); // will pause Zero, Leonardo, etc until serial console opens
  }

  Serial.println("Adafruit LSM6DSO32 test!");
  if (!dso32.begin_I2C(0x6B)) {
    // if (!dso32.begin_SPI(LSM_CS)) {
    // if (!dso32.begin_SPI(LSM_CS, LSM_SCK, LSM_MISO, LSM_MOSI)) {
    Serial.println("Failed to find LSM6DSO32 chip");
    while (1) {
      delay(10);
    }
  }

//  Serial.println("LSM6DSO32 Found!");

  dso32.setAccelRange(LSM6DSO32_ACCEL_RANGE_32_G);
  dso32.setGyroRange(LSM6DS_GYRO_RANGE_2000_DPS );
  dso32.setGyroDataRate(LSM6DS_RATE_6_66K_HZ);
  dso32.setAccelDataRate(LSM6DS_RATE_6_66K_HZ);
}

void loop() {

  //  /* Get a new normalized sensor event */
  sensors_event_t accel;
  sensors_event_t gyro;
  sensors_event_t temp;
  dso32.getEvent(&accel, &gyro, &temp);

  //  Serial.print("\t\tTemperature ");
  //  Serial.print(temp.temperature);
  //  Serial.println(" deg C");

  /* Display the results (acceleration is measured in m/s^2) */
  //  Serial.print("\t\tAccel X: ");
  //  Serial.print(accel.acceleration.x);
  //  Serial.print(" \tY: ");
  //  Serial.print(accel.acceleration.y);
  //  Serial.print(" \tZ: ");
  //  Serial.print(accel.acceleration.z);
  //  Serial.println(" m/s^2 ");

  /* Display the results (rotation is measured in rad/s) */
  //  Serial.print("\t\tGyro X: ");
  //  Serial.print(gyro.gyro.x);
  //  Serial.print(" \tY: ");
  //  Serial.print(gyro.gyro.y);
  //  Serial.print(" \tZ: ");
  //  Serial.print(gyro.gyro.z);
  //  Serial.println(" radians/s ");
  //  Serial.println();

  //  delay(100);

  //  // serial plotter friendly format

  //  Serial.print(temp.temperature);
  //  Serial.print(",");
  
//  Serial.print(millis()); Serial.print(","); 
  Serial.print(accel.acceleration.x);
  Serial.print(","); Serial.print(accel.acceleration.y);
  Serial.print(","); Serial.print(accel.acceleration.z);
  Serial.print(",");

  Serial.print(gyro.gyro.x);
  Serial.print(","); Serial.print(gyro.gyro.y);
  Serial.print(","); Serial.print(gyro.gyro.z);
  Serial.println();

//  SerialBT.print(millis()); SerialBT.print(","); 
  SerialBT.write(accel.acceleration.x); SerialBT.write(","); 
  SerialBT.write(accel.acceleration.y); SerialBT.write(","); 
  SerialBT.write(accel.acceleration.z); SerialBT.write(",");

  SerialBT.write(gyro.gyro.x); SerialBT.write(","); 
  SerialBT.write(gyro.gyro.y); SerialBT.write(","); 
  SerialBT.write(gyro.gyro.z);
  SerialBT.println();
}

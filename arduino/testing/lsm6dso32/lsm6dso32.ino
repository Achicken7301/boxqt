#include <Adafruit_LSM6DSO32.h>
#include <Wire.h>
#include "BluetoothSerial.h"

// For SPI mode, we need a CS pin
#define LSM_CS    5
// For software-SPI mode we need SCK/MOSI/MISO pins
#define LSM_SCK   18
#define LSM_MISO  19
#define LSM_MOSI  23

#if !defined(CONFIG_BT_ENABLED) || !defined(CONFIG_BLUEDROID_ENABLED)
#error Bluetooth is not enabled! Please run `make menuconfig` to and enable it
#endif

BluetoothSerial SerialBT;
Adafruit_LSM6DSO32 dso32;

void setup(void) {
  SerialBT.begin("DeviceOnBag"); //Bluetooth device name
  Serial.begin(1000 * 1000);
  //  if (!dso32.begin_I2C(0x6B)) {
  // if (!dso32.begin_SPI(LSM_CS)) {
  if (!dso32.begin_SPI(LSM_CS, LSM_SCK, LSM_MISO, LSM_MOSI)) {
    Serial.println("Failed to find LSM6DSO32 chip");
    while (1) {
      delay(10);
    }
  }

  dso32.setAccelRange(LSM6DSO32_ACCEL_RANGE_32_G);
  dso32.setGyroRange(LSM6DS_GYRO_RANGE_2000_DPS );
  dso32.setGyroDataRate(LSM6DS_RATE_1_66K_HZ);
  dso32.setAccelDataRate(LSM6DS_RATE_1_66K_HZ);
}

void loop() {
  //  /* Get a new normalized sensor event */
  sensors_event_t accel;
  sensors_event_t gyro;
  sensors_event_t temp;
  dso32.getEvent(&accel, &gyro, &temp);
  Serial.printf("%.2f,%.2f,%.2f,%.2f,%.2f,%.2f\n", accel.acceleration.x, accel.acceleration.y, accel.acceleration.z, gyro.gyro.x, gyro.gyro.y, gyro.gyro.z);
  SerialBT.printf("%.2f,%.2f,%.2f,%.2f,%.2f,%.2f\n", accel.acceleration.x, accel.acceleration.y, accel.acceleration.z, gyro.gyro.x, gyro.gyro.y, gyro.gyro.z);

}

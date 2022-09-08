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

Adafruit_LSM6DSO32 dso32;
void setup(void) {
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

  Serial.println("LSM6DSO32 Found!");

  dso32.setAccelRange(LSM6DSO32_ACCEL_RANGE_32_G);
  Serial.print("Accelerometer range set to: ");
  switch (dso32.getAccelRange()) {
    case LSM6DSO32_ACCEL_RANGE_4_G:
      Serial.println("+-4G");
      break;
    case LSM6DSO32_ACCEL_RANGE_8_G:
      Serial.println("+-8G");
      break;
    case LSM6DSO32_ACCEL_RANGE_16_G:
      Serial.println("+-16G");
      break;
    case LSM6DSO32_ACCEL_RANGE_32_G:
      Serial.println("+-32G");
      break;
  }

  dso32.setGyroRange(LSM6DS_GYRO_RANGE_2000_DPS );
  Serial.print("Gyro range set to: ");
  switch (dso32.getGyroRange()) {
    case LSM6DS_GYRO_RANGE_125_DPS:
      Serial.println("125 degrees/s");
      break;
    case LSM6DS_GYRO_RANGE_250_DPS:
      Serial.println("250 degrees/s");
      break;
    case LSM6DS_GYRO_RANGE_500_DPS:
      Serial.println("500 degrees/s");
      break;
    case LSM6DS_GYRO_RANGE_1000_DPS:
      Serial.println("1000 degrees/s");
      break;
    case LSM6DS_GYRO_RANGE_2000_DPS:
      Serial.println("2000 degrees/s");
      break;
    case ISM330DHCX_GYRO_RANGE_4000_DPS:
      break; // unsupported range for the DSO32
  }
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

  Serial.print(temp.temperature);
  Serial.print(",");

  Serial.print(accel.acceleration.x);
  Serial.print(","); Serial.print(accel.acceleration.y);
  Serial.print(","); Serial.print(accel.acceleration.z);
  Serial.print(",");

  Serial.print(gyro.gyro.x);
  Serial.print(","); Serial.print(gyro.gyro.y);
  Serial.print(","); Serial.print(gyro.gyro.z);
  Serial.println();
  delay(10);
}
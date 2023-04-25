#include <Adafruit_LSM6DSO32.h>
#include <Wire.h>

#define BLUETOOTH_MODE 1

// For SPI mode, we need a CS pin
#define LSM_CS 5
// For software-SPI mode we need SCK/MOSI/MISO pins
#define LSM_SCK 18
#define LSM_MISO 19
#define LSM_MOSI 23

Adafruit_LSM6DSO32 dso32;

#if BLUETOOTH_MODE
#include "BluetoothSerial.h"

#if !defined(CONFIG_BT_ENABLED) || !defined(CONFIG_BLUEDROID_ENABLED)
#error Bluetooth is not enabled! Please run `make menuconfig` to and enable it
#endif

#if !defined(CONFIG_BT_SPP_ENABLED)
#error Serial Bluetooth not available or not enabled. It is only available for the ESP32 chip.
#endif

BluetoothSerial SerialBT;
#endif

int timer_counter = 0;
int timer_flag = 0;
int sampleRate = 1000;  // 1000Hz

#define CLOCK_TICK 1  //1ms

hw_timer_t* timer = NULL;


void setTimer(int duration) {
  timer_counter = duration / CLOCK_TICK;
  timer_flag = 0;
}

void timerRun() {
  if (timer_counter > 0) {
    timer_counter--;
    if (timer_counter <= 0) timer_flag = 1;
  }
}

void IRAM_ATTR onTimer() {
  timerRun();
}


void setup() {
#if BLUETOOTH_MODE
  SerialBT.begin("AcelGryro");  //Bluetooth device name
#endif

  Serial.begin(115200);
  pinMode(LED_BUILTIN, OUTPUT);

  //  Create timer 1
  timer = timerBegin(1, 80, true);                  //Begin timer with 1 MHz frequency (80MHz/80)
  timerAttachInterrupt(timer, &onTimer, true);      //Attach the interrupt to Timer1
  unsigned int timerFactor = 1000000 / sampleRate;  //Calculate the time interval between two readings, or more accurately, the number of cycles between two readings
  timerAlarmWrite(timer, timerFactor, true);        //Initialize the timer
  timerAlarmEnable(timer);

  setTimer(1000);

  //  if (!dso32.begin_I2C(0x6B)) {
  // if (!dso32.begin_SPI(LSM_CS)) {
  if (!dso32.begin_SPI(LSM_CS, LSM_SCK, LSM_MISO, LSM_MOSI)) {
    Serial.println("Failed to find LSM6DSO32 chip");
    while (1) {
      delay(10);
    }
  }

  dso32.setAccelRange(LSM6DSO32_ACCEL_RANGE_32_G);
  dso32.setGyroRange(LSM6DS_GYRO_RANGE_2000_DPS);

  dso32.setGyroDataRate(LSM6DS_RATE_1_66K_HZ);
  //  dso32.setGyroDataRate(LSM6DS_RATE_208_HZ);

  dso32.setAccelDataRate(LSM6DS_RATE_1_66K_HZ);
  //  dso32.setAccelDataRate(LSM6DS_RATE_208_HZ);
}


void loop() {
  sensors_event_t accel;
  sensors_event_t gyro;
  sensors_event_t temp;
  dso32.getEvent(&accel, &gyro, &temp);

  if (timer_flag == 1) {
    /*
      Given: f = 150Hz
      T = 1/f => 1/150 ~= 6
    */
    setTimer(6);
    //    digitalWrite(LED_BUILTIN, led_state);
    //    led_state = !led_state;
    Serial.printf("%.2f,%.2f,%.2f,%.2f,%.2f,%.2f\n", accel.acceleration.x, accel.acceleration.y, accel.acceleration.z, gyro.gyro.x, gyro.gyro.y, gyro.gyro.z);
#if BLUETOOTH_MODE
    SerialBT.printf("%.6f,%.6f,%.6f,%.6f,%.6f,%.6f\n", accel.acceleration.x, accel.acceleration.y, accel.acceleration.z, gyro.gyro.x, gyro.gyro.y, gyro.gyro.z);
    //    SerialBT.printf("%.2f,%.2f,%.2f,%.2f,%.2f,%.2f\n", accel.acceleration.x, accel.acceleration.y, accel.acceleration.z, gyro.gyro.x, gyro.gyro.y, gyro.gyro.z);
#endif
  }
}

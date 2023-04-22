#define BLUETOOTH_MODE 1

#define LOADCELL01_PIN 2
#define LOADCELL02_PIN 15

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

/*
  TIMER SETUP
*/

int timer_counter = 0;
int timer_flag = 0;
int sample_rate = 1000;

#define CLOCK_TICK 1

hw_timer_t* timer = NULL;


void setTimer(int duration) {  // duration (ms)
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
  Serial.begin(115200);

  //  Create timer 1
  timer = timerBegin(1, 80, true);              //Begin timer with 1 MHz frequency (80MHz/80)
  timerAttachInterrupt(timer, &onTimer, true);  //Attach the interrupt to Timer1
  unsigned int timerFactor = 1000000 / sample_rate;           //Calculate the time interval between two readings, or more accurately, the number of cycles between two readings
  timerAlarmWrite(timer, timerFactor, true);    //Initialize the timer
  timerAlarmEnable(timer);

  setTimer(1000);


#if BLUETOOTH_MODE
  SerialBT.begin("LoadCell");  //Bluetooth device name
#endif

  pinMode(LOADCELL01_PIN, INPUT);
  pinMode(LOADCELL02_PIN, INPUT);
}

void loop() {
  int loadcell = analogRead(LOADCELL01_PIN);
  if (timer_flag == 1) {
    setTimer(1);
    Serial.printf("%d\n", loadcell);
#if BLUETOOTH_MODE
    SerialBT.printf("%d\n", loadcell);
#endif
  }
}

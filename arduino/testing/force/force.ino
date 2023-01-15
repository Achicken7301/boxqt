#include "BluetoothSerial.h"

#if !defined(CONFIG_BT_ENABLED) || !defined(CONFIG_BLUEDROID_ENABLED)
#error Bluetooth is not enabled! Please run `make menuconfig` to and enable it
#endif

#if !defined(CONFIG_BT_SPP_ENABLED)
#error Serial Bluetooth not available or not enabled. It is only available for the ESP32 chip.
#endif

BluetoothSerial SerialBT;


int timer_counter = 0;
int timer_flag = 0;

int sampleRate = 1000; // 1000Hz

#define CLOCK_TICK 1 //1ms

hw_timer_t * timer = NULL;


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

#define FORCE_PIN   2

void setup() {
  Serial.begin(115200);
  pinMode(FORCE_PIN, INPUT);
  SerialBT.begin("ForceFSR"); //Bluetooth device name

  //  Create timer 1
  timer = timerBegin(1, 80, true);                    //Begin timer with 1 MHz frequency (80MHz/80)
  timerAttachInterrupt(timer, &onTimer, true);        //Attach the interrupt to Timer1
  unsigned int timerFactor = 1000000 / sampleRate;    //Calculate the time interval between two readings, or more accurately, the number of cycles between two readings
  timerAlarmWrite(timer, timerFactor, true);          //Initialize the timer
  timerAlarmEnable(timer);

  setTimer(1000);
}
double Vmeas;

double map_vmeas(double x, double in_min, double in_max, double out_min, double out_max) {
  return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min;
}

void loop() {
  Vmeas = map_vmeas(analogRead(FORCE_PIN), 0.0, 4095.0, 0.0, 3.3);
//  if (timer_flag == 1) {
//    setTimer(1000);
//    Serial.printf("%d\n", analogRead(FORCE_PIN));
//  }
  SerialBT.printf("%0.4f\n", Vmeas);

}

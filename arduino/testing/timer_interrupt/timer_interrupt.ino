#include <Arduino.h>

hw_timer_t* timer = NULL;
portMUX_TYPE timerMux = portMUX_INITIALIZER_UNLOCKED;

unsigned int t = 0;
//print to serial every 1s
void IRAM_ATTR onTimer() {
  portENTER_CRITICAL_ISR(&timerMux); //vào chế độ tránh xung đột
  
  portEXIT_CRITICAL_ISR(&timerMux); // thoát
}

void setup() {
  Serial.begin(115200);
  //khơit tạo timer với chu kì 1ms vì thạch anh của ESP chạy 8MHz
  timer = timerBegin(0, 8000, true);
  //khởi tạo hàm xử lý ngắt ngắt cho Timer
  timerAttachInterrupt(timer, &onTimer, true);
  //khởi tạo thời gian ngắt cho timer là 1s (1000 ms)
  timerAlarmWrite(timer, 2000, true);
  //bắt đầu chạy timer
  timerAlarmEnable(timer);

}

void loop() {
  // put your main code here, to run repeatedly:

}

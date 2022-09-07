/*********
  Rui Santos
  Complete project details at https://randomnerdtutorials.com  
*********/

TaskHandle_t Task1;
TaskHandle_t Task2;

// LED pins
const int led1 = 2;
const int led2 = 4;

void setup() {
  Serial.begin(115200); 
  pinMode(led1, OUTPUT);
  pinMode(led2, OUTPUT);

  //create a task that will be executed in the Task1code() function, with priority 1 and executed on core 0
  xTaskCreatePinnedToCore(
                    Task1code,   /* Task function. */
                    "Task1",     /* name of task. */
                    10000,       /* Stack size of task */
                    NULL,        /* parameter of the task */
                    1,           /* priority of the task */
                    &Task1,      /* Task handle to keep track of created task */
                    0);          /* pin task to core 0 */                  
  delay(500); 

  //create a task that will be executed in the Task2code() function, with priority 1 and executed on core 1
  xTaskCreatePinnedToCore(
                    Task2code,   /* Task function. */
                    "Task2",     /* name of task. */
                    10000,       /* Stack size of task */
                    NULL,        /* parameter of the task */
                    1,           /* priority of the task */
                    &Task2,      /* Task handle to keep track of created task */
                    1);          /* pin task to core 1 */
    delay(500); 
}

//Task1code: blinks an LED every 1000 ms
void Task1code( void * pvParameters ){
  Serial.print("Task1 running on core ");
  Serial.println(xPortGetCoreID());

  for(;;){
    digitalWrite(led1, HIGH);
    delay(1000);
    digitalWrite(led1, LOW);
    delay(1000);
  } 
}

//Task2code: blinks an LED every 700 ms
void Task2code( void * pvParameters ){
  Serial.print("Task2 running on core ");
  Serial.println(xPortGetCoreID());

  for(;;){
    digitalWrite(led2, HIGH);
    delay(700);
    digitalWrite(led2, LOW);
    delay(700);
  }
}

ets Jun  8 2016 00:22:57

rst:0xc (SW_CPU_RESET),boot:0x13 (SPI_FAST_FLASH_BOOT)
configsip: 0, SPIWP:0xee
clk_drv:0x00,q_drv:0x00,d_drv:0x00,cs0_drv:0x00,hd_drv:0x00,wp_drv:0x00
mode:DIO, clock div:1
load:0x3fff0030,len:1284
load:0x40078000,len:12836
load:0x40080400,len:3032
entry 0x400805e4
Guru Meditation Error: Core  0 panic'ed (IllegalInstruction). Exception was unhandled.
Memory dump at 0x400d1d44: 025be502 0000f01d ad004136
Core  0 register dump:
PC      : 0x400d1d48  PS      : 0x00060f30  A0      : 0x00000000  A1      : 0x3ffcc000  
A2      : 0x3ffc1df0  A3      : 0x3f40ef9f  A4      : 0x00000000  A5      : 0x00000000  
A6      : 0x00000000  A7      : 0x00000000  A8      : 0x800d1d48  A9      : 0x3ffcbfe0  
A10     : 0x00000000  A11     : 0x00000000  A12     : 0x00000000  A13     : 0xc0389dd9  
A14     : 0x00000002  A15     : 0x00000000  SAR     : 0x0000001c  EXCCAUSE: 0x00000000  
EXCVADDR: 0x00000000  LBEG    : 0x4008f775  LEND    : 0x4008f785  LCOUNT  : 0xffffffff  


Backtrace:0x400d1d45:0x3ffcc000




ELF file SHA256: 0000000000000000
#define GAIN_128 25
#define GAIN_64 27

const int doutPin = 4;
const int sckPin = 2;

void setup() {
  Serial.begin(57600);
  pinMode(doutPin, INPUT);
  pinMode(sckPin, OUTPUT);
}

void loop() {
  unsigned long raw = readHX711();
  Serial.println(raw);
//  delay(500);
}

unsigned long readHX711() {
  unsigned long data = 0;
  uint8_t dout;

  while (digitalRead(doutPin)) {} // wait until value is available
  for (uint8_t i = 0; i < GAIN_128; i++) { //highest Gain
//    delayMicroseconds(1); // uncomment for fast MCUs
    digitalWrite(sckPin, 1);
//    delayMicroseconds(1); // uncomment for fast MCUs
    digitalWrite(sckPin, 0);
    if (i < (24)) {
      dout = digitalRead(doutPin);
      data = (data << 1) | dout;
    }
  }
  data = data ^ 0x800000; // flip bit 23

  return data;
}

void powerDown() {
  digitalWrite(sckPin, LOW);
  digitalWrite(sckPin, HIGH);
}

void powerUp() {
  digitalWrite(sckPin, LOW);
}

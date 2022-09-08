// Potentiometer is connected to GPIO 34 (Analog ADC1_CH6) 
const int potPin = 2;

// variable for storing the potentiometer value
int potValue = 0;

void setup() {
  Serial.begin(115200);
  pinMode(potPin, INPUT);
}

void loop() {
  // Reading potentiometer value
  int potValue = analogRead(potPin);
  Serial.println(potValue);
  delay(10);
}

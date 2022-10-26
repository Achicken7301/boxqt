const int potPin = 2;
int potValue = 0;

void setup() {
  pinMode(potPin, INPUT);
  Serial.begin(115200);
}

void loop() {
  int potValue = analogRead(potPin);
  Serial.println(potValue);
}

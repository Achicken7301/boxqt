void setup() {
  Serial.begin(115200);
}

void loop() {
  Serial.println(random(-200, 200));
//  delay(50);
}

void setup() {
  Serial.begin(115200);
}

static int sampleRate = 150;

void loop() {
  if (Serial.available() > 0) {
    Serial.printf("Received data: "); Serial.println(Serial.parseInt());
    sampleRate = int(Serial.parseInt());
  }

  Serial.print("Sample Rate: "); Serial.println(int(sampleRate));
  delay(1000);
}

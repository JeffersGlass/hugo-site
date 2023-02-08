// Echos back whatever is written to the serial port, with a small delay
void setup() {
  Serial.begin(9600);
}

void loop() {
  if (Serial.available() > 0){
    int incomingByte = Serial.read();
    delay(100);
    Serial.print(char(incomingByte));
  }
}
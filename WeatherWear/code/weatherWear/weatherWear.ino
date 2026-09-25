#include <Servo.h>

int curr_pos = 0;
int target_pos = 0;

Servo servo_9;

void setup() {
  
  servo_9.attach(9, 500, 2500);

  pinMode(A2, OUTPUT);
  pinMode(A3, OUTPUT);
  digitalWrite(A2, HIGH);
  digitalWrite(A3, HIGH);

  Serial.begin(9600);

  servo_9.write(90);
  delay(15);
}

void loop() {

  if(digitalRead(A2) == 0) {
    Serial.write('q');
    delay(1000);
  } else if(digitalRead(A3) == 0) {
    Serial.write('w');
    delay(1000);
  }

  if(Serial.available() > 0) {
    String value = Serial.readString();

    if(value == "HWJ") {
      target_pos = 140;
    } else if(value == "PJ") {
      target_pos = 114;
    } else if(value == "RJ") {
      target_pos = 88;
    } else if(value == "JJ") {
      target_pos = 62;
    } else if(value == "Hoodie") {
      target_pos = 36;
    } else if(value == "Shirt") {
      target_pos = 10;
    }
  }
  
  if(curr_pos < target_pos) {
    while (curr_pos < target_pos) {
      curr_pos += 1;
      servo_9.write(curr_pos);
      delay(15);
    }
  } else if(curr_pos > target_pos) {
    while (curr_pos > target_pos) {
      curr_pos -= 1;
      servo_9.write(curr_pos);
      delay(15);
    }
  }
}

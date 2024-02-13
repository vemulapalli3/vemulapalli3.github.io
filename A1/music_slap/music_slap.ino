char value[15] = {'z','z','c','d','e','f','g','a','b','D','E','G','A','B','z'};

void setup() {
  
  pinMode(2, INPUT_PULLUP);
  pinMode(3, INPUT_PULLUP);
  pinMode(4, INPUT_PULLUP);
  pinMode(5, INPUT_PULLUP);
  pinMode(6, INPUT_PULLUP);
  pinMode(7, INPUT_PULLUP);
  pinMode(8, INPUT_PULLUP);
  pinMode(9, INPUT_PULLUP);
  pinMode(10, INPUT_PULLUP);
  pinMode(11, INPUT_PULLUP);
  pinMode(12, INPUT_PULLUP);
  pinMode(13, INPUT_PULLUP);

  pinMode(A2, OUTPUT);
  pinMode(A3, OUTPUT);
  digitalWrite(A2, HIGH);
  digitalWrite(A3, HIGH);

  Serial.begin(9600);
}

void loop() {
  
  for(int i=2; i<=13; i++) {
    if(digitalRead(i) == 0) {
      Serial.write(value[i]);
      delay(1000);
    }
  }

  if(digitalRead(A2) == 0) {
    Serial.write('q');
    delay(1000);
  } else if(digitalRead(A3) == 0) {
    Serial.write('w');
    delay(1000);
  }

}

//DigiEmoji

int buttonPress = 2;
int counter = 1;
void setup() {
  pinMode(13, OUTPUT);
  pinMode(12, OUTPUT);
  pinMode(11, OUTPUT);
  pinMode(10, OUTPUT);
  pinMode(9, OUTPUT);
  pinMode(8, OUTPUT);
  pinMode(7, OUTPUT);
  pinMode(6, OUTPUT);
  pinMode(5, OUTPUT);
  pinMode(4, OUTPUT);
  
  pinMode(buttonPress, INPUT);
  digitalWrite(buttonPress, HIGH);
}

void loop() {
  if(digitalRead(buttonPress) == 0) {
    counter++;
    if(counter > 5) {
     counter = 1; 
    }
    for(int i=4; i<=13; i++) {
      digitalWrite(i, LOW);
    }
    delay(500);
  }
  if(counter == 1) {
   for(int i=5; i<=13; i++) {
      digitalWrite(i, HIGH);
    } 
  }
  if(counter == 2) {
    for(int i=10; i<=12; i++) {
      digitalWrite(i, HIGH);
    }
    digitalWrite(4, HIGH);
    for(int i=7; i<=8; i++) {
      digitalWrite(i, HIGH);
    }
  }
  if(counter == 3) {
    for(int i=9; i<=13; i++) {
      digitalWrite(i, HIGH);
    }
    digitalWrite(4, HIGH);
    digitalWrite(8, HIGH);
    digitalWrite(5, HIGH);
  }
  if(counter == 4) {
    for(int i=0; i<=13; i++) {
      digitalWrite(i, HIGH);
    }
  }
  if(counter == 5) {
    digitalWrite(12, HIGH);
    digitalWrite(10, HIGH);
    for(int i=5; i<=8; i++) {
      digitalWrite(i, HIGH);
    }
  }
}

char value[15] = {'z','C','c','d','e','f','g','a','b','D','E','G','A','B','z'};
String str = "";

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
  pinMode(A4, OUTPUT);
  digitalWrite(A2, HIGH);
  digitalWrite(A3, HIGH);
  digitalWrite(A4, HIGH);

  Serial.begin(9600);

}

void loop() {
  
  if(digitalRead(A4) == 0) {
    str += String(value[1]);
    //Serial.println(value[1]);
    //Serial.write(value[1]);
    //delay(500);
  }
  for(int i=2; i<=13; i++) {
    if(digitalRead(i) == 0) {
      str += String(value[i]);
      //Serial.println(value[i]);
      //Serial.write(value[i]);
      //Serial.println(str);
      //delay(1000);
    }
  }
  if(str.length() > 0) {
    str += '\n';
    //Serial.println(str);
    Serial.write(str.c_str());
    delay(1000);
    str = "";
  }

  if(digitalRead(A2) == 0) {
    Serial.write("q\n");
    delay(1000);
  } else if(digitalRead(A3) == 0) {
    Serial.write("w\n");
    delay(1000);
  }

}

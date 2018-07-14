void setup() {
  Serial.begin(9600);
  pinMode(8,INPUT);
  pinMode(9,INPUT);
  pinMode(10,INPUT);

}

void readAndPrintln(int num){
  if(digitalRead(num) == LOW){
    Serial.println(num);
    Serial.println("OFF");
  }  
}

void loop() {

  readAndPrintln(8);
  readAndPrintln(9);
  readAndPrintln(10);
  
  delay(1000);

}

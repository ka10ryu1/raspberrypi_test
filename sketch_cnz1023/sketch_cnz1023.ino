String val;

void setup() {
  Serial.begin(9600);
  pinMode(8,INPUT);
  pinMode(9,INPUT);
  pinMode(10,INPUT);
}

String checkSensor(int pin){
  if(digitalRead(pin) == HIGH){
    return "1";
  }
  return "0";
}

void loop() {

  val = "5";
  val.concat(checkSensor(8));
  val.concat(checkSensor(9));
  val.concat(checkSensor(10));
  //Serial.println(val);
  Serial.print(val);
  delay(2000);

} 

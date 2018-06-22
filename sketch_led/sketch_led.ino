// Example 01 : Blinking LED
 
const int LED1 = 13;  // LED connected to digital pin 13
const int LED2 = 12;  // LED connected to digital pin 12
 
void setup()
{
  pinMode(LED1, OUTPUT); //sets thebdigital
  pinMode(LED2, OUTPUT); //sets thebdigital
  //pin as output
}
 
void loop()
{
  digitalWrite(LED1, HIGH); // turns the LED on
  digitalWrite(LED2, LOW); // turns the LED on
  delay(1000);             // waits for a second
  digitalWrite(LED1, LOW);  // turns the LED off
  digitalWrite(LED2, HIGH);  // turns the LED off
  delay(500);             // waits for a second
}

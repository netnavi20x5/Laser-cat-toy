#include <Servo.h>
Servo servo1;
Servo servo2;
int x=0;
int y = 0;
void setup() 
{
 pinMode(LED_BUILTIN, OUTPUT);
 servo1.attach(D1);
 servo2.attach(D2);
 servo1.write(90);
 servo2.write(90);
 Serial.begin (115200);
 //servo1.write(0);
 //servo2.write(0);
 //servo1.attach(3);
 //servo2.attach(5);
}

void loop() {
  x=random(50,150);
  y=random(100,150);
  servo1.write(x);
  servo2.write(y);
  delay(500);
  digitalWrite(LED_BUILTIN, HIGH);
}

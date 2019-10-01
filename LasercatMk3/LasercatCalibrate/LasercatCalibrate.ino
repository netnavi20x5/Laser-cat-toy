#include<Servo.h>
String a ="X90:Y90";
Servo serX;
Servo serY;

String tempModify;

void setup() {

  serX.attach(D1);
  serY.attach(D2);
  serX.write(90);
  serY.write(90);
  Serial.begin (9600);
  Serial.setTimeout(10);
}

void loop() {

while(Serial.available()) {
a= Serial.readString();// read the incoming data as string
Serial.println(a);
Serial.println(parseDataX(a));
Serial.println(parseDataY(a));
serX.write(parseDataX(a));
serY.write(parseDataY(a));

  }

}

void serialEvent() {
tempModify = Serial.readString();
serX.write(parseDataX(tempModify));
serY.write(parseDataY(tempModify));

}

int parseDataX(String data){
  data.remove(data.indexOf(":"));
  data.remove(data.indexOf("X"), 1);
  return data.toInt();
}

int parseDataY(String data){
  data.remove(0,data.indexOf(":") + 1);
  data.remove(data.indexOf("Y"), 1);
  return data.toInt();
  
}

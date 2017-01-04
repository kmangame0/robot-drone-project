#include <Servo.h> 
#define echoPin 7 // Echo Pin
#define trigPin 8 // Trigger Pin
Servo myservo;
int pos = 0;
boolean connected = false;
int incomingByte = 0;
byte b= B00000000;
int maximumRange = 200; // Maximum range needed
int minimumRange = 0; // Minimum range needed
long duration, distance; // Duration used to calculate distance

void setup() 
{ 
  Serial.begin(9600);
  myservo.attach(9); 
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
  
} 

void loop() 
{ 
  for(pos = 0; pos < 150; pos += 1)
  {                          
    myservo.write(pos);
    b = pos;
    Serial.print(b);
    Serial.write(b);

    digitalWrite(trigPin, LOW); 
    delayMicroseconds(2); 
    digitalWrite(trigPin, HIGH);
    delayMicroseconds(10); 
    digitalWrite(trigPin, LOW);
    duration = pulseIn(echoPin, HIGH);
    delay(10);
    distance = duration/58.2;
    if (distance >= maximumRange || distance <= minimumRange){
      Serial.print("k");
      Serial.print(distance);
      Serial.print("k");
//      b=200;
//      Serial.write(b);
    }
    else {
       Serial.print(b);
      b = int(distance);
      Serial.print(b);
      Serial.write(b);
    }
  delay(25);
  }
  for(pos = 150; pos>=0; pos-=1)   
  {                                
    myservo.write(pos);
    b = pos;
    Serial.write(b);

    digitalWrite(trigPin, LOW); 
    delayMicroseconds(2); 
    digitalWrite(trigPin, HIGH);
    delayMicroseconds(10); 
    digitalWrite(trigPin, LOW);
    duration = pulseIn(echoPin, HIGH);

    distance = duration/58.2;
    if (distance >= maximumRange || distance <= minimumRange){
//      b=300;
//      Serial.write(b);
    }
    else {
      Serial.print(b);
      b = int(distance);
      Serial.print(b);
      Serial.write(b);
    }
 delay(25);
  } 
} 






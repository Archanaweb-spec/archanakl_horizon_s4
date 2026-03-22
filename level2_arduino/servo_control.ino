#include <Servo.h>

Servo s;

int pot = A0;
int led = 7;

int val;
int angle;

void setup()
{
  s.attach(9);
  pinMode(led, OUTPUT);
}

void loop()
{
  val = analogRead(pot);

  angle = map(val, 0, 1023, 0, 180);

  if(angle > 68)
  {
    s.write(68);
    digitalWrite(led, HIGH);
  }
  else
  {
    s.write(angle);
    digitalWrite(led, LOW);
  }

  delay(15);
}

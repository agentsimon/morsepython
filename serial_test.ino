int led = 2;

void setup() 
{
  pinMode(2, OUTPUT);
  Serial.begin(9600);
  while (!Serial);
  Serial.println("Input 1 to Turn LED on and 2 to off");
}

void loop()
{
  if (Serial.available())
  {
    int state = Serial.parseInt();
    if (state == 1)
    {
     digitalWrite(led, LOW);
     Serial.println("Command completed LED turned ON");
    }
    if (state == 0)
    {
     digitalWrite(led, HIGH);
     Serial.println("Command completed LED turned OFF");
    }  
  }
}

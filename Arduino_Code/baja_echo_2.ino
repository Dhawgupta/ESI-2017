int echoPin[4] = {4,5,6,7};
int trigPin[5] = {9,10,11,12,8};
int grounds[3] = { 13,2,3};
 
void setup() {
  Serial.begin (9600);
  for(int i = 0 ; i< 5;i++)
    pinMode(trigPin[i], OUTPUT);
  for(int i=0; i< 3; i++)
    {
      pinMode(grounds[i] , OUTPUT);
      digitalWrite(grounds[i],LOW);
      
    }
  for(int i = 0 ; i< 4;i++)
    pinMode(echoPin[i], INPUT);
}
long distance_measure(int trig, int echo)
{
  long distance,duration;
  digitalWrite(trig, LOW);
  delayMicroseconds(2);
  digitalWrite(trig, HIGH);
  delayMicroseconds(10);
  digitalWrite(trig, LOW);
  duration = pulseIn(echo, HIGH);
  distance = (duration/2) / 29.1;
  return distance;

}


void loop() {
  
  long distance;
  if(Serial.available()!=0)
   {
      char a = Serial.read();
      switch(a)
      {
        case 'a':  distance = distance_measure(trigPin[0], echoPin[0]);
                   break;
        case 'b':  distance = distance_measure(trigPin[1], echoPin[1]);
                   break;
        case 'c':  distance = distance_measure(trigPin[2], echoPin[2]);
                   break;
        case 'd':  distance = distance_measure(trigPin[3], echoPin[3]);
                   break;
      }
      if(distance > 255)
    distance = 255;
    //Serial.print(char(distance)); // for the raspi 
    Serial.println(distance); // to debug the code
    
      
   }
   
 
  
    //Serial.print(char(distance[i]));
    //Serial.print(" ");
    //Serial.println();
  
  
}




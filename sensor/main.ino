const int trigPin = 9;
const int echoPin = 10;

void setup()
{
    Serial.begin(9600);
    pinMode(trigPin, OUTPUT);
    pinMode(echoPin, INPUT);
}

void loop()
{
    // Calculate the distance
    digitalWrite(trigPin, LOW);
    delayMicroseconds(2);
    digitalWrite(trigPin, HIGH);
    delayMicroseconds(10);
    digitalWrite(trigPin, LOW);

    // Calculate sound wave response time
    long duration = pulseIn(echoPin, HIGH);

    // Calculate the distance (speed of sound 340 m/s)
    int distance = duration * 0.034 / 2;

    // Print the distance
    Serial.print("Mesafe: ");
    Serial.print(distance);
    Serial.println(" cm");

    // wait
    delay(1000);
}

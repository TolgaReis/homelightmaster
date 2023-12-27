// Distance sensor pins
const int trigPin = 9;  // Trig
const int echoPin = 10; // Echo

// Light sensor pin
const int ldrPin = A0; // analog pin that LDR sensor connected

const int soundSpeed = 0.034;

void setup()
{
    Serial.begin(9600); // Start the serial communication
    pinMode(trigPin, OUTPUT);
    pinMode(echoPin, INPUT);
}

void loop()
{

    // (speed of sound 340 m/s)
    int distance = calculateDistance();

    // Read the LDR sensor
    int ldrValue = readLightDependentResistence();

    // Print the distance and LDR to the monito
    Serial.print("Distance: ");
    Serial.print(distance);
    Serial.print(" cm\t");

    Serial.print("LDR: ");
    Serial.println(ldrValue);

    // Wait
    delay(1000);
}

int calculateDistance()
{
    // Distance calculation
    digitalWrite(trigPin, LOW);
    delayMicroseconds(2);
    digitalWrite(trigPin, HIGH);
    delayMicroseconds(10);
    digitalWrite(trigPin, LOW);

    // Response time of sound wave
    long duration = pulseIn(echoPin, HIGH);

    return duration * soundSpeed / 2;
}

int readLightDependentResistence()
{
    return analogRead(ldrPin);
}
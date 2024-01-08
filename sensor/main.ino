#include <WiFi.h>
#include <PubSubClient.h>

// WiFi settings
const char *ssid = "SSID";
const char *password = "PASS";

const char *mqttBroker = "ip";
const int mqttPort = 1883;
const char *mqttTopic = "/sensor/data";

// Distance sensor pins
const int trigPin = 2; // Trig
const int echoPin = 4; // Echo

// Light sensor pin
const int ldrPin = 15; // analog pin that LDR sensor connected

const int soundSpeed = 0.034;

WiFiClient espClient;
PubSubClient client(espClient);

void setup()
{
    Serial.begin(9600); // Start the serial communication
    pinMode(trigPin, OUTPUT);
    pinMode(echoPin, INPUT);

    connectToWiFi();

    client.setServer(mqttBroker, mqttPort);
    client.setCallback(callback);
    connectToMQTT();
}

void loop()
{
    if (!client.connected())
    {
        connectToMQTT();
    }

    client.loop();

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

    char message[50];
    sprintf(message, "{\"distance\":%d,\"ldrValue\":%d}", distance, ldrValue);
    client.publish(mqttTopic, message);

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

int readLDR()
{
    return analogRead(ldrPin);
}

void connectToWiFi()
{
    Serial.print("WiFi connecting...");

    WiFi.begin(ssid, password);

    while (WiFi.status() != WL_CONNECTED)
    {
        delay(1000);
        Serial.print(".");
    }

    Serial.println("\nWiFi connection successful!");
    Serial.print("IP Address: ");
    Serial.println(WiFi.localIP());
}

void connectToMQTT()
{
    while (!client.connected())
    {
        Serial.print("MQTT'ye connecting...");

        if (client.connect("ESP32Client", mqttUser, mqttPassword))
        {
            Serial.println("Connection successful!");
            client.subscribe(mqttTopic);
        }
        else
        {
            Serial.print("Connection failed, error code=");
            Serial.println(client.state());
            delay(2000);
        }
    }
}

void callback(char *topic, byte *payload, unsigned int length)
{
    Serial.print("MQTT message received [");
    Serial.print(topic);
    Serial.print("]: ");

    for (int i = 0; i < length; i++)
    {
        Serial.print((char)payload[i]);
    }

    Serial.println();
}
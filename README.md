# Infra

Infra contains Docker compose and config files to provision Docker containers MongoDB and Mosquitto.

# Service

Service is designed to read sensor data by subscribing to MQTT topic, add timestamp and status(ALARM, NORMAL) parameters then save it to MongoDB.

# UI

UI is a user interface designed to manage IoT devices and display notifications in case of alarm conditions.

## Features

- **IoT Device Management:**
  - Easily add, remove, and monitor IoT devices from the user interface.
  - View real-time status and data from connected IoT devices.

- **Alarm Notification:**
  - Receive timely notifications in case of alarm conditions or critical events.
  - Customizable alert settings for different types of alarms.

# Sensor

It is designed to create home automation using an ESP32 microcontroller with light and distance sensors. The data obtained from these sensors will be sent to the service using the MQTT protocol via Mosquitto. The project can be used to measure the ambient light in the home and determine whether the store curtain is open or closed.

## Hardware Requirements
- ESP32 microcontroller
- KY-018 LDR Light Sensor Card
- HC-SR04 Ultrasonic Distance Sensor
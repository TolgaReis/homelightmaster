# mqtt_handler.py

import paho.mqtt.client as mqtt
from config.config import Config


class MQTTHandler:
    def __init__(self):
        self.host = Config.MQTT_BROKER_HOST
        self.port = Config.MQTT_BROKER_PORT
        self.topic = Config.MQTT_TOPIC
        self.latest_messages = []
        self.client = mqtt.Client()
        self.client.on_message = self.on_message
        self.client.connect(self.host, self.port, 60)
        self.client.subscribe(self.topic)
        self.client.loop_start()

    def on_message(self, client, userdata, msg):
        message = msg.payload.decode("utf-8")
        print(f"Received message: {message}")
        self.latest_messages.append(message)
        if len(self.latest_messages) > 10:
            self.latest_messages.pop(0)

    def get_latest_messages(self):
        return self.latest_messages

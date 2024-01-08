# mqtt_handler.py

import paho.mqtt.client as mqtt
from config.config import Config
from datetime import datetime
from mongo import MongoDB
import json


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

        self.mongodb_client = MongoDB()

    def on_message(self, client, userdata, msg):
        message = json.loads(msg.payload.decode("utf-8"))
        timestamp = datetime.now()
        is_close = True if message["distance"] < 20.0 else False
        is_daytime = True if message["light"] >= 55 else False

        if is_daytime and is_close:
            message_type = "OPEN"
        elif (not is_daytime and is_close) or (is_daytime and not is_close):
            message_type = "NO_ACTION"
        else:
            message_type = "CLOSE"

        message_with_metadata = {
            "message": message,
            "timestamp": timestamp,
            "type": message_type
        }

        self.mongodb_client.write_to_mongodb(message_with_metadata)

        self.latest_messages.append(message)
        if len(self.latest_messages) > 10:
            self.latest_messages.pop(0)

    def get_latest_messages(self):
        return self.latest_messages

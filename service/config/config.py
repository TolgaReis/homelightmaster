class Config:
    MQTT_BROKER_HOST = "localhost"
    MQTT_BROKER_PORT = 1883
    MQTT_TOPIC = "/sensor/data"

    MONGODB_URI = "mongodb://localhost:27017/"
    MONGODB_DATABASE = "sensordb"
    MONGODB_COLLECTION = "sensorcollection"

from flask import Flask, jsonify
from mqtt_handler import MQTTHandler

app = Flask(__name__)

mqtt_broker_host = "localhost"
mqtt_broker_port = 1883
mqtt_topic = "/sensor/data"

mqtt_handler = MQTTHandler(mqtt_broker_host, mqtt_broker_port, mqtt_topic)


@app.route('/api/latest_mqtt_messages', methods=['GET'])
def get_latest_mqtt_messages():
    latest_messages = mqtt_handler.get_latest_messages()
    return jsonify({"latest_messages": latest_messages})


if __name__ == '__main__':
    app.run(debug=True)

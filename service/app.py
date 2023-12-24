from flask import Flask, jsonify
import paho.mqtt.client as mqtt

app = Flask(__name__)

mqtt_broker_host = "localhost"
mqtt_broker_port = 1883
mqtt_topic = "/sensor/data"

latest_messages = []


def on_message(client, userdata, msg):
    message = msg.payload.decode("utf-8")
    print(f"Received message: {message}")
    latest_messages.append(message)
    if len(latest_messages) > 10:
        latest_messages.pop(0)


mqtt_client = mqtt.Client()
mqtt_client.on_message = on_message
mqtt_client.connect(mqtt_broker_host, mqtt_broker_port, 60)
mqtt_client.subscribe(mqtt_topic)
mqtt_client.loop_start()


@app.route('/api/latest_mqtt_messages', methods=['GET'])
def get_latest_mqtt_messages():
    return jsonify({"latest_messages": latest_messages})


if __name__ == '__main__':
    app.run(debug=True)

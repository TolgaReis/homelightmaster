from flask import Flask, jsonify, render_template, url_for
from mqtt_handler import MQTTHandler
from mongo import MongoDB
from datetime import datetime
from datetime import timedelta

from flask_socketio import SocketIO, emit
import time
from threading import Thread

app = Flask(__name__)
socketio = SocketIO(app)

mqtt_handler = MQTTHandler()
mongodb = MongoDB()


@app.route('/api/latest_mqtt_messages', methods=['GET'])
def get_latest_mqtt_messages():
    latest_messages = mqtt_handler.get_latest_messages()
    return jsonify({"latest_messages": latest_messages})


@app.route('/')
def index():
    return render_template('index_socketio.html')


@socketio.on('connect')
def handle_connect():
    print('Client connected')


@socketio.on('disconnect')
def handle_disconnect():
    print('Client disconnected')


def background_thread():
    while True:
        time.sleep(10)
        data = {'timestamp': time.strftime('%Y-%m-%d %H:%M:%S')}
        # Son 60 dakikaya ait UNIX zaman damgası
        last_60_mins = datetime.now() - timedelta(minutes=60)

        # MongoDB sorgusu ile verileri filtrele
        query = {"timestamp": {"$gte": last_60_mins}}
        data = mongodb.find(query=query).sort('timestamp', -1).limit(1)
        print(data[0])
        message = dict()
        message['light'] = f"{data[0]['message']['light']}%"
        message['status'] = data[0]['type']
        socketio.emit('update_data', message)


@socketio.on('start_updates')
def start_updates():
    # İstemci bağlandığında arka planda güncelleme işlemini başlat
    thread = Thread(target=background_thread)
    thread.daemon = True
    thread.start()


if __name__ == '__main__':
    app.run(debug=True)

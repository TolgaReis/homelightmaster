// src/App.js

import React, { useEffect, useState } from 'react';
import { Line } from 'react-chartjs-2';
import MqttService from './service/MqttService';

const App = () => {
  const [data, setData] = useState([]);
  const mqttService = new MqttService();

  useEffect(() => {
    // İstediğiniz MQTT konusunu burada belirtin
    const topic = 'topic/veri';

    mqttService.connect(topic, () => {
      // Bağlantı başarılı olduğunda yapılacak işlemleri buraya ekleyebilirsiniz
    });

    return () => {
      mqttService.disconnect();
    };
  }, []);

  const chartData = {
    labels: data.map((_, index) => index),
    datasets: [
      {
        label: 'MQTT Verisi',
        data: data,
        borderWidth: 1,
        fill: false,
      },
    ],
  };

  return (
    <div>
      <Line data={chartData} />
    </div>
  );
};

export default App;

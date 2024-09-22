import paho.mqtt.client as mqtt
from data_processor import DataProcessor

class MQTTListener:
    def __init__(self, broker, port, topic, data_processor):
        self.broker = broker
        self.port = port
        self.topic = topic
        self.data_processor = data_processor
        self.client = mqtt.Client()

    def on_connect(self, client, userdata, flags, rc):
        if rc == 0:
            print("Conectado ao broker MQTT.")
            client.subscribe(self.topic)
            print(f"Inscrito no tópico: {self.topic}")
        else:
            print(f"Falha na conexão, código de retorno {rc}")

    def on_message(self, client, userdata, msg):
        try:
            message = msg.payload.decode()
            gas_value = int(message)
            print(f"Valor recebido do sensor: {gas_value}")
            self.data_processor.process(gas_value)
        except Exception as e:
            print(f"Erro ao processar mensagem: {e}")

    def start(self):
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message
        self.client.connect(self.broker, self.port, 60)
        self.client.loop_forever()

from umqtt.simple import MQTTClient
import ubinascii
import machine

class MQTTClientWrapper:
    def __init__(self, broker, port, topic, client_id=None):
        if client_id is None:
            client_id = ubinascii.hexlify(machine.unique_id())
        self.client = MQTTClient(client_id, broker, port=port)
        self.topic = topic

    def connect(self):
        self.client.connect()
        print("Conectado ao broker MQTT.")

    def publish(self, message):
        self.client.publish(self.topic, message)
        print(f"Publicado no tópico {self.topic}: {message}")

    def disconnect(self):
        self.client.disconnect()
        print("Desconectado do broker MQTT.")

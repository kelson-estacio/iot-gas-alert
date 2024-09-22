from mqtt_listener import MQTTListener
from data_processor import DataProcessor
from notifier import Notifier

# Configurações MQTT
MQTT_BROKER = "broker.hivemq.com"
MQTT_PORT = 1883
MQTT_TOPIC = "iot/gas_leak"

# Configurações de notificação
EMAIL = "seuemail@gmail.com"
PASSWORD = "suasenha"
RECIPIENT = "destinatario@gmail.com"

# Limite para detecção de gás (1 para digital)
GAS_THRESHOLD = 1  # 1 = Gás detectado

# Inicialização dos módulos
notifier = Notifier(EMAIL, PASSWORD, RECIPIENT)
data_processor = DataProcessor(GAS_THRESHOLD, notifier)
mqtt_listener = MQTTListener(MQTT_BROKER, MQTT_PORT, MQTT_TOPIC, data_processor)

if __name__ == "__main__":
    mqtt_listener.start()

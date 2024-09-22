import time
from device.sensor import GasSensor
from device.mqtt_client import MQTTClientWrapper

# Configurações
MQTT_BROKER = "broker.hivemq.com"
MQTT_PORT = 1883
MQTT_TOPIC = "iot/gas_leak"

# Configurações de Wi-Fi
WIFI_SSID = "Seu_SSID"
WIFI_PASSWORD = "Sua_Senha"

# Inicialização dos módulos
sensor = GasSensor(sensor_pin=5, led_pin=48, wifi_ssid=WIFI_SSID, wifi_password=WIFI_PASSWORD)
mqtt = MQTTClientWrapper(MQTT_BROKER, MQTT_PORT, MQTT_TOPIC)

# Conectar ao broker MQTT
mqtt.connect()

try:
    while True:
        gas_detected = sensor.read_gas()
        mqtt.publish(str(int(gas_detected)))  # Publica 1 se detectado, 0 caso contrário
        
        if gas_detected:
            sensor.set_led_color((255, 0, 0))  # Vermelho
            print("Gás detectado! LED vermelho aceso.")
        else:
            sensor.turn_off_led()
            print("Sem gás detectado. LED apagado.")
        
        time.sleep(5)  # Intervalo de 5 segundos
except KeyboardInterrupt:
    mqtt.disconnect()
    sensor.turn_off_led()
    print("Execução interrompida pelo usuário.")

from machine import Pin, PWM
import neopixel
import network
import time

class GasSensor:
    def __init__(self, sensor_pin=5, led_pin=48, wifi_ssid='Seu_SSID', wifi_password='Sua_Senha'):
        # Configura o pino do sensor como entrada digital com resistor pull-up
        self.sensor = Pin(sensor_pin, Pin.IN, Pin.PULL_UP)
        
        # Configura o pino do LED RGB como saída para o NeoPixel
        self.led = neopixel.NeoPixel(Pin(led_pin), 1)  # 1 LED RGB
        
        # Configurações de Wi-Fi
        self.wifi_ssid = wifi_ssid
        self.wifi_password = wifi_password
        self.wifi = network.WLAN(network.STA_IF)
        self.connect_wifi()
    
    def connect_wifi(self):
        if not self.wifi.isconnected():
            print('Conectando ao Wi-Fi...')
            self.wifi.active(True)
            self.wifi.connect(self.wifi_ssid, self.wifi_password)
            # Espera até conectar
            while not self.wifi.isconnected():
                time.sleep(1)
        print('Conexão Wi-Fi estabelecida:', self.wifi.ifconfig())
    
    def read_gas(self):
        # Retorna True se gás for detectado (assumindo que 0 indica detecção)
        return not self.sensor.value()
    
    def set_led_color(self, color):
        """
        Define a cor do LED RGB.
        :param color: Tuple contendo valores RGB, por exemplo, (255, 0, 0) para vermelho.
        """
        self.led[0] = color
        self.led.write()
    
    def turn_off_led(self):
        """Desliga o LED RGB."""
        self.set_led_color((0, 0, 0))  # Apaga o LED

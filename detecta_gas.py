from machine import Pin
import neopixel, time

#define o pinos de leitura e escrita
sensor_gas = Pin(5, Pin.IN) 
led = neopixel.NeoPixel(Pin(48), 1)

def define_cor_led(r, g, b):
    led[0] = (r, g, b)
    led.write()

# Função para verificar se há gás
def verifica_gas():
    if sensor_gas.value() == 1:  # Sensor detectou gás (assumindo valor 1 como positivo)
        print("Gás detectado!")
        define_cor_led(255, 0, 0)  # LED vermelho
    else:
        print("Nenhum gás detectado.")
        define_cor_led(0, 255, 0)  # LED verde

# Loop principal
while True:
    verifica_gas()
    time.sleep(1)
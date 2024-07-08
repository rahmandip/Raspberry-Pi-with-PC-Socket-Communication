import socket
import time
import board
import adafruit_dht

# Sensor data pin is connected to GPIO 4
sensor = adafruit_dht.DHT11(board.D4) # DHT11 sensor connected to GPIO 4 Type DHT22 if you are using DHT22

# Socket setup
bufferSize = 1024
ServerPort = 2222
myIP = '192.168.xx.xx' #Give the server IP

RPIsocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
RPIsocket.bind((myIP, ServerPort))
print('Server is up for listening...')

temperature_c = None
humidity = None

def read_sensor():
    global temperature_c, humidity
    try:
        temperature_c = sensor.temperature
        humidity = sensor.humidity
        print(f"Temperature: {temperature_c:.1f}ï¿½C, Humidity: {humidity:.1f}%")
    except RuntimeError as error:
        print(error.args[0])
    except Exception as error:
        sensor.exit()
        raise error

while True:
    read_sensor()
    RPIsocket.settimeout(3)  # Set timeout for 1 second to allow continuous sensor reading
    try:
        message, address = RPIsocket.recvfrom(bufferSize)
        message = message.decode('utf-8').upper()
        print("Received message:", message)
        print("Client Address:", address[0])

        # Prepare response based on client message
        if message == 'TEMP':
            response = f'Temperature: {temperature_c:.1f}ï¿½C'
        elif message == 'HUM':
            response = f'Humidity: {humidity:.1f}%'
        else:
            response = 'Invalid command'

        response = response.encode('utf-8')
        RPIsocket.sendto(response, address)

    except socket.timeout:
        # No message received, continue reading sensor
        continue

    time.sleep(1.0)

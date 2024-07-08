# Raspberry-Pi-with-PC-Socket-Communication
In this repository you will find a simple Socket Communication between Raspberry Pi and PC. The Raspi will continously read data from DHT sensor and send to pc over Socket communication.

Pinout of Raspberry Pi
![image](https://github.com/rahmandip/Raspberry-Pi-with-PC-Socket-Communication/assets/99471302/c0db7a53-76fd-4781-ad0b-914ca86c9ee8)

Circuit Connection
![image](https://github.com/rahmandip/Raspberry-Pi-with-PC-Socket-Communication/assets/99471302/9d08373b-bf49-4026-a5ae-3949259ec479)

!!DHT11 vs DHT22!!
![image](https://github.com/rahmandip/Raspberry-Pi-with-PC-Socket-Communication/assets/99471302/14866d0d-01dc-4379-a201-7bffd1544472)

DHT11 DATASHEET: https://www.mouser.com/datasheet/2/758/DHT11-Technical-Data-Sheet-Translated-Version-1143054.pdf

DHT22 DATASHEET: https://cdn-shop.adafruit.com/datasheets/Digital+humidity+and+temperature+sensor+AM2302.pdf

Here’s a list of parts you need to build the circuit (if you don’t have a DHT breakout board, you need a 4.7kOhm resistor):

Raspberry Pi board 
DHT11 or DHT22 temperature and humidity sensor
4.7k Ohm resistor or similar value (not needed if you have a DHT breakout board) This is called pull up resistor
Breadboard
Jumper wires

Installing the Adafruit_CircuitPython_DHT Library:
**pip install adafruit-circuitpython-dht**

If you get error on Raspi like:

**Traceback (most recent call last):
  File "/home/abdur/Desktop/Python/dht_to_pc.py", line 144, in <module>
    read_sensor()
  File "/home/abdur/Desktop/Python/dht_to_pc.py", line 141, in read_sensor
    raise error
  File "/home/abdur/Desktop/Python/dht_to_pc.py", line 136, in read_sensor
    print(f"Temperature: {temperature_c:.1f}ï¿½C, Humidity: {humidity:.1f}%")
TypeError: unsupported format string passed to NoneType.__format__**

Then run the code again.
Otherwise choose the port no manually in **RPIsocket.bind((myIP, xxxx))  # Bind to any available port** this part of the code

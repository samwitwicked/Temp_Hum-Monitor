#The code from https://people.csail.mit.edu/albert/bluez-intro/x232.html was used to connect to the server and transfer data. 
import bluetooth
import Adafruit_DHT
import time
import datetime
from time import sleep
import os
sensor=11
pin=3

bd_addr = "B8:27:EB:4A:B6:56" #Abishek

port = 1

sock=bluetooth.BluetoothSocket( bluetooth.RFCOMM )
sock.connect((bd_addr, port))
while True:
    humidity,temperature=Adafruit_DHT.read_retry(sensor,pin)
    currenttime=datetime.datetime.now()
    sock.send(str(currenttime) + " SensorID = Manjunath, " +"Temperature = {}, Humidity = {} ".format(temperature, humidity))
    time.sleep(5)
sock.close()
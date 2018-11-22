#The code from https://people.csail.mit.edu/albert/bluez-intro/x232.html was used to connect to the server and transfer data. 
#r7insight downloaded from https://pypi.org/project/r7insight_python/
import bluetooth
from r7insight import R7InsightHandler
import logging
import time
import Adafruit_DHT
import datetime 


sensor = 11
pin = 23

server_sock=bluetooth.BluetoothSocket( bluetooth.RFCOMM )

port = 1
server_sock.bind(("",port))
server_sock.listen(1)

log = logging.getLogger('r7insight')
log.setLevel(logging.INFO)

#Insightops Log Token
test = R7InsightHandler('24568bbf-d50f-4922-b2fc-aede9a941f98', 'eu')


log.addHandler(test)

client_sock,address = server_sock.accept()
print("Accepted connection from ",address)

while True:
    
    #Record After every 5 sec
    data = client_sock.recv(1024)
    print("received [%s]" % data)
    
    #Reading Data from RPi 1 Sensor
    log.info(data)
    
    #Reading Data from RPi 2 Sensor(Server)
    ts = str(datetime.datetime.now())
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    
    log.info(ts + " SensorID = Sam" + " Temperature = {}, Humidity= {} ".format(temperature,humidity))
#client_sock.close()





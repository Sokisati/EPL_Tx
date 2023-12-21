import socket
import time
import json


class dataPack:
    def __init__(self, teamNumber, dataPacketNumber,dateAndTime, pressure,altitude, descentSpeed, temperature, batteryVoltage, gpsLat, gpsLong, gpsAlt, pitch, roll, yaw):
        self.teamNumber = teamNumber
        self.dataPacketNumber= dataPacketNumber
        self.gondermeSaatiVeTarih =dateAndTime
        self.altitude = altitude
        self.pressure = pressure
        self.descentSpeed = descentSpeed
        self.temperature = temperature
        self.batteryVoltage = batteryVoltage
        self.gpsLat = gpsLat
        self.gpsLong = gpsLong
        self.gpsAlt = gpsAlt
        self.pitch = pitch
        self.roll = roll
        self.yaw = yaw
       

pc_ip = '127.0.0.1'  
port = 12345

dataPacketNumber = 0
pressure = 10
altitude = 8
temperature = 10
dateAndTime = 'yes'
teamNo = 1488
descentSpeed = 15
gpsLat = 10
gpsLat = 10
gpsLong = 10
gpsAlt = 20
pitch = 2
yaw = 3

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    sock.connect((pc_ip, port))
    print("Baglanti kuruldu")

    while True:
        data = dataPack(
            teamNumber=10,
            dataPacketNumber=dataPacketNumber,
            pressure=pressure,
            altitude=altitude,
            temperature=temperature,
            yaw = 3,
            pitch = 2,
            gpsAlt = 20,
            gpsLong = 10,
            gpsLat = 10,
            descentSpeed = 15,
            batteryVoltage=20,
            roll =10,
            dateAndTime = 'yes',
            
        )
        dataPacketNumber += 1
        if temperature>2:
            temperature = temperature -1
           
        elif temperature==2:
            temperature = 10

        data_json = json.dumps(data.__dict__)
        sock.send(data_json.encode())

        time.sleep(1)  

except KeyboardInterrupt:
    print("Kesildi")

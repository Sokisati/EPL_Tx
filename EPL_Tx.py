# -- coding: utf-8 --
import socket
import time
import json
import random
import numpy as np

def encryption_function(key_vector, value_to_enc, data_packet_id):
    key_index = data_packet_id % len(key_vector)
    enc_value = value_to_enc * key_vector[key_index] - key_vector[key_index]
    return enc_value

#buradaki anahtar rx ile ayný olmalý
key_vector = [16,81,33,32,5,15,13,71,43,8,31,72,4,38,71,19]

#TODO: anahtar raspberry pi ve rx'in gerçekleþtiði bilgisayarýn clock degerlerine bakip sene,ay,hafta,gun ve dakikaya gore otomatik olusmalý
#kritik sey su ki, bahsettigim parametreler her iki bilgisayarda da tam olarak ayný olmali


class GonderilecekVeriler:
    def __init__(self, takimNo, veriPaketNo, gondermeSaatiVeTarih, basinc,yukseklik, inisHizi, sicaklik, pilGerilimi, gpsLat, gpsLong, gpsAlt, pitch, roll, yaw, donusHizi):
        self.takimNo = takimNo
        self.veriPaketNo = veriPaketNo
        self.gondermeSaatiVeTarih = gondermeSaatiVeTarih
        self.yukseklik = yukseklik
        self.basinc = basinc
        self.inisHizi = inisHizi
        self.sicaklik = sicaklik
        self.pilGerilimi = pilGerilimi
        self.gpsLat = gpsLat
        self.gpsLong = gpsLong
        self.gpsAlt = gpsAlt
        self.pitch = pitch
        self.roll = roll
        self.yaw = yaw
        self.donusHizi = donusHizi
        

pc_ip = socket.gethostbyname(socket.gethostname())

#bu port degistirilebilir ama kalsin
port = 12345
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
veriPaketNo = 0;

basinc = 5
yukseklik = 8
inisHizi = 16
sicaklik = 2
pilGerilimi = 12
gpsLat=35.123456
gpsLong=139.654321
gpsAlt=100.0
pitch=0.0
roll=0.0
yaw=0.0
donusHizi=10.0


try:
    sock.connect((pc_ip, port))
    print("Hedef pc'ye baglanildi")
    while True:
        
      
        data = GonderilecekVeriler(
            
            takimNo=31,
            veriPaketNo=veriPaketNo,
            gondermeSaatiVeTarih="2023-10-20 12:00:00",
            basinc=encryption_function(key_vector,basinc,veriPaketNo),
            yukseklik=encryption_function(key_vector,yukseklik,veriPaketNo),
            inisHizi=encryption_function(key_vector,inisHizi,veriPaketNo),
            sicaklik=encryption_function(key_vector,sicaklik,veriPaketNo),
            pilGerilimi=encryption_function(key_vector,pilGerilimi,veriPaketNo),
            gpsLat=encryption_function(key_vector,gpsLat,veriPaketNo),
            gpsLong=encryption_function(key_vector,gpsLong,veriPaketNo),
            gpsAlt=encryption_function(key_vector,gpsAlt,veriPaketNo),
            pitch=0.0,
            roll=0.0,
            yaw=0.0,
            donusHizi=10.0,
           
        )
        veriPaketNo += 1
       
        
        data_json = json.dumps(data.__dict__)

        sock.send(data_json.encode())

        time.sleep(1)
except KeyboardInterrupt:
    print("Baglanti kesildi.")
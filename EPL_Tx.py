# -- coding: utf-8 --
import socket
import time
import json

class GonderilecekVeriler:
    def __init__(self, takimNo, veriPaketNo, gondermeSaatiVeTarih, basinc, inisHizi, sicaklik, pilGerilimi, gpsLat, gpsLong, gpsAlt, pitch, roll, yaw, donusHizi):
        self.takimNo = takimNo
        self.veriPaketNo = veriPaketNo
        self.gondermeSaatiVeTarih = gondermeSaatiVeTarih
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
        

#buraya baglanilacak pc'nin ip'si girilecek (cmd->ipconfig->ip4)
pc_ip = '10.45.69.108' 

#bu port degistirilebilir ama kalsin
port = 12345
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
veriPaketNo = 0;

try:
    sock.connect((pc_ip, port))
    print("Hedef pc'ye baglanildi")
    while True:
      
        data = GonderilecekVeriler(
            takimNo=31,
            veriPaketNo=veriPaketNo,
            gondermeSaatiVeTarih="2023-10-20 12:00:00",
            basinc=1013.25,
            inisHizi=5.0,
            sicaklik=25.0,
            pilGerilimi=12.0,
            gpsLat=35.123456,
            gpsLong=139.654321,
            gpsAlt=100.0,
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
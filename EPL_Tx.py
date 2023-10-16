# -- coding: utf-8 --
import socket
import time

#buraya baglanilacak pc'nin ip'si girilecek (cmd->ipconfig->ip4)
pc_ip = '192.168.128.235' 

#bu port degistirilebilir ama kalsin
port = 12345
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    sock.connect((pc_ip, port))
    print("Hedef pc'ye baglanildi")
    while True:
        sicaklik = 31.69
        yukseklik = 420
        basinc = 1013.25
        data = f"sicaklik: {sicaklik} C, yukseklik: {yukseklik} m, basinc: {basinc} hPa"
        sock.send(data.encode())
        time.sleep(5)
except KeyboardInterrupt:
    print("Baglanti kesildi.")
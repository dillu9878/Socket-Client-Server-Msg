import socket
import sys
import os

SERVER_HOST = "127.0.0.1"
SERVER_PORT = 8888 #65535
SERVER_ADDRESS = (SERVER_HOST, SERVER_PORT)

# UDP
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print('UDP Socket Created')

# connect

sock.connect(SERVER_ADDRESS)
print('Connected to server')

messgae = "hi from client-2"
sock.sendto(messgae.encode(), SERVER_ADDRESS)

data, addr = sock.recvfrom(1024)

print(f'data received: {data.decode()}; from addr: {addr}')

while 1:
    pass

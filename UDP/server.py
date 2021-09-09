import socket
import sys
import os

SERVER_HOST = "127.0.0.1"
SERVER_PORT = 8888 #65535
SERVER_ADDRESS = (SERVER_HOST, SERVER_PORT)

# UDP
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print('UDP Socket Created')


sock.bind(SERVER_ADDRESS)
print('Socke bind to the address: ', SERVER_ADDRESS)

while 1:
    data, addr = sock.recvfrom(1024)
    if data:
        print(f'Recvd data: {data.decode()}; from addr: {addr}')
        messgae = "Hello from server..."
        sock.sendto(messgae.encode(), addr)





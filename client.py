import socket
import sys
import os

# IP address of server (for now, loopback address)
SERVER_IP = '127.0.0.1'

# Port number assigned to server
SERVER_PORT = 8881
SERVER_ADDRESS = (SERVER_IP, SERVER_PORT)

def coonect_to_server(SERVER_ADDRESS):
    sock = socket.socket()
    sock.connect(SERVER_ADDRESS)
    return sock

def send_msg(sock, msg):
    data = str(msg)

    sock.sendall(data.encode())

    return 1

def recv_msg(sock):

    recv_data = sock.recv(1024)
    recv_data = recv_data.decode()

    return recv_data

def main():
    sock = coonect_to_server(SERVER_ADDRESS)

    while 1:
        msg = input("Enter msg to send: ")
        if msg == 'Bye':
            break

        print(f"Received Msg: ", end='')
        send_msg(sock, msg)
        msg = recv_msg(sock)
        print(msg)
        if msg == 'Bye':
            break


    sock.close()

if __name__ == '__main__':
    main()



import socket
import sys
import os

SERVER_HOST = "127.0.0.1"
SERVER_PORT = 8881
SERVER_ADDRESS = (SERVER_HOST, SERVER_PORT)




# Create a Socket ( connect two computers)
def create_socket():
    try:

        sock = socket.socket()
        print("Socket Creation Done")
        return sock
    except socket.error as msg:
        print("Socket creation error: " + str(msg))


# Binding the socket and listening for connections
def bind_socket(sock, SERVER_ADDRESS):
    try:
        print("Binding the Port: " + str(SERVER_ADDRESS[1]))

        sock.bind(SERVER_ADDRESS)
        sock.listen(5)
        print("Socket Listening...")

    except socket.error as msg:
        print("Socket Binding error" + str(msg) + "\n" + "Retrying...")
        bind_socket(sock, SERVER_ADDRESS)


# Establish connection with a client (socket must be listening)

def socket_accept(sock):
    conn, address = sock.accept()
    print("Connection has been established! |" + " IP " + address[0] + " | Port" + str(address[1]))
    return conn
    # send_msg(conn)
    # conn.close()

# Send commands to client/victim or a friend
def send_msg(conn):
    while True:
        print("Client:", end='')
        st = conn.recv(1024)
        print(st.decode('utf-8'))
        cmd = input('Server:')

        if cmd == 'Bye':
            break

        if len(str.encode(cmd)) > 0:
            conn.send(str.encode(cmd))




def main():
    sock = create_socket()
    bind_socket(sock, SERVER_ADDRESS)
    conn = socket_accept(sock)
    send_msg(conn)
    conn.close()
    sock.close()
    sys.exit()

if __name__ == '__main__':
    main()

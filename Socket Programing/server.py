import socket
import threading

HEADER = 64 #fixed length header first message to server always 64 bytes
FORMAT ='utf-8'
PORT = 5050
#get ip of the device
SERVER = socket.gethostbyname(socket.gethostname())
print(SERVER)
#create a tuple to hold the serverip and the port
ADDR = (SERVER, PORT)
print(ADDR)

DISCONNECT_MESSAGE = "!DISCONNECT"

#create a new socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#Bind socket to an address - in a tuple(serverip, port)
server.bind(ADDR)

#for each client
def handle_client(conn, addr):
    print(f"[SERVER:NEW CONNECTION] {addr} connected")
    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT) #receive info from client 
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MESSAGE:
                connected = False
            print(f"[SERVER:{addr} {msg}]")


#server start listening for new connections
def start():
    server.listen()
    print(f"[SERVER:LISTENING] Server is listening on {SERVER}")
    while True:
        conn, addr = server.accept() #when new connection is made store port and ip addr of src
        thread = threading.Thread(target=handle_client, args=(conn, addr)) #start thread to handle communication with new connection-pass info th the handle_client function
        thread.start()
        print(f"[SERVER:ACTIVE CONNECTIONS] {threading.activeCount() - 1}")

print("[SERVER:STARTING] server is starting ...")
start()
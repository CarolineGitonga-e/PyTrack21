import socket
import threading

HEADER = 64
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER = socket.gethostbyname(socket.gethostname())
PORT = 5050
#create new socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#bind socket to addr
ADDR = (SERVER,PORT)
server.bind(ADDR)
print(SERVER +":" + str(PORT))



#listen for clients
def start():
    server.listen()
    print("[SERVER: LISTEnING] Server is listening ....")
    while True:
        srcconn, srcaddr = server.accept()
        print("!!!!!!!!!!!!!!!CLIENT INFO!!!!!!!!!!!!!!!!!!!!!!!!")
        print(f"[SERVER: CONNECTION INFO]{srcconn}")
        print(f"[SERVER: CLIENT ADDR]{srcaddr}")
        print("!!!!!!!!!!!!!!! END CLIENT INFO!!!!!!!!!!!!!!!!!!!!!!!!")
        #pass info to handle_client function
        thread = threading.Thread(target=handle_client, args=(srcconn, srcaddr)) #start thread to handle communication with new connection-pass info th the handle_client function
        thread.start()
        print(f"[SERVER: ACTIVE CONNECTIONS] {threading.activeCount() - 1}")

#handle clients
def handle_client(conn, addr):
    print(f"[SERVER: NEW CONNECTION] {addr} added")
    connected = True
    while connected:
       message_length = conn.recv(HEADER).decode(FORMAT)
       if message_length:
           message_length = int(message_length)
           msg = conn.recv(message_length).decode(FORMAT)
           if msg == DISCONNECT_MESSAGE:
               connected = False
           print(f"[SERVER: Client {addr} has entered: \"{msg}\"]")
           toclient = "Received your name: " + msg
           conn.send(toclient.encode(FORMAT))
           
#start server
print("[SERVER: STARTING] Server is starting ....")
start()

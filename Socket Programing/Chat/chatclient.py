import socket

FORMAT = 'utf-8'
HEADER = 64
SERVER = socket.gethostbyname(socket.gethostname())
PORT = 5050
#create new socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#b
ADDR = (SERVER,PORT)
client.connect(ADDR)

#sending messsages
clientmsg = input("Enter your name: ")

def send(msg):
    message = msg.encode(FORMAT)
    message_length = len(message)
    send_length = str(message_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    print(client.recv(2048).decode(FORMAT))

send(clientmsg)
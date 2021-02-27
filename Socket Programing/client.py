import socket

HEADER = 64
FORMAT ='utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
PORT = 5050
#get ip of the device
SERVER = socket.gethostbyname(socket.gethostname())
print(SERVER)
ADDR = (SERVER,PORT)
print(ADDR)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    message = msg.encode(FORMAT)
    message_length = len(message)
    send_length = str(message_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)

send("Carolinah")
send("Carolinah222")
send(" Hello Carolinah")
send(DISCONNECT_MESSAGE)
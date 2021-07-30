import socket

PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER,PORT)
FORMAT = 'utf-8'
HEADER = 64
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(ADDR)


def send_message(message):
    msg = message.encode(FORMAT)
    msg_len = len(msg)
    send_len = str(msg_len).encode(FORMAT)
    send_len += b' ' * (HEADER - len(send_len))
    client.send(send_len)
    client.send(msg)
    print(client.recv(2048).decode(FORMAT))


for i in range(10):
    send_message(str(input("Please put and ENTER")))

import socket
import threading
##pickling to send complete object : need to try

disconnect = 'quit'
HEADER = 64
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER,PORT)
FORMAT = 'utf-8'
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(ADDR)

def client_handler(conn,addr):
    connected = True
    while connected:
        msg_len = conn.recv(HEADER).decode(FORMAT)
        msg_len = int(msg_len)
        msg = conn.recv(msg_len).decode(FORMAT)
        if(disconnect == 'quit'):
            connected = False
        print(msg)
        conn.send("RECEIVED".encode(FORMAT))
        conn.close()
def start():
    #print(f"[SERVER START] Server is starting {SERVER}")
    print(f"[SERVER LISTING] Server is listening {SERVER}")
    server.listen()
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=client_handler, args=(conn,addr))
        thread.start()
        print(f"[THREAD COUNT] Active threads {threading.activeCount()}")

print(f"[STARTING] Server id starting....")
start()
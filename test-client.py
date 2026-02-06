
import socket
from threading import Thread
  
client = socket.socket()
client.connect(("172.28.142.121", 5555))

print("Connecting...")
def send(client):
    while True:
        message = input(">> ")
        client.send(message.encode())       # отправляем данные серверу

def recive(client):
    while True:
        data = client.recv(1024)
        print(data.decode())

th1 = Thread(target=send, args=(client,))
th2 = Thread(target=recive, args=(client,))
th1.start()
th2.start()

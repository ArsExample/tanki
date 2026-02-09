import socket
import queue
import threading
from config import IP, PORT

class Client:
    def __init__(self):
        self.sock = socket.socket()
        self.msg_queue = queue.Queue()
        self.recieve_thread = None

        self.stop_recieve_loop = False

    def connect(self):
        print("Trying to connect to server...")
        try:
            self.sock.connect((IP, PORT))
            print("Connected.")
        except Exception as e:
            print(f"Connection failed with error: {e}")

    def start_recieve(self):
        # запустить поток
        self.recieve_thread = threading.Thread(target=self.recieve_loop)

    def stop_recieve(self):
        self.stop_recieve_loop = True
        

    def recieve_loop(self):
        while not self.stop_recieve_loop:
            data = self.sock.recv(1024).decode()
            self.msg_queue.put(data)

        self.stop_recieve_loop = False
        print("Recieving stopped")

    def send_msg(self, msg):
        self.sock.send(msg.encoded())

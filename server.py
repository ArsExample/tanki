import socket
from threading import Thread

def con11(con1, con2):
    while True:
        message = con1.recv(1024)       
        con2.send(message)
        print(message.decode())



def con22(con1 , con2):
    while True:
        message = con2.recv(1024)
        con1.send(message)
        print(message.decode())



server = socket.socket()            # создаем объект сокета сервера
hostname = "localhost"     # получаем имя хоста локальной машины
port = 5555 # устанавливаем порт сервера
server.bind((hostname, port))       # привязываем сокет сервера к хосту и порту
while 1:

    server.listen(2)                    # начинаем прослушиваение входящих подключений
     
    print("Server starts")

    con1, addr1 = server.accept() # принимаем клиента e E`E `
    print("client address: ", addr1)
    con2, addr2 = server.accept()
    print("client address: ", addr2)

    th1 = Thread(target = con11, args = (con1, con2,))
    th2 = Thread(target = con22, args = (con1, con2,))
    th1.start()
    th2.start()


#con1 = 1024
#con2 = 1024

#while 1:
#    data = con1.recv()
#    con2.send(data)

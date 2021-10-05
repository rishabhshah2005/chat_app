import socket
import threading

ip = '127.0.0.1'
port = 5555

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((ip, port))
server.listen()
print('Server started....')

clients = []
names = []


def send_message(msg, secret=False):
    if secret:
        for cli in clients:
            cli.send(msg)

    else:
        for cli in clients:
            ind = clients.index(cli)
            nic_nm = names[ind]
            cli.send(msg.encode('utf-8'))


def incoming(cli):
    while True:
        try:
            mes = cli.recv(1024)
            send_message(mes.decode('utf-8'))

        except:
            ind = clients.index(cli)
            clients.remove(cli)
            cli.close()
            nickname = names[ind]
            send_message(f"{nickname} left the chat!!".encode('utf-8'), secret=True)
            names.remove(nickname)
            break


def receive():
    while True:
        clnt, add = server.accept()
        print(f"{add} has connected!!")
        clnt.send("NICK".encode('utf-8'))
        nickname = clnt.recv(1024).decode('utf-8')
        clients.append(clnt)
        names.append(nickname)
        print(f"Name of {add} is {nickname}")
        send_message(f"{nickname} has joined the chat!!".encode('utf-8'), secret=True)
        clnt.send("Connection confirmed!!".encode('utf-8'))

        thr = threading.Thread(target=incoming, args=(clnt,))
        thr.start()


receive()














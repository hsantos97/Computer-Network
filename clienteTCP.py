from socket import *

host = '127.0.0.1'
port = 5050

cli = socket(AF_INET, SOCK_STREAM)
cli.connect((host, port))

while 1:
    msg = cli.recv(1024)
    print(msg.decode())
    if(msg.decode() == "Fechando conexão !\n"):
        exit()
    msg = input("Resposta: ")
    cli.send(msg.encode())
import socket

cliente_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

try:
    cliente_sock.settimeout(10)
    msg = input("Uma Mensagem: ")
    cliente_sock.sendto(msg.encode(), ('127.0.0.1', 5050))
    msg, endereco = cliente_sock.recvfrom(2048)
    print('Mensagem recebida: ',msg.decode())
except socket.timeout:
    print('Tempo esgotado !')
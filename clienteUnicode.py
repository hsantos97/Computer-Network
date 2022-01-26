import socket

cliente_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

try:
    while(1):
        cliente_sock.settimeout(10)

        msg = input("Mensagem para o servidor: ")
        cliente_sock.sendto(msg.encode(), ('127.0.0.1', 5050))

        msg, endereco = cliente_sock.recvfrom(2048)
        print('Mensagem recebida pelo servidor: ',msg.decode())
        
        msg = input("Informe um valor: ")
        cliente_sock.sendto(msg.encode(), ('127.0.0.1', 5050))

except socket.timeout:
    print('Tempo esgotado !')
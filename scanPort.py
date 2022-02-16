import socket
import sys

if len(sys.argv) < 2:
    print('Escolha um parametro ex: {} www.youtube.com'.format(sys.argv[0]))
    exit()

target = sys.argv[1]
print('Escaneando host com ip {}'.format(target))

abertas  = 0
fechadas = 0

for porta in range(1, 7000):
    c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        c.settimeout(10)
        r = c.connect_ex((target, porta))

        if r == 0:
            print(f'Porta {porta} Aberta. {socket.getservbyport(porta)}'+'\n')
            abertas += 1
        else:
            #print(f'Porta {porta} Fechada.'+'\n')
            fechadas += 1
    except socket.timeout:
        print('Tempo esgotado !')

print('Portas abertas {} -- Portas Fecahdas {}'.format(abertas, fechadas))

c.close()
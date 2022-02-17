import socket
import sys

if len(sys.argv) < 2:
    print('Escolha um parametro ex: python3 {} www.youtube.com'.format(sys.argv[0]))
    exit()

target = sys.argv[1]
print('Escaneando host com ip {}'.format(target))
#contador para portas
abertas  = 0
fechadas = 0
   
for porta in range(1, 65535): 
    c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    c.settimeout(1)  
    r = c.connect_ex((target, porta))

    if r == 0:
        try: #para portas que o getservbyport não encontra ex: porta 7070 - realserver
            print(f'Porta {porta} Aberta. {socket.getservbyport(porta)}'+'\n')
            abertas += 1
        except:
            pass
    elif r == 11:
        print('TEMPO ESGOTADO PARA PORTA', porta)
    else:
        #print(f'Porta {porta} Fechada.'+'\n')
        fechadas += 1

c.close()

print('Portas abertas {} -- Portas Fechadas {}'.format(abertas, fechadas))

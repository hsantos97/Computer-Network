import socket

def retornaListaRotulo(msg, rotulo):
    for chave in rotulo.keys():
        if(chave == msg):
            return rotulo[chave]

def rotulos():
    rotulo = {
    'dinheiro':['U+1F4B0', 'U+1F4B8', 'U+1F911', 'U+3438'],
    'rato':['U+1F401', 'U+1F42D', 'U+1F5B1', 'U+1FAA4'],
    'cachorro':['U+1F415', 'U+1F436', 'U+1F9AE', 'U+1F32D'],
    'gato':['U+1F408', 'U+1F431', 'U+1F638', 'U+1F639', 'U+1F63B', 'U+1F640'],
    'macaco':['U+1F412', 'U+1F648', 'U+1F649', 'U+1F64A'],
    'estrela':['U+2605', 'U+2606', 'U+269D', 'U+272F', 'U+2730']
    }
    return rotulo

def qtdCaracter(rotulos):
    cont = 0
    for chave in rotulos.keys():
        cont = cont + len(rotulos[chave])

    return cont



def main():
    server_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_sock.bind(('', 5050))
    print("Servidor associado á porta: ", server_sock.getsockname()[1])

    while(1):
        rotulo = rotulos()
        msg, endereco = server_sock.recvfrom(2048)
        print('Mensagem do {}: {}'.format(str(endereco), msg.decode()))
        msg = msg.decode()
        msgSaida = str(retornaListaRotulo(msg, rotulo))
        msgSaida += "\nQuantidade de caracter: " + str(qtdCaracter(rotulo))
        msgSaida += "\nListagem dos rotulos: " + str(rotulo)
        server_sock.sendto(msgSaida.encode(), endereco)

    server_sock.close()

main()
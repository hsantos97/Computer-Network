from socket import *

def qtdCaracter(rotulos):
    cont = 0
    for chave in rotulos.keys():
        cont = cont + len(rotulos[chave])

    return cont

def retornaListaRotulo(msg, rotulo):
    for chave in rotulo.keys():
        if(chave == msg):
            return rotulo[chave]

def cadastrar(chave, valor, rotulo):
    
    if chave in rotulo:
        rotulo[chave].append(valor)
    else:
        rotulo[chave] = [valor]
        
    return rotulo

def remover(chave, rotulo):
    
    if chave in rotulo:
        rotulo.pop(chave)
        return rotulo
    else:
        return "Chave não encontrada!\n"


def main():
    host = 'localhost'
    port = 5050

    print(f'HOST: {host} , PORT {port}')
    serv = socket(AF_INET, SOCK_STREAM)
    serv.bind((host, port))
    serv.listen()
 
    rotulo = {
    'dinheiro':['U+1F4B0', 'U+1F4B8', 'U+1F911', 'U+3438'],
    'rato':['U+1F401', 'U+1F42D', 'U+1F5B1', 'U+1FAA4'],
    'cachorro':['U+1F415', 'U+1F436', 'U+1F9AE', 'U+1F32D'],
    'gato':['U+1F408', 'U+1F431', 'U+1F638', 'U+1F639', 'U+1F63B', 'U+1F640'],
    'macaco':['U+1F412', 'U+1F648', 'U+1F649', 'U+1F64A'],
    'estrela':['U+2605', 'U+2606', 'U+269D', 'U+272F', 'U+2730']
    }

    con, adr = serv.accept()
    case = "\n1-Listagem de rotulos\n2-Escolher Rotulo\n3-Quantidade de caracter\n4-Cadastrar Chave/caracter\n5-Remover caracter da lista\n0-Sair"
    con.sendall(case.encode())
    while 1:

        msg = con.recv(1024)
        print(msg.decode())

        if(msg.decode() == '0'):
            msgEnv = "Fechando conexão !\n"
            print(msgEnv)
            con.sendall(msgEnv.encode())
            con.close()
            exit()
    
        elif(msg.decode() == '2'):
            nomeRotulo = 'Nome do rotulo:\n'
            con.sendall(nomeRotulo.encode())
            msg = con.recv(1024)
            print(msg.decode())
            retornoFun = str(retornaListaRotulo(msg.decode(), rotulo))+"\n"+case
            con.sendall(retornoFun.encode())
            
        
        elif(msg.decode() == '3'):            
            qtd = "Quantidade: "+str(qtdCaracter(rotulo))+"\n"+case
            con.sendall(qtd.encode())
            

        elif(msg.decode() == '1'):
            rot = "Rotulos:" + str(rotulo)+"\n"+case
            con.sendall(rot.encode())
            
        
        elif(msg.decode() == '4'):
            msgEnv = "Nome do rotulo: \n"
            con.sendall(msgEnv.encode())
            msg = con.recv(1024)
            chave = msg.decode()
            msgEnv = "Caracter: \n"
            con.sendall(msgEnv.encode())
            msg = con.recv(1024)
            caracter = msg.decode()
            rotulo = cadastrar(chave, caracter, rotulo)
            cadastro = "Rotulo cadastrado: "+ str(rotulo)+"\n"+case
            con.sendall(cadastro.encode())
            
            
        elif(msg.decode() == '5'):
            msgEnv = "Nome do rotulo: \n"
            con.sendall(msgEnv.encode())
            msg = con.recv(1024)
            chave = msg.decode()
            rotulo = remover(chave, rotulo)
            msgEnv = str(rotulo)+case
            con.sendall(msgEnv.encode())


        else:
            msgEnv = "OPÇÃO NÃO ENCONTRADA\n"
            con.sendall(msgEnv.encode())
            break 
            

main()       
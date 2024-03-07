import socket
import threading
from datetime import datetime

"""def conexao_cliente(client,address):
    
    while (True):    
        data = client.recv(2048)
        
        data_e_hora_atuais = datetime.now()
        hora = data_e_hora_atuais.strftime('%H:%M:%S')
        
        mensagem = data.decode()
        if (mensagem!='0'):
            client.sendall(hora.encode())
        else:
            client.sendall('0'.encode())
            break
    #Fechando o socket
    client.close()"""

def verificarPalavra(client,address,choosen_Word):
    print('entrou')
    #decodificando dados    
    data = client.recv(2048)
    word = data.decode()
    vetor = ""

    if(len(word) == len(choosen_Word)): #verificando se possui mesmo tamanho
        for i in range(len(choosen_Word)): #verificando se as posições batem
            if word[i] == choosen_Word[i]:
                vetor = vetor + '1'
                print('verde')
                #print('colocar aqui o marcado verde')
            elif word[i] in choosen_Word:
                vetor = vetor + '2'
                print('laranja')
        print('ok')
    else:
        vetor = vetor + '0'
        print('deu pau!')

    client.sendall(vetor.encode())
    client.close()



sock = socket.socket(socket.AF_INET,  socket.SOCK_STREAM)
    
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server_address = ('localhost', 20001)
print ("Iniciando servidor na porta %s %s" % server_address)
#Reservando porta
sock.bind(server_address)
#Escutando na porta reservada
sock.listen(1)

#Iniciando protocolo

choosen_Word = 'comer'

while True:
    client, address = sock.accept()
    conexao = threading.Thread(target=verificarPalavra,args=(client,address,choosen_Word,))
    conexao.start()
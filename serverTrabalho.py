import socket
import threading
from datetime import datetime

def verificarPalavra(client,address,choosen_Word):
    print('entrou')
    #decodificando dados    
    data = client.recv(2048)
    word = data.decode()
    
    #client.send(bytes(vetor))

    if(len(word) == len(choosen_Word)): #verificando se possui mesmo tamanho

        #cria o vetor no tamanho da palavra
        vetor = []
        for i in range(len(choosen_Word)):
            vetor.append(0)
        
        for i in range(len(choosen_Word)): #verificando se as posições batem
            if word[i] == choosen_Word[i]:
                vetor[i] = 1
                print('verde')
            elif word[i] in choosen_Word:
                vetor[i] = 2
                print('laranja')
        print('fim da verificacao')
    else:
        print('Palavras de tamanhos diferentes!')

    client.sendall(bytes(vetor))
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
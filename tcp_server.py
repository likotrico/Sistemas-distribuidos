import socket
import _thread

HOST = '127.0.0.1'     # Endereco IP do Servidor
PORT = 5000            # Porta que o Servidor está

def verificarPalavra(con,choosen_Word, msg):
    
    print('Mensagem recebida!')
    word = msg
    print(f"word:{word}")

    if(len(word) == len(choosen_Word)): #verificando se possui mesmo tamanho
        #cria o vetor no tamanho da palavra
        vetor = []
        for i in range(len(choosen_Word)):
            vetor.append(0)
        
        for i in range(len(choosen_Word)): #verificando se as posições batem
            if word[i] == choosen_Word[i]:
                vetor[i] = 1
                #print('verde')
            elif word[i] in choosen_Word:
                vetor[i] = 2
                #print('laranja')
        print('fim da verificacao')
        
    else:
        print('Palavras de tamanhos diferentes!')

    print(f"bytes(vetor):{bytes(vetor)}")
    con.sendall(bytes(vetor))
    vetor.clear()

##############################

def conectado(con, cliente): # Função chamada quando uma nova thread for iniciada

   print('\nCliente conectado:', cliente)

   choosen_word = 'comer'

   while True:

       # Recebendo as mensagens através da conexão
       msg = con.recv(1024)
       if not msg:
           break

       print('\nCliente..:', cliente)
       print('Mensagem.:', msg)
       verificarPalavra(con, choosen_word, msg.decode())

   print('\nFinalizando conexao do cliente', cliente)
   con.close()
   _thread.exit()




tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
orig = (HOST, PORT)

tcp.bind(orig) # Colocando um endereço IP e uma porta no Socket
tcp.listen(1) # Colocando o Socket em modo passivo

print('\nServidor TCP concorrente iniciado no IP', HOST, 'na porta', PORT)

while True:
   con, cliente = tcp.accept() # Aceitando uma nova conexão

   print('\nNova thread iniciada para essa conexão')

   _thread.start_new_thread(conectado, tuple([con, cliente])) # Abrindo uma thread para a conexão

# Fechando a conexão com o Socket
tcp.close()
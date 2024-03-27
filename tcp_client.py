import socket

HOST = '127.0.0.1'     # Endereço IP do Servidor
PORT = 5000            # Porta que o Servidor está

# Criando a conexão
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
destino = (HOST, PORT)
tcp.connect(destino)


print('\nAdivinhe a palavra escolhida!')
print('Para sair use CTRL+X\n')

mensagem = input() # Recebendo a mensagem do usuário final pelo teclado

# Enviando a mensagem para o Servidor TCP através da conexão
while mensagem != '\x18':

   tcp.send(str(mensagem).encode())

   resposta = tcp.recv(1024)
   print(list(resposta))
 
   mensagem = input()

# Fechando o Socket
tcp.close()
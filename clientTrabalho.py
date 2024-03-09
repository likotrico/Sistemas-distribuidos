import socket
import threading
import time

def receber_mensagens(sock):
    while (True):
        data = sock.recv(2048)
        #mensagem = data.decode()
        mensagem = list(data)
        if(len(mensagem) != 0):
            print(mensagem)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
server_address = ('localhost', 20001)
print ("Conectando %s porta %s" % server_address)
#Conectando ao servidor
sock.connect(server_address)
recepcao = threading.Thread(target=receber_mensagens,args=(sock,))
recepcao.start()
while (True): 

    message = input("Adivinhe uma palavra com 5 letras")
    
    if message=='0':
        break

    #Enviando mensagem ao servidor
    sock.sendall(message.encode('utf-8'))
    
    
recepcao.join()
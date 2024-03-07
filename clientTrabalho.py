import socket
import threading

def receber_mensagens(sock):
    while (True):
        data = sock.recv(2048)
        mensagem = data.decode()
        if mensagem!='0':
            #Imprimindo a mensagem recebida
            print(data.decode())
        else:
            sock.close()
            break

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
server_address = ('localhost', 20001)
print ("Conectando %s porta %s" % server_address)
#Conectando ao servidor
sock.connect(server_address)
recepcao = threading.Thread(target=receber_mensagens,args=(sock,))
recepcao.start()
while (True):    
    message = input("Envie qualquer mensagem para visualizar as horas.")
    #Enviando mensagem ao servidor
    sock.sendall(message.encode('utf-8'))
    #message1 = sock.recv(2048)
    #message1 = message1.decode()
    if message=='0':
        break

recepcao.join()
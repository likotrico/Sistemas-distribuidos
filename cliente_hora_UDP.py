import socket
import threading

def receber_mensagens(sock):
    data = sock.recv(2048)
    mensagem = data.decode()
    #Imprimindo a mensagem recebida
    print(mensagem)
    sock.close()


sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  
server_address = ('localhost', 20001)
#Enviando mensagem ao servidor

message = input("Envie alguma coisa para visualizar a hora")
sock.sendto(message.encode(),server_address)
print ("Enviando %s porta %s" % server_address)
recepcao = threading.Thread(target=receber_mensagens,args=(sock,))
recepcao.start()
recepcao.join()
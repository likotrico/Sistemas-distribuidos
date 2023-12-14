import socket
import threading
from datetime import datetime

def protocolo(data,address):
    data_e_hora_atuais = datetime.now()
    hora = data_e_hora_atuais.strftime('%H:%M:%S')
    sock.sendto(hora.encode(), address)
   

sock = socket.socket(socket.AF_INET,  socket.SOCK_DGRAM)
    
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server_address = ('localhost', 20001)
print ("Iniciando servidor na porta %s %s" % server_address)
#Reservando porta
sock.bind(server_address)
#Iniciando protocolo

while True:
    data, address = sock.recvfrom(1)
    conexao = threading.Thread(target=protocolo,args=(data,address,))
    conexao.start()

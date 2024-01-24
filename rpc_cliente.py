#Importar biblioteca
import xmlrpc.client
import socket
#Definir servidor
s = xmlrpc.client.ServerProxy('http://10.0.84.198:21212')

#Chamar funções disponíveis no servidor
#print(s.add(2,3))  # Returns 5
s.armazenar(socket.gethostname())
s.armazenar("Mensagem 2")
s.armazenar("Mensagem 3")
print(s.getMensagens())
print(s.getServerIp())
print(s.getDataTime())

# Print list of available methods
print(s.system.listMethods())
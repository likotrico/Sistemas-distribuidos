from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler
import socket
import datetime

# Registrar caminho para o servidor
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

# Create server
with SimpleXMLRPCServer(('10.0.84.198', 21212),requestHandler=RequestHandler) as server:
    server.register_introspection_functions()

    #Definição de funções
    
    mensagens = []
    
    def armazenar(mensagem):
        mensagens.append(mensagem)
        return (True)
    
    def getMensagens():
        return(mensagens)
    
    def getServerIp():
        return (socket.gethostbyname(socket.gethostname()))
    
    def getDataTime():
        date = datetime.datetime.now()
        date_string = date.strftime("%A %d %B %y %I:%M")
        return date_string
    
    #Registrar funções
    server.register_function(armazenar, 'armazenar')
    server.register_function(getMensagens, 'getMensagens')
    server.register_function(getServerIp, 'getServerIp')
    server.register_function(getDataTime, 'getDataTime')

    # Iniciar servidor
    server.serve_forever()
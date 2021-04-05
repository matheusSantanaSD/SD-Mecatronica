import socket

class Servidor:

    _flag= False
    mensagem = 'msg'

    def __init__(self, porta, file):
        self._hostServer = '127.0.0.10'
        print('IP: ',self._hostServer)
        self._port = int(porta)         
        self._tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)#criando socket do tipo tcp
        self._address = (self._hostServer, self._port)#passando o ip e a porta
        self._tcp.bind(self._address)#passnando para a conceçao tcp o indereço
        self._tcp.listen(999999)# quantas conecçoes podem ser feitas nesse servidor no aso 1
        self._nameFile = file #nome arquivo a ser enviado
    
    
    def readFile(self):#lendo o arquivo
        try:
            self._fileOpen = open(self._nameFile, "rb")#abre o arquivo
            self._envio = self._fileOpen.read()#le o arquivo
        except IOError as e:
            print ('ERROR: ARQUIVO NAO ENCONTRADO')
        finally:
            self._fileOpen.close()#fecha o fluxo de arquivo
        
    def sendFile(self, contador):#envio servidor
        self.mensagem = 'cliente {} peguei'.format(contador)
        print ('Esperando cliente...')
        self._connection, self._client = self._tcp.accept()
        self._flag = True
        print ('Cliente {} conectado'.format(self._client[0]))      
        self._connection.sendall(self._envio)#envia variavel envio
        #self._tcp.close()
        self._connection.close()

    
class Cliente:
    def __init__(self, IP , porta , file ):
        self._hostServer = IP
        self._port = int(porta)            # mudar como parametro
        self._tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)#criando socket do tipo tcp
        self._address = (self._hostServer, self._port)#passando o ip e a porta
        print ('Conectando...')
        self._tcp.connect(self._address)
        self._nameFile = file #mudar como parametro
    
    def closeConnection(self):
        self._tcp.close()
    
    def receiveFile(self):#baixar cliente
        with open(self._nameFile,'wb') as wf:
            print ('Baixando...')
            while True:
                self._recebido = self._tcp.recv(4096)
                if not self._recebido: break
                wf.write(self._recebido)
            print ('Concluido!')

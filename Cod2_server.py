#!/usr/bin/python3
from Cod2 import Servidor
import sys
import concurrent.futures


porta = sys.argv[1]
arquivo = sys.argv[2]

Server = Servidor(porta,arquivo)
Server.readFile()
i = 1
while True:
    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(Server.sendFile, '{}'.format(i))
    while not Server._flag:
        pass
    print(Server.mensagem)
    i = i+1
    Server._flag = False 
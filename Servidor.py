#Codigo servidor

import socket
from datetime import datetime
import os
import platform

host="localhost"
port=8080
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((host, port))

server.listen(1)
print("Ora puess")

active, addr = server.accept()

while True:
    recibido = active.recv(1024)
    
    if recibido.decode(encoding="ascii", errors="ignore") == "adios":
        enviar= "Bye"
        active.send(enviar.encode(encoding="ascii", errors="ignore"))
        break
    #PALABRA DATE
    if recibido.decode(encoding="ascii", errors="ignore") == "date":
        enviar= str(datetime.now())
        print(datetime.now())
        active.send(enviar.encode(encoding="ascii", errors="ignore"))
        break
    #PALABRA OS
    if recibido.decode(encoding="ascii", errors="ignore") == "os":
        enviar= str(platform.system() + " " + platform.release() + ", " + platform.processor())
        print(platform.system(), platform.release())
        active.send(enviar.encode(encoding="ascii", errors="ignore"))
        break
    #PALABRA ls
    if recibido.decode(encoding="ascii", errors="ignore") == "ls":
        enviar= str(os.listdir())
        print(os.listdir())
        active.send(enviar.encode(encoding="ascii", errors="ignore"))
        break

    print("Cliente: ", recibido.decode(encoding="ascii", errors="ignore"))

    enviar= input("Servidor: ")
    active.send(enviar.encode(encoding="ascii", errors="ignore"))

active.close()
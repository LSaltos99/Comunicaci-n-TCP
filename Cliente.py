import socket

host = "localhost"
port = 8080

socket1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket1.connect((host,port))

print ("Inicializando el cliente...")

while True:

    enviar = input("Cliente: ")

    socket1.send(enviar.encode(encoding="ascii", errors="ignore"))

    recibido = socket1.recv(1024)

    if recibido.decode(encoding="ascii", errors="ignore") == "Bye":
        print ("Cierro conexión")
        break
    
    print("Servidor: ", recibido.decode(encoding="ascii", errors="ignore"))


socket1.close()
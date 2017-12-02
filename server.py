import os
import socket

HOST = os.environ.get("HOST", "localhost")
PORT = int(os.environ.get("PORT", "8080"))

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# setsockopt
server_socket.bind((HOST, PORT))
server_socket.listen(1)
print("Listening connections on {0}:{1}".format(HOST, PORT))

while True:
    client_socket, client_address = server_socket.accept()
    print("Got connection: {0}".format(client_address))

    request = client_socket.recv(1024)
    print(request)

    client_socket.sendall(b"""HTTP/1.1 200 OK
    
    <h1><a href=\"http://dimini.tk\">Dimini Inc</a></h1>""")

    client_socket.close()

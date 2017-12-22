import os
import socket

HOST = os.environ.get("HOST", "localhost")
PORT = int(os.environ.get("PORT", "8080"))

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# setsockopt
server_socket.bind((HOST, PORT))
server_socket.listen(2)
print("Listening connections on {0}:{1}".format(HOST, PORT))

while True:
    client_socket, client_address = server_socket.accept()
    print("Got connection: {0}".format(client_address))

    request = client_socket.recv(1024)
    print(request.decode("UTF-8"))

    client_socket.sendall(request)

    client_socket.close()
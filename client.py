import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_socket.connect(("localhost",8080))

client_socket.sendall(b"GET / HTTP/1.1\n")

response=client_socket.recv(1024)

print(response)
client_socket.close()
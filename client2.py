import socket



while True:
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    inputtext=input("")
    client_socket.connect(("localhost", 8080))
    client_socket.sendall(bytes(inputtext, encoding='utf-8'))

    response=client_socket.recv(1024)

    print(response.decode("UTF-8"))
    client_socket.close()
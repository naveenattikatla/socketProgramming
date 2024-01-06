import socket

client_socket = socket.socket()

# 1. connect to server socket
client_socket.connect(("localhost" , 8083))


client_socket.sendall(b'hello from client')

mess =  client_socket.recv(2048)
print(mess)


client_socket.close()
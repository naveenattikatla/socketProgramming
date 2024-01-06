import socket

client2_socket =socket.socket()

client2_socket.connect(("localhost" ,  8080))

client2_socket.sendall(b'data from client2 socket')

mess   =  client2_socket.recv(2048)

print(mess)

client2_socket.close()
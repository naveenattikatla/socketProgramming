# socket programming is a process of enabling two process to communictae with each other..
# socket is compremised of three things protocal , ip address and port number

import socket
import threading


def connect_a_client(conn , addr) : 
    mess  = conn.recv(2048)
    conn.sendall(b"message received from server")
    print(mess)
    conn.close()

PORT = 8080
HOST  = "localhost"

#  1. create server object

server_socket = socket.socket()

# 2 . bind with  port 

server_socket.bind((HOST,  PORT))

# 3 . listen  for server socket port 

server_socket.listen()


# accepting for new connections 
while True : 
    conn ,  addr =  server_socket.accept()
    t = threading.Thread(target  = connect_a_client , args = (conn ,  addr))
    t.start()

server_socket.close()





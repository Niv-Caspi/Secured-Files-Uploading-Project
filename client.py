import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("127.0.0.1", 8080))


while True:
    message = input("----> ")
    sock.send(message.encode())

    if message == "open":
        received_message = sock.recv(1024)
        print("Server: {}".format(received_message.decode()))
        message = input("----> ")
        sock.send(message.encode())
        received_message = sock.recv(1024)
        print("Server: {}".format(received_message.decode()))

    if message == "upload":
        received_message = sock.recv(1024)
        print("Server: {}".format(received_message.decode()))
        message = input("----> ")
        sock.send(message.encode())
        received_message = sock.recv(1024)
        print("Server: {}".format(received_message.decode()))

    if message == "download":
        received_message = sock.recv(1024)
        print("Server: {}".format(received_message.decode()))
        message = input("----> ")
        sock.send(message.encode())
        received_message = sock.recv(1024)
        print("Server: {}".format(received_message.decode()))
        message = input("----> ")
        sock.send(message.encode())
        received_message = sock.recv(1024)
        print("Server: {}".format(received_message.decode()))

    
    if message == "bye":
        break

sock.close()
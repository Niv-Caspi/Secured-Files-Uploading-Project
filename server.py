import socket
import shutil
import os

DIRECTORY = "C:\\Users\\Niv\\Programmers Club Work\\Secured Files Uploading Project\\files\\"

def open_file(file_name):
    file_path = DIRECTORY + file_name
    try:
        f = open(file_path)
    except FileNotFoundError:
        message = "This file does not exist in our system."
        connection.send(message.encode())
        return message
    else:
        message = "This file exists in our system.\n\nContent of " + file_name + ":\n\n" + str(f.read() + "\n")
        connection.send(message.encode())
        return message

def upload_file(file_path):
    shutil.move(file_path, DIRECTORY)
    message = "The file was uploaded succesfully."
    connection.send(message.encode())
    return message
    
def download_file(file_name, location_path):
    file_location = DIRECTORY + file_name 
    final_location = location_path + '\\' + file_name 
    shutil.move(file_location, final_location)
    
    message = "The file was downloaded succesfully."
    connection.send(message.encode())
    return message


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip = "127.0.0.1"
port = 8080
sock.bind((ip, port))

sock.listen(1)
print()
print("Server is listening...")
connection, adress = sock.accept()
print("Connection Established: " + str(adress))
print()

while True:
    received_message = connection.recv(1024)
    print("Client: {}".format(received_message.decode()))

    if received_message.decode() == "open":
        message = "What is the file name?"
        connection.send(message.encode())
        print("Server: {}".format(message))

        # Waiting for a file name.
        received_message = connection.recv(1024)
        print("Client: {}".format(received_message.decode()))

        # opening the file.
        print("Server: {}".format(open_file(received_message.decode())))

    if received_message.decode() == "upload":
        message = "What is the file path?"
        connection.send(message.encode())
        print("Server: {}".format(message))

        # Waiting for a file path.
        received_message = connection.recv(1024)
        print("Client: {}".format(received_message.decode()))

        # uploading the file.
        print("Server: {}".format(upload_file(received_message.decode())))

    if received_message.decode() == "download":
        message = "Which file would you like to download?\n" +  str(os.listdir(r"C:\Users\Niv\Programmers Club Work\Secured Files Uploading Project\Files"))
        connection.send(message.encode())
        print("Server: {}".format(message))

        # Waiting for a file name.
        received_message1 = connection.recv(1024)
        print("Client: {}".format(received_message1.decode()))

        # asking for location path
        message = "Where shall the downloaded file be located?"
        connection.send(message.encode())
        print("Server: {}".format(message))

        # Waiting for a location path.
        received_message = connection.recv(1024)
        print("Client: {}".format(received_message.decode()))

        # downloading the file.
        print("Server: {}".format(download_file(received_message1.decode(), received_message.decode())))

    if received_message.decode() == "bye":
        print()
        break

connection.close()

sock.close()



"""how to send message from server:
if received_message.decode() == "open":
        message = "What is the file name?"
        connection.send(message.encode())
        print("Server: {}".format(message))
"""
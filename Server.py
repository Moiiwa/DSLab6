import socket as socket_lib
import os

socket = socket_lib.socket(socket_lib.AF_INET, socket_lib.SOCK_STREAM)
socket.setsockopt(socket_lib.SOL_SOCKET, socket_lib.SO_REUSEADDR, 1)
socket.bind(("localhost",8096))
socket.listen(10)

class Server():

    def accept_connections(self):
        while(True):
            connection, address = socket.accept()
            data = connection.recv(1024)
            filename = str(data, encoding='utf-8')
            name, extension = filename.split('.')
            copy_name = None
            if filename in os.listdir():
                copy_number = 1
                copy_name = f"{name}_copy{copy_number}.{extension}"
                while copy_name in os.listdir():
                    copy_number += 1
                    copy_name = f"{name}_copy{copy_number}.{extension}"
            if copy_name != None:
                filename = copy_name
            data = connection.recv(1024)
            file = open(filename, 'wb')
            while (data):
                file.write(data)
                data = connection.recv(1024)
            file.close()
            connection.close()
server = Server()
server.accept_connections()
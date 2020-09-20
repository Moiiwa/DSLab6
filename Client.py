import sys
import socket
import time

class Client:

    socket = None

    def send_file(self, file):
        self.socket.send(bytes(filename, encoding='utf-8'))
        time.sleep(1)
        size_of_file = file.__sizeof__()
        bytes_sent = 0
        self.print_progress_bar(0, size_of_file)
        while(bytes_sent<=size_of_file):
            self.socket.send(file.read(1024))
            bytes_sent += 1024
            if bytes_sent < size_of_file:
                self.print_progress_bar(bytes_sent, size_of_file)
            else:
                print("File is Sent")

    def __init__(self, socket):
        self.socket = socket
        socket.bind(("localhost",8095))
        socket.connect((host, int(port)))

    def print_progress_bar(self, ready, all):
        percentage = ready * 100 / all
        ready = int((ready * 100 / all) // 10)
        print(f"Ready: {percentage} percent")
        progress = " "
        for i in range (ready):
            progress += "I"
        for i in range (10-ready):
            progress += " "
        progress += "|"
        print(progress)

    def close_socket(self):
        self.socket.close()


arguments = sys.argv

if len(sys.argv)!=4:
    raise Exception('Wrong number of args')

filename = arguments.__getitem__(1)
host = arguments.__getitem__(2)
port = arguments.__getitem__(3)

print(filename)
print(host)
print(port)

socket = socket.socket()
client = Client(socket)
file = open(filename, "rb")
print(file.__sizeof__())
client.send_file(file=file)
client.close_socket()
socket.close()

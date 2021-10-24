# imports
import socket
import sys

# Sample values for ip, port, and buffer
serverIP = '127.0.0.1'
serverPort = 8080
buffer = 1024

# Main client function, for connecting to established server and printing received data.
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as socketInput:
    print('Waiting...')
    socketInput.connect((serverIP, serverPort))
    print('Connected to a server')

    # Receives and prints data from server input
    def recv():
        while True:
            data = socketInput.recv(1024).decode('UTF-8')
            if not data:
                sys.exit(0)
            print(data)

    # Repeatedly runs the receive function
    while True:
        recv()

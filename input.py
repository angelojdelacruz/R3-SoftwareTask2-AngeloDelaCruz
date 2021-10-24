# Imports
from pynput.keyboard import Key
from pynput import keyboard
import socket
import threading

# Initialized variables
data = ""
speed = 0
m1 = ''
m2 = ''
m3 = ''
m4 = ''


# Main function for detecting which key is being pressed down (One at a time)
def multiKey(key):
    global m1, m2, m3, m4, data, speed
    # Direction keys, determines which motors move in what way, uses arrow keys
    if key == Key.up:
        m1 = 'f'
        m2 = 'f'
        m3 = 'f'
        m4 = 'f'
        print('Moving forward')
    elif key == Key.down:
        m1 = 'r'
        m2 = 'r'
        m3 = 'r'
        m4 = 'r'
        print('Moving backwards')
    if key == Key.right:
        m1 = 'f'
        m2 = 'f'
        m3 = 'r'
        m4 = 'r'
        print('Turning right')
    elif key == Key.left:
        m1 = 'r'
        m2 = 'r'
        m3 = 'f'
        m4 = 'f'
        print('Turning left')
    # Speed setting keys, uses f1 to f6
    if key == Key.f1:
        speed = 0
        print(f'Speed set to {speed}')
    if key == Key.f2:
        speed = 51
        print(f'Speed set to {speed}')
    if key == Key.f3:
        speed = 102
        print(f'Speed set to {speed}')
    if key == Key.f4:
        speed = 153
        print(f'Speed set to {speed}')
    if key == Key.f5:
        speed = 204
        print(f'Speed set to {speed}')
    if key == Key.f6:
        speed = 255
        print(f'Speed set to {speed}')
    # Sets data as a combination of each motor and the speed setting
    data = f'[{m1}{speed}][{m2}{speed}][{m3}{speed}][{m4}{speed}]'


# Used to display how the rover has stopped, in what the previous directional input was
def on_release(key):
    global data
    data = f'[{m1}0][{m2}0][{m3}0][{m4}0]'
    print('Stopped moving')


# Sends data over to client server
def listenerFunk():
    global data
    while True:
        if data:
            connect.send(data.encode('UTF-8'))
            data = None


# Sample values for ip, port, and buffer
serverIP = '127.0.0.1'
serverPort = 8080
buffer = 1024

# Main server function, binding, listening, connecting, etc.
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as socketInput:
    socketInput.bind((serverIP, serverPort))
    socketInput.listen()
    print(f'Listening...')
    connect, address = socketInput.accept()
    with connect:
        print('Connection from', address)
        with keyboard.Listener(on_press=multiKey, on_release=on_release) as listener:
            # runs listenerFunk alongside everything else
            threading.Thread(target=listenerFunk).start()
            listener.join()

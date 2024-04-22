import socket
import threading

HOST = '127.0.0.1'
PORT = 5555

def receive_messages(client):
    while True:
        try:
            data = client.recv(1024).decode()
            print(data)
        except:
            break

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

receive_thread = threading.Thread(target=receive_messages, args=(client,))
receive_thread.start()

while True:
    message = input()
    client.sendall(message.encode())

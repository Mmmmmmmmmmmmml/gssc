import socket
import threading

HOST = '127.0.0.1'
PORT = 5555

clients = []
messages = []

def handle_client(client_socket, address):
    global clients
    try:
        while True:
            data = client_socket.recv(1024).decode()
            if not data:
                break

            messages.append(data)
            for client in clients:
                client.sendall(data.encode())
    except:
        pass

    client_socket.close()
    clients.remove(client_socket)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(5)

print(f'Server is running on {HOST}:{PORT}')

while True:
    client_socket, address = server.accept()
    clients.append(client_socket)
    print(f'Connection from {address}')

    # Start a new thread to handle the client communication
    client_thread = threading.Thread(target=handle_client, args=(client_socket, address))
    client_thread.start()

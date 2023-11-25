import socket
import threading

def handle_client(client_socket, client_address):
    print(f"Accepted connection from {client_address}")

    while True:
        try:
            message = client_socket.recv(1024)
            if not message:
                break
            print(f"Received message from {client_address}: {message.decode('utf-8')}")
            broadcast(message, client_socket)
        except OSError:
            break

    print(f"Connection from {client_address} closed.")
    client_sockets.remove(client_socket)
    client_socket.close()


def broadcast(message, sender_socket):
    for client_socket in client_sockets:
        if client_socket != sender_socket:
            try:
                client_socket.send(message)
            except socket.error:
                client_sockets.remove(client_socket)

# Server configuration
HOST = '192.168.100.57'
PORT = 39277

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(5)

print(f"Server listening on {HOST}:{PORT}")

# List to store connected clients
client_sockets = []

# Accept and handle incoming connections
while True:
    client_socket, client_address = server_socket.accept()
    client_sockets.append(client_socket)

    # Start a new thread to handle the client
    client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
    client_thread.start()

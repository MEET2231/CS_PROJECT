import socket
import threading

# Server configuration
HOST = ''  # Listen on all available network interfaces
PORT = 55555

# List to hold client connections and usernames
clients = {}

# Function to broadcast messages to all clients
def broadcast(message, sender_username):
    for username, client in clients.items():
        if username != sender_username:
            client.send(f"{sender_username}: {message}".encode('utf-8'))

# Function to handle each client's connection
def handle_client(client, username):
    while True:
        try:
            # Receive message from client
            message = client.recv(1024).decode('utf-8')
            broadcast(message, username)
        except:
            # If an error occurs or client disconnects, remove the client
            del clients[username]
            client.close()
            break

# Function to start the server
def start_server():
    # Create a socket object
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Bind the server to the specified address and port
    server.bind((HOST, PORT))
    # Listen for incoming connections
    server.listen()

    print(f"Server is listening on {HOST}:{PORT}")

    while True:
        # Accept a new connection
        client, address = server.accept()
        print(f"New connection from {address}")
        
        # Prompt the client for a username
        client.send("Enter your username: ".encode('utf-8'))
        username = client.recv(1024).decode('utf-8')
        
        # Add the new client to the list
        clients[username] = client
        
        # Create a new thread to handle the client's connection
        thread = threading.Thread(target=handle_client, args=(client, username))
        thread.start()

# Start the server
start_server()

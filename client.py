import socket
import threading

# Server configuration
HOST = '192.168.8.73'  # Replace with the server's intranet IP address
PORT = 55555

# Function to handle receiving messages from the server
def receive_messages(client_socket):
    while True:
        try:
            # Receive message from server
            message = client_socket.recv(1024).decode('utf-8')
            print(message)
        except:
            # If an error occurs, close the connection
            client_socket.close()
            break

# Function to start the client
def start_client():
    # Create a socket object
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Connect to the server
    client_socket.connect((HOST, PORT))

    # Receive username prompt from server
    print(client_socket.recv(1024).decode('utf-8'))
    # Prompt user to enter a username
    username = input("Enter your username: ")
    # Send the username to the server
    client_socket.send(username.encode('utf-8'))

    # Start a thread to receive messages from the server
    receive_thread = threading.Thread(target=receive_messages, args=(client_socket,))
    receive_thread.start()

    while True:
        # Send messages to the server
        message = input()
        client_socket.send(message.encode('utf-8'))

# Start the client
start_client()

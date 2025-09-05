import socket
import threading
import time
import psutil
from datetime import datetime

# Server configuration
HOST = '127.0.0.1'
PORT = 12345

# Lists to manage clients and their nicknames
clients = []
nicknames = []

# Function to broadcast messages to all clients
def broadcast(message, sender_socket=None):
    start_time = time.time()
    for client in clients:
        if client != sender_socket:
            try:
                client.send(message.encode('utf-8'))
            except:
                if client in clients:
                    index = clients.index(client)
                    nickname = nicknames.pop(index)
                    clients.remove(client)
                    broadcast(f"{nickname} has left the chat.")
    print(f"Broadcast Execution Time: {time.time() - start_time:.4f} seconds")

# Function to handle private messaging for multiple recipients
def send_private_message(sender_socket, recipient_nicknames, message):
    start_time = time.time()
    sender_nickname = nicknames[clients.index(sender_socket)]
    failed_recipients = []

    for recipient_nickname in recipient_nicknames:
        recipient_nickname = recipient_nickname.strip()  # Remove extra spaces
        if recipient_nickname in nicknames:
            recipient_index = nicknames.index(recipient_nickname)
recipient_socket = clients[recipient_index]
            private_message = f"Private message from {sender_nickname}: {message}"
            recipient_socket.send(private_message.encode('utf-8'))
        else:
            failed_recipients.append(recipient_nickname)

    if failed_recipients:
        failed_message = f"Failed to deliver message to: {', '.join(failed_recipients)}"
        sender_socket.send(failed_message.encode('utf-8'))

    print(f"Private Message Execution Time: {time.time() - start_time:.4f} seconds")

# Function to handle a client
def handle_client(client_socket):
    try:
        while True:
            client_socket.send("Enter your nickname:".encode('utf-8'))
            nickname = client_socket.recv(1024).decode('utf-8').strip()
            if nickname not in nicknames and nickname.lower() != "you":
                nicknames.append(nickname)
                clients.append(client_socket)
                client_socket.send("You have joined the chat!".encode('utf-8'))
                client_socket.send(
                    "To send a private message, type `/msg <nickname1,nickname2> <message>`.".encode('utf-8')
                )
                broadcast(f"{nickname} has joined the chat!", sender_socket=client_socket)
                print(f"{nickname} joined the chat.")
                break
            else:
                client_socket.send("ERROR: Nickname already taken or invalid. Please try again.".encode('utf-8'))

        while True:
            message = client_socket.recv(1024).decode('utf-8')
            if message.startswith('/msg'):
                try:
                    _, recipient_part, *private_message = message.split(' ')
                    recipient_nicknames = recipient_part.split(',')
                    private_message = ' '.join(private_message)
                    send_private_message(client_socket, recipient_nicknames, private_message)
                except ValueError:
                    client_socket.send("ERROR: Invalid /msg format. Use `/msg <nickname1,nickname2> <message>`.".encode('utf-8'))
            else:
                sender_nickname = nicknames[clients.index(client_socket)]
                broadcast(f"{sender_nickname}: {message}", sender_socket=client_socket)

    except Exception as e:
        if client_socket in clients:
            index = clients.index(client_socket)
            nickname = nicknames.pop(index)
            clients.remove(client_socket)
            broadcast(f"{nickname} has left the chat.")
            print(f"{nickname} disconnected.")
            client_socket.close()

# Function to monitor server performance
def monitor_performance():
    while True:
        print(f"Memory Usage: {psutil.Process().memory_info().rss / 1024 ** 2:.2f} MB")
        time.sleep(5)

# Start the server
def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen()
    print(f"Server running on {HOST}:{PORT}")

    # Start the performance monitoring thread
    threading.Thread(target=monitor_performance, daemon=True).start()

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"New connection from {client_address}")
        thread = threading.Thread(target=handle_client, args=(client_socket,))
        thread.start()

if __name__ == "__main__":
    start_server()
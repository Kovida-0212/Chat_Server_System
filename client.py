import socket
import threading
from datetime import datetime

# Client configuration
HOST = '127.0.0.1'
PORT = 12345

# Function to handle receiving messages
def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            print(f"[{datetime.now().strftime('%H:%M:%S')}] {message}")
        except:
            print("Disconnected from the server.")
            client_socket.close()
            break

# Function to handle sending messages
def send_messages(client_socket):
    while True:
        message = input()
        timestamp = datetime.now()
        client_socket.send(message.encode('utf-8'))
        print(f"Message sent at {timestamp.strftime('%H:%M:%S')}")

# Start the client
def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((HOST, PORT))

    # Start threads for sending and receiving messages
    receive_thread = threading.Thread(target=receive_messages, args=(client_socket,))
    receive_thread.start()

    send_thread = threading.Thread(target=send_messages, args=(client_socket,))
    send_thread.start()

if __name__ == "__main__":
    start_client()


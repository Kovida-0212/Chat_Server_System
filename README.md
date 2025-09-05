# Chat_Server_System
A real-time multi-client chat application implemented in Python using socket programming and multithreading. This project demonstrates core concepts of networking, inter-process communication (IPC), and concurrency while providing features like message broadcasting and private messaging.
## Features
- Multi-Client Support: Handles multiple simultaneous client connections effectively.
- Message Broadcasting: Sends messages from one client to all other connected clients.
- Private Messaging: Enables sending private messages to one or more specific clients using /msg command.
- Robust Error Handling: Handles invalid inputs, duplicate nicknames, and client disconnections gracefully.
- Performance Monitoring: Server tracks memory usage dynamically using psutil to ensure efficient resource management.
- User-Friendly Interface: Simple command-line interface for easy client interaction and message commands.
- Multi-threaded: Utilizes threads on both server and client sides for concurrent handling of connections and messaging.
## Technologies Used
- Python 3
- Socket programming (TCP/IP)
- Multithreading
- psutil library for system performance monitoring
## Getting Started
### Prerequisites
- Python 3.x installed
- psutil library (install via pip install psutil)
### Running the Server
1. Save the server code into a file named server.py.
2. Run the server in your terminal or command prompt:
   ```
   python3 server.py
   ```
3. The server starts listening on localhost (127.0.0.1) and port 12345.
### Running the Client
1. Save the client code into a file named chat_client.py.
2. Run the client in a separate terminal:
   ```
   python3 client.py
   ```
3. Enter a unique nickname when prompted.
4. Start chatting! Use /msg <nickname1,nickname2> <message> to send private messages or simply type messages to broadcast.
## How It Works
- The server manages connected clients and their nicknames.
- It broadcasts messages from clients to others or sends private messages based on commands.
- Each client runs two threads: one for receiving messages and one for sending.
- The server monitors memory usage every 5 seconds and prints stats for performance awareness.
## Future Enhancements
- Authentication: Add login with username and password.
- IP Blocking: Restrict unauthorized or malicious access.
- Multi-Server Architecture: Support load balancing over multiple servers.
- Database Integration: Store user data and chat logs persistently.
- Group Chats: Enable chatting in groups or channels.
- Chat History: Allow saving and retrieving past messages.
- Moderation Commands: Support /ban, /mute, and more.
- Bot Integration: Add automated chat bots for moderation or entertainment.

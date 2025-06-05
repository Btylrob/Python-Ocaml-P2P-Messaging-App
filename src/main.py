import socket
import threading

HOST = '0.0.0.0'
PORT = 5000

class ChatApp:
    def __init__(self):
        self.conn = None
        self.active = False
        self.username = ''
        self.peer_username = ''
        self.status = None
        
    def start_server(self):
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server.bind((HOST, PORT))
        server.listen(1)
        print(f"Listening on port {PORT}")
        conn, addr = server.accept()
        print(f"Connected to {addr[0]}")
        self.status = active
        print(self.status)
        self.conn = conn
        self.active = True
        
        # Send and receive usernames
        self.conn.send(self.username.encode())
        self.peer_username = self.conn.recv(1024).decode()
        print(f"{self.peer_username} has joined the chat.")
        
    def connect_to_peer(self, ip):
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((ip, PORT))
        print(f"Connected to {ip}")
        self.conn = client
        self.active = True
        
        # Send and receive usernames
        self.peer_username = self.conn.recv(1024).decode()
        self.conn.send(self.username.encode())
        print(f"{self.peer_username} has joined the chat.")
    
    def receive_messages(self):
        while self.active:
            try:
                msg = self.conn.recv(1024).decode()
                if msg:
                    print(f"{self.peer_username}: {msg}")
                else:
                    break
            except:
                break
        self.active = False
    
    def send_message(self, msg):
        if self.conn and msg:
            self.conn.send(msg.encode())
    
    def run(self):
        self.username = input("Enter your username: ").strip()
        mode = input("Host (h) or Connect (c): ").strip().lower()
        
        if mode == 'h':
            self.start_server()
        else:
            ip = input("ip: ").strip()
            self.connect_to_peer(ip)
        
        threading.Thread(target=self.receive_messages, daemon=True).start()
        
        while self.active:
            msg = input()
            if msg:
                self.send_message(msg)
                print(f"You ({self.username}): {msg}")

if __name__ == "__main__":
    app = ChatApp()
    app.run()

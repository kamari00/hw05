import socket

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 12345))
    server_socket.listen(5)

    print("Server listening on port 12345...")

    client_socket, addr = server_socket.accept()
    print("Connection from", addr)

    for _ in range(100):
        data = client_socket.recv(1024)  # отримати дані розміром 1024 байти
        print("Received:", data.decode())

    client_socket.close()

if __name__ == "__main__":
    start_server()

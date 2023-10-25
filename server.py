import socket

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 12345))
    server_socket.listen(5)

    print("Server listening on port 12345...")

    client_socket, addr = server_socket.accept()
    print("Connection from", addr)

    messages_received = 0

    while messages_received < 100:
        data = client_socket.recv(1024).decode()  # отримати дані та перетворити їх у рядок
        if "###END###" in data:
            messages_received += 1
            message = data.replace("###END###", "")
            print("Received:", message)
        else:
            print("Received incomplete message:", data)

    client_socket.close()

if __name__ == "__main__":
    start_server()

import socket

def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 12345))

    for i in range(100):
        message = f"Message {i}###END###"  # додавання маркера до кінця повідомлення
        client_socket.send(message.encode())  # надсилання повідомлення на сервер
        print("Sent:", message)

    client_socket.close()

if __name__ == "__main__":
    start_client()

import socket

class SocketClient:
    def __init__(self, host: str='localhost', port: int=5000) -> None:
        self.host = host
        self.port = port
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self) -> None:
        self.client_socket.connect((self.host, self.port))

    def send_data(self, data: str) -> str:
        self.client_socket.sendall(data.encode('utf-8'))
        response = self.client_socket.recv(1024).decode('utf-8')
        return response

    def close(self) -> None:
        self.client_socket.close()
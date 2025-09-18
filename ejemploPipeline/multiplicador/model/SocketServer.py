import socket

class SocketServer:
    def __init__(self, port) -> None:
        self.host=socket.gethostname()
        self.port=port
        self.server_socket = socket.socket()
        self.server_socket.bind((self.host, self.port))
        self.datasRecived=""
        self.conn=None
        self.address=None

    def socketRecive(self)->str:
        self.server_socket.listen()
        self.conn, self.address = self.server_socket.accept()
        self.dataRecived=self.conn.recv(1024).decode('utf-8')
        return self.dataRecived,self.address
    
    def sendResponseData(self,data:str)->None:
        if self.conn:
            self.conn.send(data.encode('utf-8'))

    def closeSocket(self)->None:
        if self.conn:
            self.conn.close()
        self.server_socket.close()
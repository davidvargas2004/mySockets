import socket
from view.Terminal import Terminal
from model.SocketClient import SocketClient
from model.SocketServer import SocketServer
from model.Calculator import Calculator
from model.FileManager import FileManager

class Controller:
    def __init__(self) -> None:
        self.terminal=Terminal()
        self.casio=Calculator()
        self.socket_clientToMultiplicador=SocketClient(socket.gethostname(),5001)
        self.socket_server=SocketServer(5000)
        self.file_manager=FileManager("../docs/help.json") 
       
    def run(self) -> None:
        self.terminal.showMessage("Welcome to the Sumador Server")
        self.terminal.showMessage("Type 'help' to see available commands")
        while True:
            self.terminal.captureCommand(input(self.terminal.symbolPrompt+" "))
            if self.terminal.command=="bye":
                break
            elif self.terminal.command=="sum":
                self.terminal.showMessage("Result: "+str(self.casio.sum(input("Enter first number: "),input("Enter second number: "))))
            elif self.terminal.command=="server mode":
                print("Entering server mode...")
                self.socket_server.socketRecive()
                #Process the data recived from the client
                #Expected format: "sum num1 num2 num3"
                op,a,b,c=self.socket_server.dataRecived.split(" ")
                self.terminal.showMessage("Data recived: "+self.socket_server.dataRecived)
                #Send to Multiplicador Server the data recived
                self.socket_clientToMultiplicador.connect()
                responseFromMultiplicador=self.socket_clientToMultiplicador.send_data(b+" "+c)
                responseTotal=str(self.casio.sum(a,responseFromMultiplicador))
                self.terminal.showMessage("Total Result: "+responseTotal)
                self.socket_clientToMultiplicador.close()
                #Send to the client the total result
                self.socket_server.sendResponseData(responseTotal)
                self.socket_server.closeSocket() 
            elif self.terminal.command=="help":
                self.file_manager.setPath("../docs/help.json")
                self.terminal.showMessage(self.file_manager.readFileStr())
            elif self.terminal.command=="about":
                self.file_manager.setPath("../docs/about.json")
                self.terminal.showMessage(self.file_manager.readFileStr())
            elif self.terminal.command=="clear":
                self.terminal.clear()
            else:
                self.terminal.showMessage("Unknown command: "+self.terminal.command)


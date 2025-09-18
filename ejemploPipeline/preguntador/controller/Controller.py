import socket
from view.Terminal import Terminal
from model.SocketClient import SocketClient
from model.FileManager import FileManager

class Controller:
    def __init__(self) -> None:
        self.terminal=Terminal()
        self.socket_client=SocketClient(socket.gethostname(),5000)
        self.file_manager=FileManager("../docs/help.json") 
       
    def run(self) -> None:
        self.terminal.showMessage("Welcome to the Preguntador Client")
        self.terminal.showMessage("Type 'help' to see available commands")
        while True:
            self.terminal.captureCommand(input(self.terminal.symbolPrompt+" "))
            if self.terminal.command=="bye":
                break
            elif self.terminal.command=="sum":
                a=input("Enter first number: ")
                b=input("Enter second number: ")
                c=input("Enter third number: ")    
                #Send data to the server and get the result
                self.socket_client.connect()
                result=self.socket_client.send_data(self.terminal.command+" "+a+" "+b+" "+c)
                self.terminal.showMessage("Result: "+str(result))
            elif self.terminal.command=="help":
                self.file_manager.setPath("../docs/help.json")
                self.terminal.showMessage(self.file_manager.readFile())
            elif self.terminal.command=="about":
                self.file_manager.setPath("../docs/about.json")
                self.terminal.showMessage(self.file_manager.readFile())
            elif self.terminal.command.startswith("clear"):
                self.terminal.clear()
            else:
                self.terminal.showMessage("Unknown command: "+self.terminal.command)

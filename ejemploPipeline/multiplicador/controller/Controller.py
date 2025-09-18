from view.Terminal import Terminal
from model.Calculator import Calculator
from model.SocketServer import SocketServer
from model.FileManager import FileManager

class Controller:
    def __init__(self) -> None:
        self.terminal=Terminal()
        self.casio=Calculator()
        self.socket_server=SocketServer(5001)
        self.file_manager=FileManager("../docs/help.json") 
       
    def run(self) -> None:
        self.terminal.showMessage("Welcome to the Multiplicador Server")
        self.terminal.showMessage("Type 'help' to see available commands")
        while True:
            self.terminal.captureCommand(input(self.terminal.symbolPrompt+" "))
            if self.terminal.command=="bye":
                break
            elif self.terminal.command=="mult":
                self.terminal.showMessage("Result: "+str(self.casio.mult(input("Enter first number: "),input("Enter second number: "))))
            elif self.terminal.command=="server mode":
                print("Entering server mode...")
                self.socket_server.socketRecive()
                self.terminal.showMessage("Data recived: "+self.socket_server.dataRecived)
                b,c=self.socket_server.dataRecived.split(" ")
                result=str(self.casio.mult(int(b),int(c)))
                self.terminal.showMessage("Result: "+result)
                self.socket_server.sendResponseData(result)
                self.socket_server.closeSocket()
            elif self.terminal.command=="help":
                self.file_manager.setPath("../docs/help.json")
                self.terminal.showMessage(self.file_manager.readFileStr())
            elif self.terminal.command=="about":
                self.file_manager.setPath("../docs/about.json")
                self.terminal.showMessage(self.file_manager.readFileStr())
            elif self.terminal.command.startswith("clear"):
                self.terminal.clear()
            else:
                self.terminal.showMessage("Unknown command: "+self.terminal.command)

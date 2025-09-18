import os
import platform

class Terminal:
    def __init__(self) -> None:
        self.message=None
        self.command=None
        self.fm=None
        self.symbolPrompt=".:>>"    

    def showPrompt(self) -> None:
        print (self.symbolPrompt)

    def clear(self) -> None:
        if platform.system()!="Windows":
            os.system("clear")
        else:
            os.system("cls")       

    def showMessage(self, message) -> None:
        self.message=message
        print (self.message)

    def captureCommand(self, command) -> None:
        self.command=command
        return self.command
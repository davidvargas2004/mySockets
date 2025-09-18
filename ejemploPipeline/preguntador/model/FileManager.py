import json

class FileManager:
   def __init__(self, path):
    self.path = path
    self.content=None

   def setPath(self, path):
     self.path=path
   
   def getPath(self)->str:
     return self.path

   def readFile(self):
    f = open(self.path, "r")
    self.content =json.load(f)
    return self.content

   def writeFile(self, name, ip):
     dat = {"name":name,"ip":ip}
     self.content.append(dat)

     with open(self.path, "w") as outfile:
        json_str = json.dumps(self.content,indent=2)
        outfile.write(json_str)
        outfile.write('\n')
  
   def writeNumber(self, number):
     dat={"number":number}
     json_str=json.dumps(dat)
     with open(self.path,"w") as outfile:
        outfile.write(json_str)
     
   def __str__(self) -> str:
     with open(self.path, "w") as outfile:
        json_str = json.dumps(self.content,indent=2)
     return self.path+"content:"+json_str

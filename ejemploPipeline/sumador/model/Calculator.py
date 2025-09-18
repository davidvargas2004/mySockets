
class Calculator:
    def __init__(self):
        self.a=0
        self.b=0
        self.c=0

    def sum(self, a, b)->str:
        self.a=int(a)
        self.b=int(b)
        self.c=self.a+self.b
        return str(self.c)
    
    def subs(self, a, b)->str:
        self.a=int(a)
        self.b=int(b)
        self.c=self.a-self.b
        return str(self.c)
    
    def mult(self, a, b)->str:
        self.a=int(a)
        self.b=int(b)
        self.c=self.a*self.b
        return str(self.c)
    
    def mult(self, a, b)->str:
        self.a=int(a)
        self.b=int(b)
        self.c=self.a/self.b
        return str(self.c)





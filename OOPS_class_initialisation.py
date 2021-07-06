class Friends:
    def __init__(self,name,bond_level,clas,institution):            # constructor
        self.name=name
        self.bond_level=bond_level                                  #self.attribute=value
        self.clas=clas
        self.institution=institution
    def display(self):                                              #method
        print(self.name,self.bond_level,self.clas,self.institution)

name=input()
bond_level=int(input())
clas=input()
institution=input()

suvarna=Friends(name,bond_level,clas,institution)                     #instanciating
suvarna.display()                                                   #calling the method

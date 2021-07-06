class Friends:                                                      #*******super class******
    def __init__(self,name,bond_level,clas,institution):
        self.name=name
        self.bond_level=bond_level
        self.clas=clas
        self.institution=institution
    def display(self):
        print(self.name,self.bond_level,self.clas,self.institution)

class Close_friend(Friends):                                        #******Sub class*********
    def __init__(self,ranking,name,bond_level,clas,institution):
        self.ranking=ranking
        super().__init__(name,bond_level,clas,institution)          #need to import from super class
    def display(self):
        super().display()                                           #imported the method in super class
        print(self.ranking)

name=input()
bond_level=int(input())
clas=input()
institution=input()
ranking=int(input())

friend1=Close_friend(ranking,name,bond_level,clas,institution)  
friend1.display()                                                   #here we are calling the method present in
                                                                    # both the classes so,the preference is sub
                                                                    # class.so,first give the values for sub class
    

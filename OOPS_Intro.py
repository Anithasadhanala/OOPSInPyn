class Family:
    me="Anitha"             #class variable 
    def __init__(self,father,mother,son):
        self.father=father
        self.mother=mother    #instance variable
        self.son=son
    def member(self):
        print(Family.me)      #accessing class variable
        print(self.father)    # accessing instance variable
        
    
main=Family("krishna murthy","rama devi","hari")   #obj of the class
print(main.father)
print(Family.me)
main.member()              #calling method

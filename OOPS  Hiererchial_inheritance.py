class Family:                                   #Parent class
    me="Anitha"            
    def __init__(self,father,mother,son):
        self.father=father
        self.mother=mother   
        self.son=son
    def member(self):
        print(Family.me)     
        print(self.father)    

        
class Superfamily(Family):                      # sub class of Family parent class                 
    
    def __init__(self,grand_father,grand_mother,father,mother,son):
        self.grand_father=grand_father
        self.grand_mother=grand_mother
        super().__init__(father,mother,son)


class Marvelfamily(Family):                     # sub class of family class

    def __init__(self,uncle,anty,father,mother,son):
        self.uncle=uncle
        self.anty=anty
        super().__init__(father,mother,son)

main=Marvelfamily("honey","Bunny","krishna murthy","Rama devi","hari")
main2=Superfamily("padma","satyanarayana","murthy","devi","hari")

print(main.father)
print(main2.father)



##### here we cant access superfamily var/methods in Marvelfamily class and wise versa ##############

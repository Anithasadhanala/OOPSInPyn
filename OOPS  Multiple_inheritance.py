class Family:                                   #Parent 1 class
    me="Anitha"            
    def __init__(self,father,mother,son):                           #     Family      Superfamily
        self.father=father                                          #         \         /
        self.mother=mother                                          #        Marvel class 
        self.son=son                                                                
    def member(self):
        print(Family.me)     
        print(self.father)

        
class Superfamily():                            # parent 2 class     
    
    def __init__(self,grand_father,grand_mother):
        self.grand_father=grand_father
        self.grand_mother=grand_mother

        

class Marvelfamily(Family,Superfamily):         # sub class for both the parents               

    def __init__(self,uncle,anty,father,mother,son,grand_father,grand_mother):
        self.uncle=uncle
        self.anty=anty                                                   #      In multiple inheritance
        Family.__init__(self,father,mother,son)                          #####  we use parent name and also add instance of the 
        Superfamily.__init__(self,grand_father,grand_mother)             #            class i.e "self"

main=Marvelfamily("honey","Bunny","krishna murthy","Rama devi","hari","padma","satyanarayana")


print(main.grand_father)




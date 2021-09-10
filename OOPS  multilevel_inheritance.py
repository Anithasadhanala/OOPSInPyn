class Family:                                   #Parent class
    me="Anitha"                                                                               #         Family
    def __init__(self,father,mother,son):                                                     #           |
        self.father=father                                                                    #     Superfamily
        self.mother=mother                                                                    #           |
        self.son=son                                                                          #     Marvelfamily
    def member(self):                                                                         #  
        print(Family.me)                                                                      #
        print(self.father)                                                                    

        
class Superfamily(Family):                      #subclass of Family class and parent to Marvelfamily subclass
    
    def __init__(self,grand_father,grand_mother,father,mother,son):
        self.grand_father=grand_father
        self.grand_mother=grand_mother
        super().__init__(father,mother,son)


class Marvelfamily(Superfamily):                 #sub class of Superfamily

    def __init__(self,uncle,anty,grand_father,grand_mother,father,mother,son):
        self.uncle=uncle
        self.anty=anty
        super().__init__(grand_father,grand_mother,father,mother,son)

main=Marvelfamily("honey","Bunny","padma","satyanarayana","krishna murthy","Rama devi","hari")


print(main.father)                              #can access var of Family , Superfamily , marvelfamily also




class Family:
    me="Anitha"
    greet="hello"
    def __init__(self,father,mother,son):  #instance method
        self.father=father
        self.mother=mother    
        self.son=son
          
    @classmethod                     #class method (cant access instance var)
    def nuclear(cls):
        print(Family.greet)
        
    @staticmethod                    #static method (cant access instance var)
    def member():
        print(Family.me) 
        
    
main=Family("krishna murthy","rama devi","hari")

main.nuclear()                #calling  class_method with class obj
Family.nuclear()              #calling class_method with class name
main.member()                 #calling  static_method with class obj
Family.member()               #calling static
_method with class name


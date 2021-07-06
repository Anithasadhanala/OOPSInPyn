class BinarySearch:
    def __init__(self,data,search,st,ed,mid):
        self.data=data
        self.search=search
        self.st=st
        self.ed=ed
        self.mid=mid
    def BinaryMethod(self):
        self.mid=((self.st+self.ed)//2)
        if(self.st<=self.ed):
            if(self.data[self.mid]==self.search):
                return (self.mid)+1
            elif(self.data[self.mid]>self.search):
                self.ed=self.mid
              
                return BinaryMethod(self)
        
            elif(self.data[self.mid]<self.search):
                self.st=self.mid+1
               
                return BinaryMethod(self)
       
        return False

n=int(input())
data=list(map(int,input().split()))
search=int(input())

st=0
ed=n
mid=((st+ed)//2)
data.sort()
print(data)
obj1=BinarySearch(data,search,st,ed,mid)
print(obj1.BinaryMethod())










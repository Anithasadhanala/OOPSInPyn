class Sorting:
    def __init__(self,n,data):
        self.n=n
        self.data=data
    def Insertion_sort(self):
        for i in range(1,self.n):
            j=i
            while(self.data[j]<self.data[j-1] and j>0):
                self.data[j],self.data[j-1]=self.data[j-1],self.data[j]
                j-=1
        return self.data





n=int(input())
data=list(map(int,input().split()))
obj1=Sorting(n,data)
print(*obj1.Insertion_sort())


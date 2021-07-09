class Sorting:
    def __init__(self,n,data):
        self.n=n
        self.data=data
    def Bubble_sort(self):
        for i in range(self.n,0,-1):
            swap=0
            for j in range(i-1):
                if(self.data[j+1]<self.data[j]):
                    self.data[j+1],self.data[j]=self.data[j],self.data[j+1]
                    swap=1
            if(swap==0):                 #if the no.of swaps==0 then in this sort data is sorted..
                return self.data
        return self.data





n=int(input())
data=list(map(int,input().split()))
obj1=Sorting(n,data)
print(*obj1.Bubble_sort())

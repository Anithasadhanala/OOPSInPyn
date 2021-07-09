class Sorting:
    def __init__(self,n,data):
        self.n=n
        self.data=data
    def Bubble_sort_ascending(self):                #ascending sort using bubble sort
        for i in range(self.n-1,0,-1):
            maxi=self.data[i]
            count=i
            for j in range(i):
                if(maxi<self.data[j]):
                    maxi=self.data[j]
                    count=j
            self.data[count],self.data[i]=self.data[i],self.data[count]

        return self.data
    
    def Bubble_sort_decending(self):                #decending sort using bubble sort
        for i in range(0,self.n-1):
            maxi=self.data[i]
            count=i
            for j in range(i,n):
                if(maxi<self.data[j]):
                    maxi=self.data[j]
                    count=j
            self.data[count],self.data[i]=self.data[i],self.data[count]
       
        return self.data

    

n=int(input())
data=list(map(int,input().split()))
obj1=Sorting(n,data)
print(*obj1.Bubble_sort_ascending())            # here "*" is for printing the all elements normally
print(*obj1.Bubble_sort_decending())

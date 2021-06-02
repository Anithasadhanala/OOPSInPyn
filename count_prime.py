def sumofdigits(n,data):
    m=0
    for i in data:
        add=0
        while(i):
            k=i%10
            i=i%10
            add+=k
    
        data[m]=add
        m+=1
    return data
    
            
                


n=int(input())
data=list(map(int,input().split()))
sumofdigits(n,data)
print(*data)

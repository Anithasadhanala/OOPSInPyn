def find_min(n,data):
    mini=data[0]
    maxi=data[0]
    count=0
    minVal=[]
    for i in data:
        if(mini>i):
            mini=i
    minVal.append(i)
    list_a=[]
    for j in range(n):
        if(mini==data[j]):
            count+=1
            list_a.append(j)
            
            
    minVal.append(count)
    minVal.extend(list_a)
    return minVal
         


n=int(input())
data=list(map(int,input().split()))
minVal=find_min(n,data)
print(*minVal)


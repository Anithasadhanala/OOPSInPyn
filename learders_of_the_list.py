def find_an_item_as_leader(n,data):
    list_a=[]
    
    for i in range(n):
        if(i<n-1):
            
            maxi=max(data[i+1:])
            print(data[i+1:])
            
        if(data[i]>=maxi):
            list_a.append(data[i])
        
    return list_a



n=int(input())
data=list(map(int,input().split()))
leader=find_an_item_as_leader(n,data)
print(*leader)

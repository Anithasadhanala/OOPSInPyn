def finding_sec_index(n,data,val):
    count=0
    if(data.count(val)>1):
        for i in range(len(data)):
            if(data[i]==val):
                count+=1
            if(count==2):
                return i
    else:
        return "2nd index not found"



        
n=int(input())
data=list(map(int,input().split()))
val=int(input())
index=finding_sec_index(n,data,val)
print(index)

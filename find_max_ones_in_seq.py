def finding_max_ones_in_seq(n,data):
    count=0
    list_a=[]
    for i in data:
        if(i==1):
            count+=1
            list_a.append(count)
        else:
            count=0
    
    return max(list_a)



n=int(input())
data=list(map(int,input().split()))
max_ones=finding_max_ones_in_seq(n,data)
print(max_ones)

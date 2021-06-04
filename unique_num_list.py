def unique_num(n,data):
    list_a=[]
    list_a.append(data[0])
    for i in data:
        if(i not in list_a):
             list_a.append(i)

    
    return list_a


n=int(input())
data=list(map(int,input().split()))
list_a=unique_num(n,data)
print(*list_a)

    

def unique_num(n,data):
    list_a=[]
    count=0
    list_a.append(data[0])
    for i in data:
        if(i not in list_a):
             list_a.append(i)
    for i in range(len(list_a)):
        if(data[i]==list_a[i]):
            count+=1
    
    return count
    


n=int(input())
data=list(map(int,input().split()))
count=unique_num(n,data)
print(count)

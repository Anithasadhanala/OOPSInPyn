def unique_elements(n,data):
    list_b=[]
    list_b.append(data[0])
    for i in range(n):
        if data[i] not in list_b:
            list_b.append(data[i])

    return list_b

def list_of_count(unique_list,data):
    list_of_count=[]
    for i in unique_list:
        k=data.count(i)
        list_of_count.append(k)
    return list_of_count

def min_visitors(n,data):
   
    unique_list=unique_elements(n,data)
    count_list=list_of_count(unique_list,data)
    
    mini=min(count_list)

    list_c=[]
    for i in range(n):
        v=data.count(data[i])
        if(mini==v):
            list_c.append(data[i])
 
    visitors=unique_elements(len(list_c),list_c)
    
    return visitors
    
        

n=int(input())
data=list(map(int,input().split()))
visitors=min_visitors(n,data)
print(*visitors)

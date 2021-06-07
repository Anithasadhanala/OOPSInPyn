def sorted_or_not(n,data):
    list_a=[]
    k=data
    list_a.append(k)
    data2=sorted(data)
    data3=sorted(data2,reverse=True)
    list_a.append(data2)
    list_a.append(data3)
    
    if (list_a[0]==list_a[1]) or (list_a[0]==list_a[2]):
        return "Given list is sorted"
    return "Given list is not sorted"


n=int(input())
data=list(map(int,input().split()))
bool_val=sorted_or_not(n,data)
print(bool_val)


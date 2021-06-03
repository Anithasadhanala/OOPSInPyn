def reverse_of_each(k):
    rev=0
    while(k):
        m=k%10
        k=k//10
        rev=rev*10+m
    return rev


def reverse(n,data):
    for i in range(n):
        data[i]=reverse_of_each(data[i])
    
        
n=int(input())
data=list(map(int,input().split()))
reverse(n,data)
print(*data)

def finding_second_largest(n,data):
    k=max(data)
    for i in range(n):
        if(data[i]==k):
            data[i]=0

    return max(data)





n=int(input())
data=list(map(int,input().split()))
sec_min=finding_second_largest(n,data)
print(sec_min)

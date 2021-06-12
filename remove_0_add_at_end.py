def move_zeros(n,data):
    for i in range(n):
        if(data[i]==0):
            data.remove(0)
            data.append(0)



n=int(input())
data=list(map(int,input().split()))
move_zeros(n,data)
print(*data)

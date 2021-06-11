def finding_bouncy(n,data):
    count_a=0
    count_b=0
    list_a=[]
    for i in range(n):
        if(i<=n-2):
            if data[i]>data[i+1]:
                list_a.append(1)
            elif data[i]==data[i+1]:
                list_a.append(8)
            else:
                list_a.append(0)
    if(data[n-1]>data[n-2]):
        list_a.append(1)
    elif data[n-1]==data[n-2]:
        list_a.append(8)
    else:
        list_a.append(0)
    
    if(8 not in list_a):
        if(list_a[0]==1):
           for i in range(n):
               if(i%2==0):
                   if(list_a[i]!=1):
                       return False
               else:
                   if(list_a[i]!=0):
                       return False
        elif(list_a[0]==0):
            for i in range(n):
                if(i%2==0):
                   if(list_a[i]!=0):
                       return False
                else:
                    if(list_a[i]!=1):
                        return False
        return True

    return False


n=int(input())
data=list(map(int,input().split()))
bouncy=finding_bouncy(n,data)
print(bouncy)


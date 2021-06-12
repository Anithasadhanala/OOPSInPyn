def rotate_the_list(n,data,rotate):
    
    if(rotate%n!=0):                                        #if the rotate is multiple of n then the same data
       if(rotate>n):                          
            for i in range(rotate%n):                       # if the rotate is > n then ,no need to ratate for those many times
                k=data[0]                 
                data.remove(k)
                data.append(k)
       else:
            for i in range(rotate):                         # if the rotate is < n then, rotating those many times.....
                k=data[0]           
                data.remove(k)
                data.append(k)


n=int(input())
data=list(map(int,input().split()))
rotate=int(input())
rotate_the_list(n,data,rotate)
print(*data)

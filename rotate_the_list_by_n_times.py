def rotate_the_list(n,data,rotate):
    
    if(rotate%n!=0):            #If the no,of items is the multiple of 
        for i in range(rotate): # the rotate then no need to rotate as
            k=data[0]           # we get the same data..
            data.remove(k)
            data.append(k)



n=int(input())
data=list(map(int,input().split()))
rotate=int(input())
rotate_the_list(n,data,rotate)
print(*data)

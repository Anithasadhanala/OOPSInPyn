def count_of_prime(n,data):
    pc=0
    
    for i in data:
        prime=True
        count=0
        if(i==1):
            count+=1
        if(i==2):
            count=0
            pc+=1
        s=int(i**(1/2))+1
        
        for j in (2,s):
            if (i%j==1):
                count+=1
        data=[]
        if (count>1):
            pc+=1
            m=i
            add=0
            while(m):
                l=m%10
                m=m%10
                add+=l
            data[o]=add
            o+=1
    return data
          
    

n=int(input())
data=list(map(int,input().split()))
pc=count_of_prime(n,data)
print(*data)


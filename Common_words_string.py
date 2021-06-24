def fun(s1,s2):
    d1=s1.split()
    d2=s2.split()
    s=""
    k=[]
    count=0
    for i in range(len(d1)):
        
        if(d1[i] not in k):
            if(d1[i] in d2):
                s+=d1[i]
                s+=" "
                count+=1
                
        k.append(d1[i])
    
    return [count,s]


s1=input()
s2=input()
s=fun(s1,s2)
print(*s)

def fun(s1,s2):
    s=""
    
    for i in range(len(s1)):
        k=s1[:i]
        if(s1[i] not in k):
            if(s1[i] in s2):
                s+=s1[i]
    return s


s1=input()
s2=input()
s=fun(s1,s2)
print(s)



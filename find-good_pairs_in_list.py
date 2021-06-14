def finding_good_pairs(n,data):
    count=0
    k=0
    for i in range(n):                      #1 2 1 3 1
        k+=1                                #pairs=(1 1),(1 1),(1 1)
        for j in range(k,n):  
            if(data[i]==data[j]):
                count+=1
                
    return count


        

n=int(input())
data=list(map(int,input().split()))
good_pairs=finding_good_pairs(n,data)
print(good_pairs)

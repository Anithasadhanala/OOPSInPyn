def find_min_max(n,data):
    mini=data[0]
    maxi=data[0]
    for i in range(n):
        if(mini>data[i]):
            mini=data[i]
            p=i
            
        if(maxi<data[i]):
            maxi=data[i]
            
    return mini,maxi

def rev_of_num(mini,maxi):
    rev2=0
    rev1=0
    while(mini):
        k=mini%10
        mini=mini//10
        rev1=rev1*10+k
    while(maxi):
        k=maxi%10
        maxi=maxi//10
        rev2=rev2*10+k
    return rev1,rev2
    
def super_min_max(n,data):
    
    mini,maxi=find_min_max(n,data)

    
    rev_min,rev_max=rev_of_num(mini,maxi)
    

    data.remove(mini)
    data.remove(maxi)
    
    data.append(rev_min)
    data.append(rev_max)
    

    final_min,final_max=find_min_max(n,data)
    

    if(final_min==rev_min):
        print("Super min found")
    else:
        print("No super min")
    if(final_max==rev_max):
        print("Super max found")
    else:
        print("No super max")
        

n=int(input())
data=list(map(int,input().split()))
super_min_max(n,data)

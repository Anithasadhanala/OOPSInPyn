def finding_max_sorted_list(n,data):
    a=0
    b=1
    len_list=[]                 #given:-1 2 3 1 4 1 2 3 4 5 n=10
    for i in range(2,n+1):      #here 1 2 3, 1 4, 1 2 3 4 5 are sorted
                                #among the lists, the max_len_of_list is 3rd one
        s1=sorted(data[a:b+1])  #so, the output is 5
        
        if(s1==data[a:b+1]):
            length=len(data[a:b+1])
            b=i
            len_list.append(length)
            
        else:
            a=i-1
            b=i

    max_sorted_items=max(len_list)
    return max_sorted_items
    


n=int(input())
data=list(map(int,input().split()))
len_max_sorted=finding_max_sorted_list(n,data)
print(len_max_sorted)

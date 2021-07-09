def Batsman_no(n,data):
    first=1
    second=2
    for i in range(n):          #this problem is finding which bats man hits the next ball
        if(i+1)%6==0:
            if(data[i]==-1):                 #keys:
                first=second+1               #1.no_balls=n and runs=data if data has -1 
                first,second=second,first    # then that person is out
            else:                       
                first,second=second,first
        else:                                # if odd data[i](runs) swap the batsman
            if(data[i]%2==1 and data[i]>0):  # if 6th ball i%6==0 then swap
                first,second=second,first    # if -1 i.e first placed man is out and next 
                                             # man comes if it is 6th ball then change and swap
            if(data[i]==-1):
                maxi=max([first,second])
                first=maxi+1
                
    return first

        
n=int(input())
data=list(map(int,input().split()))
ans=Batsman_no(n,data)
print(ans)

s=input()
data=s.split()
maxi=len(data[0])
k=0
for i in range(len(data)):
    if(maxi<len(data[i])):
       maxi=len(data[i])
       k=i
print(k,data[k],len(data[k]))

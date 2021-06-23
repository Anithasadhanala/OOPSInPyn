s=input()
data=s.split()
for i in data:
    for j in range(len(i)-1,-1,-1):
        print(i[j],end="")
    print(" ",end="")
    

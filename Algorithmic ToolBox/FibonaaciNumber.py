n=int(input())
l=[0]*(n)
l[0]=0
l[1]=1
if n==1:
    print(l[0])
elif n==2:
    print(l[0],l[1])
else:
    for i in range(2,n):
        l[i]=(l[i-1]+l[i-2])
print(*l)

    
